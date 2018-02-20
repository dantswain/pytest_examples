'''
A stupid client for devnull-as-a-service.com
'''

import http.client
import urllib.parse

# pylint: disable=too-few-public-methods

class DevNull(object):
    '''
    A stupid client for devnull-as-a-service.com
    '''
    @staticmethod
    def _do_query_post(params):
        conn = http.client.HTTPSConnection("devnull-as-a-service.com")
        conn.request("POST", "/dev/null", params)
        return conn.getresponse()

    def post(self, data):
        '''
        Post `data` to /dev/null
        '''
        params = urllib.parse.urlencode(data)
        response = self._do_query_post(params)
        return response.status
