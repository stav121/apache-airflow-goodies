"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


class CommandParser:
    """
    Command Parser for Airgoodies supported YAML format.

    Parses the provided YAML file and creates a list of AirgoodiesCommand with the provided target callable.
    """
    from airgoodies.command.command import AirgoodiesCommand
    from airgoodies.xcom.manager import XComManager
    from airflow import DAG
    from airgoodies.util.annotation import provide_dag_id

    _config: dict = None
    _commands: [AirgoodiesCommand] = []
    _xcom_manager: XComManager

    @provide_dag_id
    def __init__(self,
                 dag: DAG,
                 dag_id: str | None = None,
                 yaml_file: str | None = None):
        """
        Constructor used to initialize the parser.
        """
        import yaml
        from io import StringIO
        from airflow.models import Variable
        from airgoodies.common.variables import CommandParserVariables, Common

        if Variable.get(
                CommandParserVariables.CONFIG_FILE_KEY.replace(
                    Common.DAG_ID_VARIABLE, dag_id)) is not None:
            from airgoodies.aws.s3.wrapper import S3Wrapper
            # Load the configuration file from S3 bucket
            yaml_file: str = S3Wrapper(dag_id=dag_id).load_file(
                key=Variable.get(
                    CommandParserVariables.CONFIG_FILE_KEY.replace(
                        Common.DAG_ID_VARIABLE, dag_id)))
        elif yaml_file is None:
            raise Exception("No YAML file provided")

        self._config: dict = yaml.safe_load(stream=StringIO(
            initial_value=yaml_file))

        self._parse()

    def _parse(self) -> None:
        """
        Parse the provided command into a list of AirgoodiesCommand.
        """
        from airgoodies.command.command import AirgoodiesCommand
        from airgoodies.common.variables import CommandParserVariables

        for _key in self._config.keys():
            _airgoodies_callable: dict = self._config[_key]

            if CommandParserVariables.AIRGOODIES_TASK in self._config[_key]:
                # Aigoodies provided task callable
                self._commands.append(
                    AirgoodiesCommand(
                        task_id=_key,
                        python_callable=CommandParser._pick_callable(
                            _callable_name=_airgoodies_callable[
                                CommandParserVariables.AIRGOODIES_TASK])))
            elif CommandParserVariables.CUSTOM_TASK in self._config[_key]:
                # User provided task module
                from importlib import import_module

                module_name, method_name = self._config[_key][
                    CommandParserVariables.CUSTOM_TASK].rsplit('.', 1)
                imported_module = import_module(module_name)
                python_callable: callable = getattr(imported_module,
                                                    method_name)

                self._commands.append(
                    AirgoodiesCommand(task_id=_key,
                                      python_callable=python_callable))

    def get_commands(self) -> [AirgoodiesCommand]:
        """
        Retrieve the list of parsed commands.
        """
        return self._commands

    @staticmethod
    def _pick_callable(_callable_name: str) -> callable:
        """
        Static method used to pick the executable suitable for the provided name.

        If no registered airgoodies_command exists, None is returned

        :param _callable_name: the name of the callable to match
        """
        from airgoodies.task.aws_tasks import load_from_s3_to_mongo_table
        from airgoodies.common.variables import CommandParserVariables

        if _callable_name == CommandParserVariables.LOAD_S3_TO_MONGO:
            return load_from_s3_to_mongo_table
        else:
            return None
