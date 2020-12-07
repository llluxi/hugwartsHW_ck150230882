import yaml
import pytest
import allure
import os, sys

sys.path.append('E://hugwartsHW')
from api.testApi.tagDemo import Tag


# 获取数据
def get_datas():
    with open('../testData/tag_case_data.yaml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    return [add_datas, add_ids]


@allure.feature("tag_Test_Class")

class TestTag:

    # 创建标签
    @allure.story("tag_create")
    @pytest.mark.parametrize("tagname", get_datas()[0], ids=get_datas()[1])
    def test_create_tag(self, tagname):
        r = Tag().create_tag(tagname)
        print(r)
        assert r["errcode"] == 0

    # 获取标签列表
    @allure.story("tag_get")
    def test_get(self):
        r = Tag().get_tag_list()
        print(r)
        assert r["errcode"] == 0

    # 验证无权限更新
    @allure.story("tag_update")
    def test_update_tag(self):
        r = Tag().update_tag("1", "笋岗中学")
        print(r)
        assert r["errcode"] == 60011

    # 清除自动化数据
    @allure.story("tag_delete")
    @pytest.mark.parametrize("tagid", ['1', '2', '3'])
    def test_delete_tag(self, tagid):
        r = Tag().delete_tag(tagid)
        print(r)
        assert r["errcode"] == 0
