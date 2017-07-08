""" Using bitwise operators to clear, set and flip bits """

import unittest

def set_bit(x, position):
    """ Set the bit at the given position. set means convert 0 -> 1 """
    assert position >= 0
    mask = 1 << position
    return x | mask


def clear_bit(x, position):
    """ Clear the bit at the given position. Set means convert 1 -> 0 """
    assert position >= 0
    mask = 1 << position
    return x & (~mask)


def flip_bit(x, position):
    """ Flip the bit at the given position. Flip means convert 0 -> 1, 1 -> 0 """
    assert position >= 0
    mask = 1 << position
    return x ^ mask


def is_even(x):
    return not (x & 1)


def is_power_of_two(x):
    return not (x & (x-1))


def count_diff_bits(x, y):
    z = x ^ y
    z = bin(z)
    count = 0
    for c in z[2:]:
        if c == '1':
            count += 1
    return count

def count_diff_bits2(x, y):
    z = x ^ y
    count = 0
    while z:
        count += 1
        z = z & (z-1)
    return count


class TestBitwise(unittest.TestCase):    
    """ Test the above bitwise operations """

    def test_set_bit(self):
        """ Tests for set_bit function """
        a = bin(set_bit(0b1010101, 3))
        assert a[2:] == '1011101'

        b = bin(set_bit(0b000, 1))
        assert b[2:] == '10'

        c = bin(set_bit(0b0, 5))
        assert c[2:] == '100000'

        d = bin(set_bit(0b111111111111111111110000000000000000, 23))
        assert d[2:] ==  '111111111111111111110000000000000000'

        e = bin(set_bit(0b101010010101010101001, 13))
        assert e[2:] ==  '101010010101010101001'

        f = bin(set_bit(0b111111111111111110, 0))
        assert f[2:] ==  '111111111111111111'

        g = bin(set_bit(0b011100011, 8))
        assert g[2:] ==  '111100011'

    def test_clear_bit(self):
        """ Tests for clear_bit function """
        a = bin(clear_bit(0b1111001, 0))
        assert a[2:] == '1111000'

        b = bin(clear_bit(0b110110101, 10))
        assert b[2:] == '110110101'

        c = bin(clear_bit(0b10100101111, 1))
        assert c[2:] == '10100101101'

        d = bin(clear_bit(0b11111111111111, 13))
        assert d[2:] ==    '1111111111111'

        e = bin(clear_bit(0b00000000, 100))
        assert e[2:] == '0'

        f = bin(clear_bit(0b101001, 3))
        assert f[2:] == '100001'

    def test_flip_bit(self):
        """ Tests for the flip bit function """
        a = bin(flip_bit(0b0, 5))
        assert a == bin(0b100000)

        b = bin(flip_bit(0b11111111, 0))
        assert b == bin(0b11111110)

        c = bin(flip_bit(0b1010101010, 9))
        assert c == bin(0b10101010)

        d = bin(flip_bit(0b1010101010, 1))
        assert d == bin(0b1010101000)

        e = bin(flip_bit(0b1000111110, 3))
        assert e == bin(0b1000110110)

    def test_is_even(self):
        """ Tests for is_even function """
        assert is_even(0) == True
        assert is_even(1) == False
        assert is_even(2) == True
        assert is_even(10000000) == True
        assert is_even(324345654323) == False
        assert is_even(1001) == False
        assert is_even(999999999999) == False
        assert is_even(987654321) == False
        assert is_even(1234567890) == True

    def test_is_power_of_two(self):
        """ Test for is_power_of_two function """
        assert is_power_of_two(1) == True
        assert is_power_of_two(2) == True
        assert is_power_of_two(4) == True
        assert is_power_of_two(512) == True
        assert is_power_of_two(4096) == True
        assert is_power_of_two(4294967296) == True
        assert is_power_of_two(1024) == True

        assert is_power_of_two(3) == False
        assert is_power_of_two(5) == False
        assert is_power_of_two(20) == False
        assert is_power_of_two(55) == False
        assert is_power_of_two(100) == False
        assert is_power_of_two(100045654345) == False
        assert is_power_of_two(9999999) == False

    def test_count_diff_bits(self):
        """ Tests for count_diff_bits function """
        print(count_diff_bits(0b1111111, 0b1111111))
        assert count_diff_bits(0b1111111, 0b1111111) == 0
        assert count_diff_bits(0b1010101, 0b1010100) == 1
        assert count_diff_bits(0b0000000, 0b1111111) == 7
        assert count_diff_bits(0b111000111, 0b111100001111) == 6
        assert count_diff_bits(0b100110101, 0b101111010) == 5
        assert count_diff_bits(0b1010, 0b1100) == 2
        assert count_diff_bits(0b0000000, 0b000000) == 0
       
    def test_count_diff_bits2(self):
        """ Tests for count_diff_bits function """
        assert count_diff_bits2(0b1111111, 0b1111111) == 0
        assert count_diff_bits2(0b1010101, 0b1010100) == 1
        assert count_diff_bits2(0b0000000, 0b1111111) == 7
        assert count_diff_bits2(0b111000111, 0b111100001111) == 6
        assert count_diff_bits2(0b100110101, 0b101111010) == 5
        assert count_diff_bits2(0b1010, 0b1100) == 2
        assert count_diff_bits2(0b0000000, 0b000000) == 0

if __name__ == '__main__':
    unittest.main()
