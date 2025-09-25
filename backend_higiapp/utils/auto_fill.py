from datetime import datetime

class AutoFill:
    """ Esta clase define los campos para actualizar y crear registros capturando el usuario y la fecha. """

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