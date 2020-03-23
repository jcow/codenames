



class Player(dict):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __hash__(self):
        return hash(self.name)
