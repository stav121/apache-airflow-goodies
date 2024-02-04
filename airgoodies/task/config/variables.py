"""
Configuration options for Airgoodies supported commands.

@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


class CommonTaskOptions:
    """
    Configuration options, common across multiple tasks.
    """
    OUTPUT_TABLE_NAME: str = 'output_table_name'


class AwsS3ToMongoTableOptions:
    """
    Configuration options for `load_from_s3_to_mongo_table` command.
    """
    AIRGOODIES_TRANSFORM_METHOD: str = 'airgoodies_transform_method'
    CUSTOM_TRANSFORM_METHOD: str = 'custom_transform_method'
