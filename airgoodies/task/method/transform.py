from pandas import DataFrame
from typing import Callable
"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


def _print_table_contents(data: DataFrame) -> DataFrame:
    """
    Print the contents of the provided datatable.

    :param data: the input data
    """
    from logging import Logger, getLogger

    logger: Logger = getLogger('airflow.task')

    logger.info('Executing `print_table_contents` callable')

    logger.info(data)

    return data


def resolve(name: str) -> Callable[[DataFrame], DataFrame]:
    """
    Resolve the provided airgoodies transform method callable if it exists.
    :param name: the name of the airgoodies transform method to resolve
    :return: the callable of the method
    """
    if name == 'print_table_contents':
        return _print_table_contents
    else:
        raise Exception(
            f'airgoodies_transform_method with name <{name}> not found')
