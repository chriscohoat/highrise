import datetime

class Attachment(object):
    
    def __init__(self,attachment_id=None,url=None,name=None,size=None):
        self.attachment_id = attachment_id
        self.url = url
        self.name = name
        self.size = size

class Note(object):
    
    def __init__(self,body=None,subject_name=None,note_id=None,author_id=None,created_at=None):
        self.body = body
        self.subject_name = subject_name
        self.note_id = note_id
        self.author_id = author_id
        self.created_at = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        self.attachments = []

class Email(object):
    
    def __init__(self,email_id=None,author_id=None,body=None,created_at=None,subject=None,subject_name=None,title=None):
        self.email_id = email_id
        self.author_id = author_id
        self.body = body
        self.created_at = datetime.datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
        self.title = title
        self.subject_name = subject_name
        self.attachments = []