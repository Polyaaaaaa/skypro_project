import pytest

from src.decorators import log, my_function

from datetime import datetime


@log(filename="mylog.txt")
def test_my_func_with_file_1time(my_function):
    assert my_function() == True


@log(filename="mylog.txt")
def test_my_func_with_file_2time():
    pass


@log()
def test_my_func_without_file_1time():
    pass


@log
def test_my_func_without_file_2time():
    pass

