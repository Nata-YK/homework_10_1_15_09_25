from typing import Union

from src.decorators import log


@log(filename=None)
def dividing(x: Union[int | float], y: Union[int | float]) -> Union[float]:
    return x / y


def test_log(capsys):
    dividing(1, 10)
    captured = capsys.readouterr()
    assert captured.out == "\nName function: dividing Result: 0.1\n"
