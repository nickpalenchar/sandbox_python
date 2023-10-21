from computer import Computer

class User:
    def __init__(name: str, computer: Computer):
        self.name = name
        self.computer = computer

    def list_computers(self):
        return self.computer.name
