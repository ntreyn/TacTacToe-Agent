

class computer_agent():
    def __init__(self, n, m):
        self.name = n
        self.mark = m

    def turn(self, env):
        move = env.sample_action()
        print(self.name + " chose " + str(move))
        return move

    def wins(self):
        print(self.name + " wins!")
