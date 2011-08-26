import base64
import urllib2

import elementtree.ElementTree as ET

class Highrise(object):
    
    def __init__(self, baseURL, username, password):
        self.baseURL = baseURL
        if self.baseURL[-1] == '/':
            self.baseURL = self.baseURL[:-1]
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [
            ('Content-Type', 'application/xml'),
            ('Accept', 'application/xml'),
            ('Authorization', 'Basic %s' \
                % base64.encodestring('%s:%s' % (username, password)))]
    
    def _request(self, path, data=None):
        if isinstance(data, ET._ElementInterface):
            data = ET.tostring(data)
        req = urllib2.Request(url=self.baseURL + path, data=data)
        return self.opener.open(req).read()
 