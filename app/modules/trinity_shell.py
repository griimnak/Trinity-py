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
            self.respond("To leave, simply navigate to a new page on the left.")
        else:
            self.respond("You didn't enter a command! Type help to get started")
    def respond(self, command):
        self.response = ujson.dumps(
            {"response": command}, sort_keys=False, indent=2
        )