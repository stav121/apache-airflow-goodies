"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.1-alpha
"""


class MongoConnection:
    from pymongo import MongoClient
    from pymongo.database import Database
    """
    Mongo connection class, contains the configuration and creates an open connection
    with the configured MongoDB.
    """

    _conn_url: str
    _db_name: str
    _client: MongoClient
    _db: Database

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
        from airgoodies.common.variables import MongoVariables

        logger = logging.getLogger('airflow.task')

        logger.info('Retrieving Mongo connection')
        self._conn_url = Variable.get(key=MongoVariables.CONNECTION_URL)
        self._db_name = Variable.get(key=MongoVariables.DEFAULT_DB_NAME)

        # Raise exception if none of the above were found.
        if not self._conn_url:
            raise ConfigNotFoundException(MongoVariables.CONNECTION_URL)
        if not self._db_name:
            raise ConfigNotFoundException(MongoVariables.DEFAULT_DB_NAME)

        logger.info('Connecting to MongoDB...')
        self._client = MongoClient(host=self._conn_url)
        self._db = self._client.get_database(name=self._db_name)
        logger.info('Connected successfully')

    def get_db(self) -> Database:
        """
        Get the created database connection.
        :return: the created database connection.
        """
        return self._db
