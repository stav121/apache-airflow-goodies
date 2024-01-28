"""
TODO: Write a parser script to read this file and dynamically generate the
TODO: airgoodies.{module}.variables.json

@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.3
"""


class AWSVariables:
    """"
    Variables for AWS S3 goodies.
    """
    __PACKAGE: str = 'airgoodies.aws'
    S3_CONNECTION_NAME: str = 'airgoodies-aws-s3-connection-name'
    S3_DEFAULT_BUCKET: str = 'airgoodies-aws-s3-default-bucket'


class MongoVariables:
    """
    Variables for Mongo DB goodies.
    """
    __PACKAGE: str = 'airgoodies.mongo'
    CONNECTION_URL: str = 'airgoodies-mongo-db-connection-url'
    DEFAULT_DB_NAME: str = 'airgoodies-mongo-db-name'
