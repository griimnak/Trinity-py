

class ContentEditor:
    def __init__(self, requested):
        self.path = requested     

    def read(self):
        try:
            self.html = open(self.path, 'r+')

        except Exception as error:
            print(error)

        return self.html.read()
        
    def write(self, data):
        try:
            f = open(self.path, 'w', newline='')
            f.write(data)
            f.close()
   
        except Exception as error:
            print(error)

