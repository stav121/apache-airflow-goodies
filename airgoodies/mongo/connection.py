"""
@author Stavros Grigoriou <unix121@protonmail.com>
"""


class MongoConnection:
    from pymongo import MongoClient
    from pymongo.database import Database
    """
    Mongo connection class, contains the configuration and creates an open connection
    with the configured MongoDB.
    """

    __conn_url: str
    __db_name: str
    __client: MongoClient
    __db: Database

    def __init__(self):
        """
        Constructor, requires the existence of the following Airflow Variables:
        * airgoodies-mongo-db-connection-url
        * airgoodies-mongo-db-name

        @see airgoodies/mongo/airgoodies.mongo.variables.json
        """
        import logging
        from airflow.models import Variable
        from airgoodies.common.exception import ConfigNotFoundException
        from pymongo import MongoClient

        logger = logging.getLogger('airflow.task')

        logger.info('Retrieving Mongo connection')
        self.__conn_url = Variable.get('airgoodies-mongo-db-connection-url')
        self.__db_name = Variable.get('airgoodies-mongo-db-name')

        # Raise exception if none of the above were found.
        if not self.__conn_url:
            raise ConfigNotFoundException('airgoodies-mongo-db-connection-url')
        if not self.__db_name:
            raise ConfigNotFoundException('airgoodies-mongo-db-name')

        logger.info('Connecting to MongoDB...')
        self.__client = MongoClient(host=self.__conn_url)
        self.__db = self.__client.get_database(name=self.__db_name)
        logger.info('Connected successfully')

    def get_db(self) -> Database:
        """
        Get the created database connection.
        :return: the created database connection.
        """
        return self.__db
