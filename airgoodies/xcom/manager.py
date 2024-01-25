"""
@author: Stavros Grigoriou <unix121@protonmail.com>
"""


class XComManager:
    """
    XCom manager utility, contains methods used to manage values and variables across
    tasks.
    """
    from airflow.models.taskinstance import TaskInstance
    import logging

    __logger: logging.Logger = logging.getLogger(name='airflow.task')
    __ti: TaskInstance
    __task_id: str
    __run_id: str
    __shared_data: dict = {}

    def __init__(self, ti: TaskInstance) -> None:
        """
        Initialize the manager with information from the TaskInstance.

        Pulls the current shared variables of the tasks from XCom and saves it
        for easy access.

        :param ti: the current task instance
        """
        from airflow.models.taskinstance import TaskInstance
        import json

        self.__ti: TaskInstance = ti
        self.__task_id: str = ti.task_id
        self.__run_id: str = ti.run_id
        self.__logger.info(msg=f'Initializing XCom manager for task {self.__task_id}')
        __xcom_val: str = ti.xcom_pull(key=f'{self.__run_id}_variables')
        if __xcom_val is None:
            self.__shared_data: dict = {}
        else:
            self.__shared_data: dict = json.loads(__xcom_val)
        self.__logger.info(self.__shared_data)

    def get_variable(self, name: str) -> str | dict:
        """
        Get the value of the provided property saved in XCom
        :param name: the name of the variable
        :return: the found value
        """
        from airgoodies.common.exception import ValueNotFoundException

        if not self.__shared_data[name]:
            raise ValueNotFoundException(property=name)

        return self.__shared_data[name]

    def set_variable(self, name: str, value: str | dict) -> None:
        """
        Set provided variable with the given value
        :param name: the name of the variable
        :param value: the value to be saved
        """
        self.__shared_data[name] = value
        self.__dump_variables()

    def remove_variable(self, name: str) -> None:
        """
        Remove a value from the shared variables of the DAG run.
        :param name: name of the variable
        """
        del self.__shared_data[name]
        self.__dump_variables()

    def clear_variables(self) -> None:
        """
        Clear the variables of the dag run.
        """
        self.__shared_data = {}
        self.__dump_variables()

    def __dump_variables(self) -> None:
        """
        Push the current value of self.__shared_data variables to XCom
        """
        import json

        self.__ti.xcom_push(key=f'{self.__run_id}_variables', value=json.dumps(self.__shared_data))
