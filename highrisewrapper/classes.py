class Note(object):
    
    def __init__(self,body=None,subject_name=None,note_id=None,author_id=None,created_at=None):
        self.body = body
        self.subject_name = subject_name
        self.note_id = note_id
        self.author_id = author_id
        self.created_at = created_at
        
    def attach_documents(self):
        pass

class Email(object):
    
    def __init__(self):
        pass