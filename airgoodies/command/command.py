"""
@author: Stavros Grigoriou
@since: 0.0.4
"""


class AirgoodiesCommand:
    """
    Airgoodies Command class, contains the metadata and callable for an Airgoodies compatible command.
    """
    from airflow.operators.python import PythonOperator
    from airflow import DAG

    _task_id: str
    _python_callable: callable
    _provide_context: bool = True

    def __init__(self,
                 task_id: str,
                 python_callable: callable,
                 provide_context: bool = True):
        """
        Command initializer.
        """
        self._task_id = task_id
        self._python_callable = python_callable
        self._provide_context = provide_context

    def to_operator(self, dag=DAG) -> PythonOperator:
        """
        Convert the command in to a PythonOperator usable by Apache Airflow.

        :return: A setup python operator.
        """
        from airflow.operators.python import PythonOperator

        return PythonOperator(task_id=self._task_id,
                              python_callable=self._python_callable,
                              provide_context=self._provide_context,
                              dag=dag)
