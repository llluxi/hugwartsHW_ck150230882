import requests


class Util:
    def get_token(self):
        request_params = {
            "corpid": "ww8665a2776cad0b34",
            "corpsecret": "nU34z1NPe7W-ps0M11SdLjMN04YWfwjGK6P6ZbQnpiw"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params=request_params)
        return r.json()['access_token']
