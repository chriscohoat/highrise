import base64
import urllib2

import elementtree.ElementTree as ET
from classes import Note,Email,Attachment

class Highrise(object):
    """
    Provides a Pythonic wrapper for the Highrise API.
    
    Usage:
    
        # Import ElementTree and the Basecamp wrapper module.
        import elementtree.ElementTree as ET
        from highrisewrapper.wrapper import Highrise
    
        # Prepare the interaction with Basecamp.
        hr = Highrise('http://yourBasecamp.projectpath.com/', HIGHRISE_API_TOKEN)
    
        # Get the notes for a person
        notes = hr.notes(personID)
    
        # View the body of each note
        for note in hr.notes(personID):
            print note.find('body').text
    
    """
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
        returned_xml = ""
        try:
            returned_xml = self.opener.open(req,timeout=5).read()
        except:
            pass
        return ET.fromstring(returned_xml)
    
    def add_attachments(self,object,attachments):
        if attachments:
            for attachment in attachments.findall('attachment'):
                attachment_model = Attachment(attachment_id=attachment.find('id').text,
                                              url=attachment.find('url').text,
                                              name=attachment.find('name').text,
                                              size=attachment.find('size').text)
                object.attachments.append(attachment_model)
    
    def notes(self, person_id, get_attachments=False):
        """
        This will return all notes for the specified person.
        """
        path = '/people/%s/notes' % person_id
        notes = []
        for a_note in self._request(path).findall('note'):
            
            note = Note(body=a_note.find('body').text,
                        subject_name=a_note.find('subject-name').text,
                        note_id=a_note.find('id').text,
                        author_id=a_note.find('author-id').text,
                        created_at=a_note.find('created-at').text)
            
            if get_attachments:
                path = '/notes/%s.xml' % note.note_id
                attachments = self._request(path).find('attachments')
                self.add_attachments(note,attachments)
                
            notes.append(note)
            
        return notes
    
    def emails(self, person_id):
        """
        This will return all emails for the specified person.
        """
        path = '/people/%s/emails' % person_id
        emails = []
        for an_email in self._request(path).findall('email'):
            
            email = Email(email_id=an_email.find('id').text,
                          author_id=an_email.find('author-id').text,
                          body=an_email.find('body').text,
                          created_at=an_email.find('created-at').text,
                          title=an_email.find('title').text,
                          subject_name=an_email.find('subject-name').text,
                          )
            
            attachments = an_email.find('attachments')
            self.add_attachments(email,attachments)
            emails.append(email)
            
        return emails
 