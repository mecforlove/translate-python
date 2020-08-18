import requests

from .base import BaseProvider
from ..constants import TRANSLATION_FROM_DEFAULT


class YoudaoProvider(BaseProvider):

    name = 'Youdao'
    base_url = 'http://fanyi.youdao.com/openapi.do'
    version = '1.1'
    keyfrom = 'letusgo'

    def _make_request(self, text):
        params = {
            'keyfrom': self.keyfrom,
            'key': self.secret_access_key,
            'type': 'data',
            'doctype': 'json',
            'version': self.version,
            'q': text
        }
        resp = requests.get(self.base_url, params=params)
        return resp.json()
    
    def get_translation(self, text):
        data = self._make_request(text)
        return data['translation'][0]
