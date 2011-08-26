import base64
import urllib2

import elementtree.ElementTree as ET

class Highrise(object):
    
    def __init__(self, baseURL, api_token):
        self.baseURL = baseURL
        if self.baseURL[-1] == '/':
            self.baseURL = self.baseURL[:-1]
        base64string = base64.encodestring('%s:X' % api_token).replace('\n', '')
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [("Authorization", "Basic %s" % base64string),]
    
    def _request(self, path, data=None):
        if isinstance(data, ET._ElementInterface):
            data = ET.tostring(data)
        url=self.baseURL + path
        req = urllib2.Request(url=url, data=data)
        returned_xml = self.opener.open(req).read()
        return ET.fromstring(returned_xml)
    
    def notes(self, person_id):
        """
        This will return all notes for the specified person.
        """
        path = '/people/%u/notes' % person_id
        return self._request(path).findall('note')
    
    def emails(self, person_id):
        """
        This will return all emails for the specified person.
        """
        path = '/people/%u/emails' % person_id
        return self._request(path).findall('email')
 