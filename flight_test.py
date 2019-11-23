import pytest
import flight as r


def test_employee():
    assert r.obj2.employeeno() < 600, 'should be in range'


if __name__ == '__main__':
    test_employee()
