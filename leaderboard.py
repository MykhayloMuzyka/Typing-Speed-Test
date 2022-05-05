import pickle


class Leader:
    def __init__(self, username, inputted_phrases, symbols_per_second, hearts_left, input_efficiency, score):
        self.username = username
        self.inputted_phrases = inputted_phrases
        self.symbols_per_second = symbols_per_second
        self.hearts_left = hearts_left
        self.input_efficiency = input_efficiency
        self.score = score


if __name__ == '__main__':
    with open('Leaderboards/level1.pickle', 'rb') as f:
        leaderboard = pickle.load(f)

    for key, value in leaderboard.items():
        print(f"{key}: {value.username} {value.score}")
