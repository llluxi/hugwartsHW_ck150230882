# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
from pythoncode.calculator import Calculator


def get_datas():
    with open("./datas/calc.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    return [add_datas, add_ids]


class TestCalc():
    def setup_class(self):
        self.calc = Calculator()
        print("计算开始")

    def teardown_class(self):
        print("计算结束")

    # @pytest.mark.parametrize('a,b,expect', [[1, 1, 2], [100, 1, 101], [0.2, 0.2, 0.4]],
    #                          ids=['int_case', 'bignum_case', 'float_case'])
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',
                             [[1, 1, 1], [1, 0, 0], [1, -1, -1], [-2, -2, 4], [100, 500, 50000], [0.5, 0.5, 0.25]],
                             ids=['整数', '零', '单负数', '双负数', '大数', '浮点'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect
