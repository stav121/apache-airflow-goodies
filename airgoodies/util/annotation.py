from typing import Callable
from inspect import Signature
from functools import wraps
from typing import cast
"""
@author: Stavros Grigoriou <unix121@protonmail.com>
@since: 0.0.4
"""


def provide_dag_id(func: Callable) -> Callable:
    """
    Provide the dag_id parsed from the <task_instance> or the <dag> parameter if it has not been provided during the call of the function.

    :param func: the Callable function.
    :return: the Callable with the updated dag_id
    """
    signature = Signature.from_callable(func,
                                        follow_wrapped=True,
                                        globals=None,
                                        locals=None,
                                        eval_str=False)

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        func_args = signature.bind(*args, **kwargs)

        if "dag_id" not in func_args.arguments:
            if "dag" in func_args.arguments:
                func_args.arguments["dag_id"] = func_args.arguments[
                    "dag"].dag_id
            elif "task_instance" in func_args.arguments:
                func_args.arguments["dag_id"] = func_args.arguments[
                    "task_instance"].dag_id
            else:
                raise Exception(
                    'Could not located <dag> or <task_instance> in function parameters'
                )

        return func(*func_args.args, **func_args.kwargs)

    return cast(Callable, wrapper)
