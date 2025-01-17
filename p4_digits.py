from ib111 import week_10  # noqa


# Napište čistou funkci, která vrátí množinu všech čísel, kterých
# ciferný součet v desítkové soustavě je právě ‹digit_sum› a zároveň
# jejich počet cifer není větší než ‹max_length› (rozmyslete si, že
# bez tohoto omezení by byla hledaná množina nekonečná).

def calc_sum_digits(number: int) -> int:
    result = 0
    while number > 0:
        result += number % 10
        number //= 10
    return result


def digits_help(index: int, dig_sum: int) -> set[int]:
    num = 0
    result: set[int] = set()

    for _ in range(10 ** index):
        curr_sum = calc_sum_digits(num)
        if curr_sum == dig_sum:
            result.add(num)
        num += 1

    return result


def digits(digit_sum: int, max_length: int) -> set[int]:
    final_result: set[int] = set()
    for i in range(max_length + 1):
        curr_set = digits_help(i, digit_sum)
        for a in curr_set:
            final_result.add(a)

    return final_result


def main() -> None:
    assert digits(0, 1) == {0}
    assert digits(0, 5) == {0}
    assert digits(1, 1) == {1}
    assert digits(1, 2) == {1, 10}
    assert digits(2, 4) == {11, 2, 101, 110, 20, 200,
                            1001, 1010, 1100, 2000}
    assert digits(5, 4) == {5, 14, 41, 23, 32, 113,
                            131, 311, 122, 212, 221,
                            1112, 1121, 1211, 2111,
                            50, 104, 140, 401, 410, 203, 230,
                            302, 320, 1013, 1103, 1130, 1031,
                            1301, 1310, 3011, 3101, 3110, 1022, 1202,
                            1220, 2012, 2102, 2120, 2021, 2201, 2210,
                            500, 5000, 1040, 1400, 4010, 4100, 2030,
                            2300, 3020, 3200, 4001, 3002, 2003,
                            1004}
    assert digits(10, 1) == set()
    assert digits(19, 2) == set()
    assert digits(50, 1) == set()
    assert digits(4, 2) == {4, 22, 13, 31, 40}
    assert digits(4, 5) == {4, 22, 13, 31, 112, 121, 211, 1111,
                            40, 202, 220, 103, 130, 301, 310,
                            1012, 1102, 1120, 1021, 1201, 1210,
                            2011, 2101, 2110, 10111, 11011, 11101,
                            11110, 400, 4000, 2020, 2200, 1030, 1300,
                            3010, 3100, 40000, 20200, 22000, 10300,
                            13000, 30100, 31000, 10120, 11020, 11200,
                            10210, 12010, 12100, 20110, 21010, 21100,
                            1003, 2002, 3001, 10003, 10012,
                            10021, 10030, 10102, 10201,
                            11002, 12001, 20002, 20011, 20020,
                            20101, 21001, 30001, 30010}


if __name__ == '__main__':
    main()
