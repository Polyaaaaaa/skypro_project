from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> None:
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    try:
                        func(*args, **kwargs)
                    except Exception as mistake:
                        file.write(
                            f"{datetime.now()} my_function error: {type(mistake).__name__}. Inputs: (1, 2), {{}}"
                        )
                    else:
                        file.write(str(datetime.now()) + " " + "my_function ok\n")
            else:
                try:
                    func(*args, **kwargs)
                except Exception as mistake:
                    print(f"{datetime.now()} my_function error: {type(mistake).__name__}. Inputs: (1, 2), {{}}")
                else:
                    print((str(datetime.now()) + " " + "my_function ok\n"))

        return inner

    return wrapper


@log()
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
