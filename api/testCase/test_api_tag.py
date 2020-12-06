from api.testConfig.base_api import BaseApi
from api.testApi.tagDemo import Tag


import requests
class TestWework:
  def test_create_tag(self):
    print(Tag().create_tag("笋岗大学"))

  def test_get(self):
    print(Tag().get_tag_list())

  def test_update_tag(self):
    print(Tag().update_tag("14073753120626177","五年级"))







