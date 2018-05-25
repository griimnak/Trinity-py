from datetime import datetime
from sys import version_info

from wsgiref.simple_server import make_server

from app import app
from app.configs.config import config


class TrinityDevServer:
    """ Trinity development server """
    def __init__(self):
        print("[DEV][INFO] Note: Not intended for production use, refer to readme.md for more info.")
        self.show_splash()
        self.load_config()
        self.create_server()

    def show_splash(self):
        _pyver = ".".join(map(str, version_info[:3]))
        _splash = '''
         _______    _       _
        (_______)  (_)     (_)  _
            _  ____ _ ____  _ _| |_ _   _ _____ ____  _   _
           | |/ ___) |  _ \\| (_   _) | | (_____)  _ \\| | | |
           | | |   | | | | | | | |_| |_| |     | |_| | |_| |
           |_|_|   |_|_| |_|_|  \\__)\\__  |     |  __/ \\__  |
                                   (____/      |_|   (____/
        '''

        print('{:^60}'.format(_splash))
        print(f"[DEV][ OK ] Python {_pyver}\n")

    def load_config(self):
        _error = False
        print("[DEV][INFO] Requesting config ..")

        try:
            self.config = config
        except Exception as error:
            _error = True
            print("\n[DEV][ERRO] "+str(error))
            exit()
        if _error != True: print("[DEV][ OK ] Configuration loaded! ")

    def create_server(self):
        _error = False
        _parsed = str(self.config['trinity']['ip'])+\
        ":"+str(self.config['trinity']['port'])
        print(f"\n[DEV][INFO] Binding to {_parsed}..")

        try:
            with make_server(
                self.config['trinity']['ip'],
                self.config['trinity']['port'], app) as httpd:
                if _error != True:
                    _date = datetime.now().strftime('%H:%M%p - %m-%d-%Y')
                    print(f"[DEV][ OK ] READY! ({_parsed}) ({_date})\n")
                httpd.serve_forever()
        except Exception as error:
            _error = True
            print("\n[DEV][ERRO] "+str(error))
            exit()


if __name__ == '__main__':
    TrinityDevServer()
