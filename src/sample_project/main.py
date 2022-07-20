from typing import Union


def func(var: Union[str, int]) -> int:
    """
    文字列か数値を受け取る。
    数値はそのまま返し、
    文字列は文字列の長さを返す。

    Args:
        var (Union[str, int]): 文字列か数値を指定する

    Returns:
        int: 文字列の長さか数値が返る
    """
    if isinstance(var, int):
        return var
    return len(var)


length = func("abc")
print(length)
