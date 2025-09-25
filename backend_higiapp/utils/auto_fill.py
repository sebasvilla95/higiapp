from datetime import datetime

class AutoFill:
    """ This class defines the fields for updating and creating records by capturing the user and timestamp. """

    def __init__(self, request, data):
        self.request = request 
        self.data = data

    def AutoFillPost(self):
        self.data['created_by'] = self.request.user.id
        self.data['created_at'] = datetime.now()
        self.data['updated_by'] = self.request.user.id
        self.data['updated_at'] = datetime.now()
        return self.data
    
    def AutoFillUpdate(self):
        self.data['updated_by'] = self.request.user.id
        self.data['updated_at'] = datetime.now()
        return self.data