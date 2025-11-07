from src.decorators import log


@log(filename=None)
def dividing(x, y):
    return x / y


def test_log(capsys):
    dividing(1, 10)
    captured = capsys.readouterr()
    assert captured.out == ("\nName function: dividing Result: 0.1\n")


#
# def test_log(capsys):
#     dividing(1,0)
#     captured = capsys.readouterr()
#     assert captured.out == ("Name function: sum_num Result: 30Name function: dividing error: division by zero.
#     Inputs: (1, 0), {}\n")


# @log(filename=None)
# def sum_num(*args):
#     for i in args:
#         try:
#             if type(i) == int:
#                 return sum(args)
#         except TypeError:
#             return Exception
#
# def test_log_2():
#     with pytest.raises(Exception, match= "Name function: sum_num error: unsupported operand type(s) for +:
#     'int' and "
#                                          "'str'. Inputs: (1, 2, 5, 6, 7, 8, 0, '1'), {}"):
#         sum_num(1,2,5,6,7,8,0)
