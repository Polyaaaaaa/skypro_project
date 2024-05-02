from src.decorators import log


def test_decorator() -> None:
    my_function(1, 2)
    with open("mylog.txt", "r", encoding="utf-8") as file:
        assert len(file.readlines()) > 0


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y
