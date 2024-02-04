"""
TODO: Write a parser script to read this file and dynamically generate the
TODO: airgoodies.{module}.variables.json

@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.3
"""


class Common:
    DAG_ID_VARIABLE: str = '{dag_id}'


class AWSVariables:
    """"
    Variables for AWS S3 goodies.
    """
    __PACKAGE: str = 'airgoodies.aws'
    S3_CONNECTION_NAME: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-aws-s3-connection-name'
    S3_DEFAULT_BUCKET: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-aws-s3-default-bucket'


class MongoVariables:
    """
    Variables for Mongo DB goodies.
    """
    __PACKAGE: str = 'airgoodies.mongo'
    CONNECTION_URL: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-mongo-db-connection-url'
    DEFAULT_DB_NAME: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-mongo-db-name'


class CommandParserVariables:
    """
    Variables for YAML CommandParser.
    """
    __PACKAGE: str = 'airgoodies.command'
    AIRGOODIES_TASK: str = 'airgoodies_task'
    CUSTOM_TASK: str = 'custom_task'
    CONFIG_FILE_KEY: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-dag-config-file-key'

    # Callables
    LOAD_S3_TO_MONGO: str = f'load_from_s3_to_mongo_table'


class AWSTasksVariables:
    """
    Variables for AWS Tasks.
    """
    __PACKAGE: str = 'airgoodies.task'
    INPUT_FILE_VARIABLE: str = f'{Common.DAG_ID_VARIABLE}.airgoodies-task-aws-load-from-s3-to-mongo-input-file-variable'
