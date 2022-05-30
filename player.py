from random import randint, random, randrange, uniform


postitions = {'PG': {'speed': 95}, 'SF': {'speed': 75}, 'C': {'speed': 55}}

tester = 75
class player:
    def __init__(self):
        self.height = randint(72, 84)
        self.weight = randint(200, 300)
        self.threePoint = randint(72, 84)
        self.midRange = randint(72, 84)
        self.shortRange = randint(72, 84)
        self.layup = randint(72, 84)
        self.dunk = randint(72, 84)
        self.freeThrow = randint(72, 84)
        self.passing = randint(72, 84)
        self.offensiveAgg3pt = self.threePoint + randint(-10, 10)
        self.offensiveAggMid = self.midRange + randint(-10, 10)
        self.offensiveAggClose = self.shortRange + randint(-10, 10)
        self.rebound =  randint(72, 84)
        self.dribbling = randint(72, 84)
        self.speed = randint(72, 84)
        self.jumping = randint(72, 84)
        self.manDefense = randint(72, 84)
        self.helpDefense = randint(72, 84)      
    
def genTeam(team):
    for i in range(5):
        x = player()
        team.append(x)
    return team
team1 = []
team2 = []
# team3PT = 0
# teamMidRange = 0
# teamShortRange = 0
# teamDribbling = 0
# teamPasssing = 0
# teamRimOffense = 0
genTeam(team1)
stats = {}
playerShoot3 = {}
playerShootMid = {}
playerShootClose = {}
playerRebound = {}
playerAssist = {}
PID = 0
for p in team1:
    for attr, value in p.__dict__.items():
        if attr not in ['height', 'weight']:
            if attr not in stats:
                stats[attr] = value
            else:
                stats[attr] += value
        if attr == 'offensiveAgg3pt':
            playerShoot3[PID] = value
        elif attr == 'offensiveAggMid':
            playerShootMid[PID] = value
        elif attr == 'offensiveAggClose':
            playerShootClose[PID] = value
        elif attr == 'rebound':
            playerRebound[PID] = value
        elif attr == 'passing':
            playerAssist[PID] = value
    PID += 1

class team:
    def __init__(self):
        self.name = 'dank'
        self.players = []
    def genTeam(self):
        for i in range(5):
            newPLayer = player()
            self.players.append(newPLayer)

tester = team()
tester.genTeam()
print(tester.players)



for k,v in stats.items():
    stats[k] = v/5
# team3PT = stats['threePoint'] + stats['offensiveAgg3pt']
# teamMidRange = stats['midRange'] + stats['offensiveAggMid']
# teamShortRange = ((stats['layup'] + stats['dunk'] + stats['shortRange']) / 3) + stats['offensiveAggClose']
total = stats['offensiveAgg3pt'] + stats['offensiveAggMid'] + stats['offensiveAggClose']
three = stats['offensiveAgg3pt'] / total
mid = stats['offensiveAggMid']  / total
short = stats['offensiveAggClose'] / total

# print(team3PT, teamMidRange, teamShortRange)
# print("{:.2%}".format(three), "{:.2%}".format(mid), "{:.2%}".format(short))
base3, baseMid, baseShort = 37, 30, 33
attempt3 = base3 + (three - .33)
attemptMid = baseMid + (mid - .33)
attemptShort = baseShort + (short - .33)

openThreeModifier = (stats['passing'] * .6) + (stats['dribbling'] * .4)
openShortModifier = (stats['passing'] * .35) + (stats['dribbling'] * .65)

def genDefRatings(team):
    team.defense3 = stats['manDefense'] * .7 + stats['helpDefense'] * .3
    team.defenseMid = stats['manDefense'] * .8 + stats['helpDefense'] * .2
    team.defenseShort = stats['manDefense'] * .4 + stats['helpDefense'] * .6

# print(stats['offensiveAgg3pt'], defense3)
# print(stats['offensiveAggMid'], defenseMid)
# print(stats['offensiveAggClose'], defenseShort)

# print(stats['offensiveAgg3pt'] - defense3)
# print(stats['offensiveAggMid'] - defenseMid)
# print(stats['offensiveAggClose'] - defenseShort)

# threeDefMod = stats['offensiveAgg3pt'] - defense3
# midDefMod = stats['offensiveAggMid'] - defenseMid
# shortDefMod = stats['offensiveAggClose'] - defenseShort

# attempt3 += threeDefMod
# attemptMid += midDefMod
# attemptShort += shortDefMod

# attemptTotal = attempt3 + attemptMid + attemptShort

test = {'Shoot Three': attempt3, 'Shoot Mid Range': attemptMid, 'Shoot Close Range': attemptShort}





def weightedDict(data):
    num = uniform(0, sum(data.values()))
    total = 0
    for k, v in data.items():
        total += v
        if total > num:
            return k


def determineShotType(offense, defense):
    pass


results = {'Shoot Three': 0, 'Shoot Mid Range': 0, 'Shoot Close Range': 0}
for i in range(100):
    x = weightedDict(test)
    results[x] += 1
#     print(x)
#     print(results)
# print(test)
# print(defense3, defenseMid, defenseShort)
winner = weightedDict(playerShootMid)
print(winner)
print(team1[winner].midRange)
# defenseTotal = defense3 + defenseMid + defenseShort
# dThree = defense3 / defenseTotal
# dMid = defenseMid / defenseTotal
# dShort = defenseShort / defenseTotal





