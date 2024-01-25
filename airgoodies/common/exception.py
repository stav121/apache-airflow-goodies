"""
@author: Stavros Grigoriou <unix121@protonmail.com>
"""


class ConfigNotFoundException(Exception):
    """
    Exception to be thrown when the provided Airflow variable was not found.

    When thrown, it means that the Airflow Variable with the given name must be set
    in order for the goody to work properly.
    """

    def __init__(self, variable: str):
        super().__init__(f'Airflow Variable with name <{variable}> was not found')


class ValueNotFoundException(Exception):
    """
    Exception to be thrown when the provided value was not located in the goody.
    """

    def __init__(self, property: str):
        super().__init__(f'Could not located property with name <{property}>')
