

class human_player:
    def __init__(self, n, m):
        self.name = n
        self.mark = m

    def turn(self, env):
        strmove = input(self.name + ", choose your move: ")
        return int(strmove)

    def wins(self):
        print(self.name + " wins!")