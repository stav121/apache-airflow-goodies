"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.2
"""


class XComManager:
    """
    XCom manager utility, contains methods used to manage values and variables across
    tasks.
    """
    from airflow.models.taskinstance import TaskInstance
    import logging

    _logger: logging.Logger = logging.getLogger(name='airflow.task')
    _ti: TaskInstance
    _task_id: str
    _run_id: str
    _shared_data: dict = {}

    def __init__(self, ti: TaskInstance) -> None:
        """
        Initialize the manager with information from the TaskInstance.

        Pulls the current shared variables of the tasks from XCom and saves it
        for easy access.

        :param ti: the current task instance
        """
        from airflow.models.taskinstance import TaskInstance
        import json

        self._ti: TaskInstance = ti
        self._task_id: str = ti.task_id
        self._run_id: str = ti.run_id
        self._logger.info(msg=f'Initializing XCom manager for task {self._task_id}')
        _xcom_val: str = ti.xcom_pull(key=f'{self._run_id}_variables')
        if _xcom_val is None:
            self._shared_data: dict = {}
        else:
            self._shared_data: dict = json.loads(_xcom_val)
        self._logger.info(self._shared_data)

    def get_variable(self, name: str) -> str | dict:
        """
        Get the value of the provided property saved in XCom
        :param name: the name of the variable
        :return: the found value
        """
        from airgoodies.common.exception import ValueNotFoundException

        if not self._shared_data[name]:
            raise ValueNotFoundException(property=name)

        return self._shared_data[name]

    def set_variable(self, name: str, value: str | dict) -> None:
        """
        Set provided variable with the given value
        :param name: the name of the variable
        :param value: the value to be saved
        """
        self._shared_data[name] = value
        self._dump_variables()

    def remove_variable(self, name: str) -> None:
        """
        Remove a value from the shared variables of the DAG run.
        :param name: name of the variable
        """
        del self._shared_data[name]
        self._dump_variables()

    def clear_variables(self) -> None:
        """
        Clear the variables of the dag run.
        """
        self._shared_data = {}
        self._dump_variables()

    def _dump_variables(self) -> None:
        """
        Push the current value of self._shared_data variables to XCom
        """
        import json

        self._ti.xcom_push(key=f'{self._run_id}_variables', value=json.dumps(self._shared_data))
