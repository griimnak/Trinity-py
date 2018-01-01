

class HtmlEditor:
    def __init__(self):
        self.path = 'app/views/'        

    def read(self, file):
        self.location = self.path + file
        try:
            self.html = open(self.location, 'r')

        except Exception as error:
            print(error)

        return self.html.read()
        
    def write(self, data):
        try:
            self.html.write(data)

        except Exception as error:
            print(error)

HtmlEditor()