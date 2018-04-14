import os

import ujson


class TrinityShell:
    def __init__(self, command):
        self.command = command

        if self.command == '':
            self.respond(
                "You didn't enter a command! Type help to get started")
        else:
            self.query_basic_commands(command)

    def query_basic_commands(self, command):
        if command == 'help':
            self.respond("TOGGLE_HELP")

        elif command == 'clear':
            self.respond("TOGGLE_CLEAR")

        elif command == 'stats':
            self.respond("TOGGLE_STATS")

        elif command == 'exit':
            self.respond(
                "To leave, simply navigate to a new page on the left.")

        elif command == f'ls {command[3:]}' or command == 'ls':
            self.ls(command)

        elif command == f'emu {command[4:]}' or command == 'emu':
            self.emu(command)
        else:
            self.respond(
                "You didn't enter a command! Type help to get started")

    def emu(self, command):
        if command == 'emu':
            self.respond("(Use emu [command])")
        else:
            try:
                cmd = os.popen(command[4:]).read()
                self.respond(cmd)
            except Exception as e:
                self.respond("emu failed " + str(e))

    def ls(self, command):
        if command == 'ls':
            path = 'app'
        else:
            path = 'app/' + str(command[3:])
        try:
            result = [e for e in os.listdir(path) if not e.startswith('.')]
            self.respond_array("TOGGLE_LS", result)
        except Exception as e:
            self.respond("ls failed " + str(e))

    def respond(self, command):
        self.response = ujson.dumps(
            {"response": command}, sort_keys=False, indent=2)

    def respond_array(self, command, data):
        self.response = ujson.dumps(
            {"response": command, "array": data}, sort_keys=False, indent=2)
