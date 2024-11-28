from Commands.command import Command

class History:
    def __init__(self):
        self.history = []

    def log_request(self, request, response):
        self.history.append({"request": request, "response": response})

    def show_history(self):
        for entry in self.history:
            print(f"Request: {entry['request']}")
            print(f"Response: {entry['response']}\n")

class ShowHistoryCommand(Command):
    def __init__(self, user_interface, history):
        self.user_interface = user_interface
        self.history = history

    def execute(self):
        self.user_interface.display_message("=== Історія запитів ===")
        self.history.show_history()
