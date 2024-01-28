"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.3
"""


class S3Wrapper:
    """
    Wrapper class for simple interactions with S3.

    Contains utilities such as, load CSV to pandas, load Excel etc.
    """
    from logging import Logger, getLogger
    from airflow.providers.amazon.aws.hooks.s3 import S3Hook
    from pandas import DataFrame
    from typing import Callable
    from airgoodies.mongo.connection import MongoConnection

    _logger: Logger = getLogger('airflow.task')
    _conn_name: str
    _s3_hook: S3Hook
    _default_bucket: str = None

    def __init__(self, connection_name: str | None = None) -> None:
        """
        Initialize the connection to S3 with either the provided connection_name or
        the pre-configured from the variable:

        * airgoodies-aws-s3-connection-name

        Also sets the value of the default bucket if provided through the property:

        * airgoodies-aws-s3-default-bucket

        :param connection_name: the (optional) connection name to use
        """

        from airflow.models import Variable
        from airgoodies.common.exception import ConfigNotFoundException
        from airflow.providers.amazon.aws.hooks.s3 import S3Hook
        from airgoodies.common.variables import AWSVariables

        if connection_name is None:
            # Load from variable
            self._conn_name = Variable.get(key=AWSVariables.S3_CONNECTION_NAME)
            if self._conn_name is None:
                raise ConfigNotFoundException(AWSVariables.S3_CONNECTION_NAME)
        else:
            # Load from the provided name
            self._conn_name = connection_name

        if Variable.get(key=AWSVariables.S3_DEFAULT_BUCKET) is not None:
            self._default_bucket = Variable.get(key=AWSVariables.S3_DEFAULT_BUCKET)

        self._s3_hook: S3Hook = S3Hook(aws_conn_id=self._conn_name)

    def get_s3_hook(self) -> S3Hook:
        """
        Get the value of the self._s3_hook property
        """
        return self._s3_hook

    def load_file(self, key: str, bucket_name: str | None = None) -> str | None:
        """
        Load the provided key from the provided or default bucket.

        :param key: the fully qualified key of the file
        :param bucket_name: alternative bucket name otherwise it will use the default
        """
        if bucket_name is None:
            bucket_name = self._default_bucket

        file: str = self._s3_hook.read_key(key=key, bucket_name=bucket_name)

        return file

    def load_as_dataframe(self, key: str, bucket_name: str | None = None, sep: str = ',') -> DataFrame:
        """
        Load the provided file from S3 into a pandas DataFrame.

        :param key: the key of the file
        :param bucket_name: (optional) bucket name to fetch from
        :param sep: (optional) csv separator
        :return: Pandas DataFrame
        """
        from pandas import read_csv, read_excel
        from io import StringIO
        from airgoodies.common.exception import FileNotFoundException, UnsupportedFileFormatException

        file: StringIO = StringIO(self.load_file(key=key, bucket_name=bucket_name))

        if file is None:
            raise FileNotFoundException(filename=key)

        if key.lower().endswith('.csv'):
            return read_csv(filepath_or_buffer=file, sep=sep)
        elif key.lower().endswith(('.xls', '.xlsx')):
            return read_excel(io=file)
        else:
            raise UnsupportedFileFormatException()

    def load_and_transform(self,
                           key: str,
                           bucket_name: str | None = None,
                           transform_method: Callable[[DataFrame], DataFrame] | None = None,
                           sep: str | None = None) \
            -> DataFrame:
        """
        Load the provided key from S3 and perform the provided transform action on it.

        :param key: the key of the file
        :param bucket_name: (optional) bucket name to fetch from
        :param transform_method: the transformation method to use on the fetched file
        :param sep: (optional) csv separator
        :return: Pandas DataFrame
        """
        from pandas import DataFrame

        result: DataFrame = self.load_as_dataframe(key=key, bucket_name=bucket_name, sep=sep)

        if transform_method is None:
            return result
        else:
            return transform_method(result)

    def load_to_mongo(self,
                      key: str,
                      connection: MongoConnection,
                      load_table_name: str,
                      bucket_name: str | None = None,
                      transform_method: Callable[[DataFrame], DataFrame] | None = None,
                      sep: str | None = None) \
            -> str:
        """
        Load the provided file into the provided mongoDB table.

        Optionally perform the provided transformation on the table.

        :param key: the file to load
        :param connection: the mongoDB connection
        :param load_table_name: the name of the table to insert into
        :param bucket_name: the name of the bucket to load from (optional)
        :param transform_method: the (optional) transformation method
        :param sep: the (optional) csv separator
        """
        from pandas import DataFrame
        from json import loads

        data: DataFrame

        if transform_method is None:
            data = self.load_as_dataframe(key=key, bucket_name=bucket_name, sep=sep)
        else:
            data = self.load_and_transform(key=key, bucket_name=bucket_name, transform_method=transform_method, sep=sep)

        connection.get_db().get_collection(name=load_table_name).insert_many(loads(data.to_json(orient='records')))

        return load_table_name
