import json

import requests


class BaseApi:
    def get_token(self):
        request_params = {
            "corpid": "ww8665a2776cad0b34",
            "corpsecret": "nU34z1NPe7W-ps0M11SdLjMN04YWfwjGK6P6ZbQnpiw"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params)
        return r.json()['access_token']

    params = {}

    def send(self, data):
        # pytest test_wework.py::TestWework::test_create
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace("${" + key + "}", value)
        data = json.loads(raw_data)
        return requests.request(**data).json()
