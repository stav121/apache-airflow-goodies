from airflow.models import TaskInstance
"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


def load_from_s3_to_mongo_table(ti: TaskInstance, **kwargs) -> None:
    """
    Task that uses the S3Wrapper and MongoConnection to load a file from the configured Bucket
    directly into a MongoDB datatable.

    :param ti: the TaskInstance of the task
    :param kwargs: args
    """
    from logging import Logger, getLogger
    from airgoodies.aws.s3.wrapper import S3Wrapper
    from airgoodies.mongo.connection import MongoConnection
    from airflow.models import Variable
    from typing import Callable
    from airgoodies.common.variables import AWSTasksVariables, Common
    from airgoodies.task.config.task_configuration import TaskConfig
    from airgoodies.task.config.variables import AwsS3ToMongoTableOptions, CommonTaskOptions
    from airgoodies.task.method.transform import resolve
    from pandas import DataFrame

    logger: Logger = getLogger(name='airflow.task')

    logger.info(f'airgoodies::load_from_s3_to_mongo_table: {ti.task_id}')

    input_file_variable: str = Variable.get(
        AWSTasksVariables.INPUT_FILE_VARIABLE.replace(Common.DAG_ID_VARIABLE,
                                                      ti.dag_id))

    logger.info(
        f'Looking for value of <{input_file_variable}> in provided configuration.'
    )

    input_file: str = kwargs['dag_run'].conf[input_file_variable]

    # Load the S3Wrapper and the MongoConnection
    s3_wrapper: S3Wrapper = S3Wrapper(task_instance=ti)
    task_configuration: TaskConfig = TaskConfig(task_instance=ti,
                                                s3_wrapper=s3_wrapper,
                                                task_id=ti.task_id)

    transform_method: Callable[[DataFrame], DataFrame] | None = None
    if task_configuration.get_config(conf=AwsS3ToMongoTableOptions.
                                     AIRGOODIES_TRANSFORM_METHOD) is not None:
        # Load the transform method
        transform_method: Callable = resolve(
            name=task_configuration.get_config(
                conf=AwsS3ToMongoTableOptions.AIRGOODIES_TRANSFORM_METHOD))
    elif task_configuration.get_config(
            conf=AwsS3ToMongoTableOptions.CUSTOM_TRANSFORM_METHOD) is not None:
        from importlib import import_module
        # Load from locals
        custom_method: str = task_configuration.get_config(
            conf=AwsS3ToMongoTableOptions.CUSTOM_TRANSFORM_METHOD)
        module_name, method_name = custom_method.rsplit('.', 1)
        logger.info(
            f'Importing custom transform_method <{method_name}> from <{module_name}>'
        )
        imported_module = import_module(module_name)
        transform_method: Callable[[DataFrame], DataFrame] = getattr(
            imported_module, method_name)

    mongo_conn: MongoConnection = MongoConnection(dag_id=ti.dag_id)

    out_table_name: str = f'{ti.task_id}_out_table' if task_configuration.get_config(
        conf=CommonTaskOptions.OUTPUT_TABLE_NAME
    ) is None else task_configuration.get_config(
        conf=CommonTaskOptions.OUTPUT_TABLE_NAME)

    # Load the file from S3 into MongoDB
    s3_wrapper.load_to_mongo(
        key=input_file,
        connection=mongo_conn,
        transform_method=transform_method,
        load_table_name=out_table_name)  # TODO: add to config
