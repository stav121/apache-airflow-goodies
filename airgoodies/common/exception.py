"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since 0.0.1
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


class FileNotFoundException(Exception):
    """
    Exception to be thrown when the provided file was not found.
    """

    def __init__(self, filename: str):
        super().__init__(f'Could not locate file with name <{filename}>')


class UnsupportedFileFormatException(Exception):
    """
    Exception to be thrown when the provided file format is not supported.
    """

    def __init__(self):
        super().__init__('Unsupported file format')
