import random


class Ball:
    def __init__(self):
        self.color_num = 0
        self.position_num = 0
        self.ans_list = []

    def init_random(self):
        _list = []
        for i in range(self.position_num):
            _list.append(random.randint(1, self.color_num))
        self.ans_list = _list
        # print(self.ans_list)

    def check_ans(self, guess):
        positions = 0
        color = 0
        for i in range(len(self.ans_list)):
            if int(guess[i]) == self.ans_list[i]:
                positions += 1

        set_guess = set(list(guess))
        for i in set_guess:
            n = min(guess.count(i), self.ans_list.count(int(i)))
            color += n

        print('*' * positions, end='')
        print('o' * (color - positions), end='')
        print()

        if len(guess) == positions:
            return True
        return False

    def play(self):
        self.color_num = int(input('How many colors? '))
        while self.color_num not in range(1, 9):
            self.color_num = int(input('How many colors? '))

        self.position_num = int(input('How many positions? '))
        while self.position_num not in range(1, 11):
            self.position_num = int(input('How many positions? '))

        print(f'Playing Mastermind with {self.color_num} colors and {self.position_num} positions')

        self.init_random()
        tried = 0
        while True:
            guess = input("input: ")
            if len(guess) != self.position_num:
                continue
            if self.check_ans(guess):
                print(f'You solve it after {tried+1} rounds')
                break
            tried += 1


game = Ball()
game.play()
while True:
    new = input('Start new game?(n/y): ')
    if new == 'n':
        break
    else:
        game.play()
