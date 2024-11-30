from ib111 import week_10  # noqa


# Napište predikát, který rozhodne, zda lze dané číslo ‹num› napsat
# jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem ‹count› a
# ⟦aᵢ⟧ jsou po dvou různá kladná čísla. Jinými slovy, lze ‹num›
# zapsat jako součet ‹count› druhých mocnin různých kladných čísel?

def find_squares(r_sum: int, r_count: int, i: int) -> bool:
    if r_count == 0:
        return r_sum == 0
    if r_sum < 0:
        return False

    s2 = i * i
    while s2 <= r_sum:
        if find_squares(r_sum - s2, r_count - 1, i + 1):
            return True
        i += 1
        s2 = i * i
    return False


def is_sum_of_squares(num: int, count: int) -> bool:
    return find_squares(num, count, 1)


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
