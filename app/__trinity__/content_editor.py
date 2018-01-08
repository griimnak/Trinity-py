

class ContentEditor:
    def __init__(self, requested, file):
        self.path = 'app/' + requested + '/'  
        self.location = self.path + file      

    def read(self):
        try:
            self.html = open(self.location, 'r+')

        except Exception as error:
            print(error)

        return self.html.read()
        
    def write(self, data):
        try:
            f = open(self.location, 'w', newline='')
            f.write(data)
            f.close()
   
        except Exception as error:
            print(error)

