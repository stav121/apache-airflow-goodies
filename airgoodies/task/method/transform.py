from pandas import DataFrame
from typing import Callable
"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


def _print_table_contents(data: DataFrame, config: dict = None) -> DataFrame:
    """
    Print the contents of the provided datatable.

    :param data: the input data
    """
    from logging import Logger, getLogger

    logger: Logger = getLogger(name='airflow.task')

    logger.info('Executing `print_table_contents` callable')

    logger.info(data)

    return data


def _drop_columns(data: DataFrame, config: dict) -> DataFrame:
    """
    Drop the selected column(s) from the imported data.

    :param data: the input data
    :param config: the columns to drop
    """
    from logging import Logger, getLogger

    logger: Logger = getLogger(name='airflow.task')

    if 'drop_columns_val' in config:
        columns: [str] = config['drop_columns_val']
        logger.info(
            f'Executing `drop_column` callable for columns <{columns}>')
        data = data.drop(columns=columns)

    return data


def resolve(name: str) -> Callable[[DataFrame, dict], DataFrame]:
    """
    Resolve the provided airgoodies transform method callable if it exists.
    :param name: the name of the airgoodies transform method to resolve
    :return: the callable of the method
    """
    if name == 'print_table_contents':
        return _print_table_contents
    elif name == 'drop_columns':
        return _drop_columns
    else:
        raise Exception(
            f'airgoodies_transform_method with name <{name}> not found')
