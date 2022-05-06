from pickle import dump

for i in range(10):
    with open(f'Leaderboards/level{i+1}.pickle', 'wb') as f:
        dump(dict(), f)
