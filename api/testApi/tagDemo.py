import yaml
from api.testConfig.base_api import BaseApi


class Tag(BaseApi):
    # 获取token
    def __init__(self):
        self.token = BaseApi().get_token()
        self.params["token"] = self.token
        with open("../testData/tag_case.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def get_tag_list(self):
        return self.send(self.data["get"])

    def update_tag(self, tagid, tagname):
        self.params["tagid"] = tagid
        self.params["tagname"] = tagname
        return self.send(self.data["update"])

    def create_tag(self, tagname):
        self.params["tagname"] = tagname
        return self.send(self.data["create"])

    def delete_tag(self, tagid):
        self.params["tagid"] = tagid
        return self.send(self.data["delete"])
