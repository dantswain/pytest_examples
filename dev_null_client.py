'''
A stupid client for devnull-as-a-service.com
'''

import http.client, urllib.parse

class DevNull(object):
    def _do_query_post(self, params):
        conn = http.client.HTTPSConnection("devnull-as-a-service.com")
        conn.request("POST","/dev/null", params)
        return conn.getresponse()

    def post(self, data):
        params = urllib.parse.urlencode(data)
        response = self._do_query_post(params)
        return response.status
