from random import uniform

def weightedDict(data):
    num = uniform(0, sum(data.values()))
    total = 0
    for k, v in data.items():
        total += v
        if total > num:
            return k

plays = {'block': 5, 'foul': 19, 'turnover': 12, 'shot':60}

playResults = {'block': 0, 'foul': 0, 'turnover': 0, 'shot':0}
for i in range(100):
    playResults[weightedDict(plays)] += 1

print(playResults)