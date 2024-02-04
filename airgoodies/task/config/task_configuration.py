"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since 0.0.4
"""


class TaskConfig:
    from logging import Logger, getLogger
    from airflow.models import TaskInstance
    from airgoodies.util.annotation import provide_dag_id
    from airgoodies.aws.s3.wrapper import S3Wrapper

    _logger: Logger = getLogger(name='airflow.task')
    _s3_wrapper: S3Wrapper = None
    _task_config: dict = None
    _airgoodies_command: str = None

    @provide_dag_id
    def __init__(self,
                 task_instance: TaskInstance,
                 s3_wrapper: S3Wrapper,
                 task_id: str,
                 dag_id: str | None = None) -> None:
        import yaml
        from airgoodies.aws.s3.wrapper import S3Wrapper
        from airgoodies.common.variables import CommandParserVariables, Common
        from airflow.models import Variable
        from io import StringIO

        self._s3_wrapper: S3Wrapper = s3_wrapper

        # Load the configuration of the task
        self._task_config: dict = yaml.safe_load(
            StringIO(
                self._s3_wrapper.load_file(key=Variable.get(
                    CommandParserVariables.CONFIG_FILE_KEY.replace(
                        Common.DAG_ID_VARIABLE, dag_id)))))[task_id]

        self._airgoodies_command: str = self._task_config[
            CommandParserVariables.AIRGOODIES_TASK]

        self._logger.info(f'Loaded task config: {self._task_config}')
        self._logger.info(f'Config: {self._task_config["config"]}')

    def get_config(self, conf: str) -> str | None:
        """
        Retrieve the requested configuration from the `config` section.
        :param conf: the name of the configuration property
        :return: the value if it exists
        """
        if 'config' in self._task_config:
            if conf in self._task_config['config']:
                return self._task_config['config'][conf]

        return None
