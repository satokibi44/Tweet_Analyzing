from bot.return_abc import return_abcde


def test_return():
    expect = "abcde"
    result = return_abcde()

    assert expect == result
