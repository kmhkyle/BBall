
from random import randint, uniform

''' things to do
-generate actual player ratings and heights/weights (positions too)
-generate player turnovers based on passing/dribbling skill/perent of offense run through player
-generate player and team blocks (taller players and good defeenders on average get more)
-generate player fouls (worse/more aggresive/rim protectors get more)
-implement bonus free throw rules
-generate full team (15 players) and generate depth chart
-implement subs
'''



def weightedDict(data):
    num = uniform(0, sum(data.values()))
    total = 0
    for k, v in data.items():
        total += v
        if total > num:
            return k

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
        self.stats = {
            'points': 0,
            'rebounds': 0,
            'assists': 0,
            'turnovers': 0,
            'fouls': 0,
            'blocks':0,
            'field goals attempted': 0,
            'field goals made': 0,
            'free throws attemped': 0,
            'free throws made': 0,
        }

class team:
    def __init__(self):
        self.name = 'dank'
        self.players = []
        self.teamAttr = {}
        self.offShotPrefs = {}
        self.defRatings = {}
        self.playerShoot3 = {}
        self.playerShootMid = {}
        self.playerShootClose = {}
        self.playerRebound = {}
        self.playerAssist = {}
        self.teamFouls = 0
        self.score = 0
        self.stats = {
            'points': 0,
            'rebounds': 0,
            'assists': 0,
            'turnovers': 0,
            'fouls': 0,
            'blocks':0,
            'field goals attempted': 0,
            'field goals made': 0,
            'free throws attemped': 0,
            'free throws made': 0,
        }
        PID = 0
        # gen team
        for i in range(5):
            self.players.append(player())
        # calc team ratings
        for person in self.players:
            for attr, value in person.__dict__.items():
                if attr not in ['height', 'weight', 'stats']:
                    if attr not in self.teamAttr:
                        self.teamAttr[attr] = value
                    else:
                        self.teamAttr[attr] += value
        # calc odds player shoots/reb/ast         
                if attr == 'offensiveAgg3pt':
                    self.playerShoot3[PID] = value
                elif attr == 'offensiveAggMid':
                    self.playerShootMid[PID] = value
                elif attr == 'offensiveAggClose':
                    self.playerShootClose[PID] = value
                elif attr == 'rebound':
                    self.playerRebound[PID] = value
                elif attr == 'passing':
                    self.playerAssist[PID] = value
            PID += 1
        # get average of team ratings (may not be necessary)
        for k, v in self.teamAttr.items():
            self.teamAttr[k] = v / 5
        # calc what type of shot team prefers
        self.offShotPrefs = {
            'offensiveAgg3pt': self.teamAttr['offensiveAgg3pt'], 
            'offensiveAggMid': self.teamAttr['offensiveAggMid'],
            'offensiveAggClose': self.teamAttr['offensiveAggClose']
            }
        # calc team defense by shot
        self.defRatings = {
            'threePointDef': (self.teamAttr['manDefense'] * .7) + (self.teamAttr['helpDefense'] * .3),
            'midRangeDef': (self.teamAttr['manDefense'] * .8) + (self.teamAttr['helpDefense'] * .2),
            'closeRangeDef': (self.teamAttr['manDefense'] * .4) + (self.teamAttr['helpDefense'] * .6),
        }

def genShot(offense, defense):
    # determines type of shot taken, then uses makeOrMissShot to see if it is made, reture true if made
    base3, baseMid, baseClose = 37, 26, 37
    shootThree = base3 + ((offense.offShotPrefs['offensiveAgg3pt'] - defense.defRatings['threePointDef']) / 1.5)
    shootMid = baseMid + ((offense.offShotPrefs['offensiveAggMid'] - defense.defRatings['midRangeDef']) / 1.5)
    shootClose = baseClose + ((offense.offShotPrefs['offensiveAggClose'] - defense.defRatings['closeRangeDef']) / 1.5)
    shotType = {'three': shootThree, 'mid': shootMid, 'close': shootClose}
    shot = weightedDict(shotType)
    # vs code not letting me use switch cases
    # after player and shot type determined, gen shot make or miss/blocked 
    if shot == 'three':
        shootingPlayer = offense.players[weightedDict(offense.playerShoot3)]
    elif shot =='mid':
        shootingPlayer = offense.players[weightedDict(offense.playerShootMid)]
    elif shot == 'close':
        shootingPlayer = offense.players[weightedDict(offense.playerShootClose)]
    return makeOrMissShot(offense, defense, shootingPlayer, shot)

def makeOrMissShot(offense, defense, player, shotType):
    # return true if shot is made, false if not
    # better dribble/pass = higer shot quality, compare that to defense quality to get modifer
    off3ptShotModifer = (offense.teamAttr['passing'] * .65) + (offense.teamAttr['dribbling'] * .35)
    offMidShotModifer = (offense.teamAttr['passing'] * .50) + (offense.teamAttr['dribbling'] * .50)
    offCloseShotModifer = (offense.teamAttr['passing'] * .40) + (offense.teamAttr['dribbling'] * .60)
    player.stats['field goals attempted'] += 1
    offense.stats['field goals attempted'] += 1
    if shotType == 'three':
        defenseModifier = off3ptShotModifer - defense.defRatings['threePointDef']
        shotRating = player.threePoint + defenseModifier
        makeShotChance = shotRating / 2.35
    elif shotType == 'mid':
        defenseModifier = offMidShotModifer - defense.defRatings['midRangeDef']
        shotRating = player.midRange + defenseModifier
        makeShotChance = shotRating / 1.8
    elif shotType == 'close':
        defenseModifier = offCloseShotModifer - defense.defRatings['closeRangeDef']
        shotRating = player.shortRange + defenseModifier
        makeShotChance = shotRating / 1.25
    randomNumber = uniform(0, 100)
    if makeShotChance >= randomNumber:
        player.stats['field goals made'] += 1
        offense.stats['field goals made'] += 1
        if shotType == 'three':
            offense.score += 3
            player.stats['points'] += 3
            offense.stats['points'] += 3
        else:
            offense.score += 2
            player.stats['points'] += 2
            offense.stats['points'] += 2
        return True
    else:
        return False

def shootFT(player, offense, numFT):
    lastMade = False
    for i in range(numFT):
        player.stats['free throws attemped'] += 1
        offense.stats['free throws attemped'] += 1
        randomNumber = uniform(0, 100)
        if player.freeThrow  * .95 > randomNumber:
            offense.score += 1
            player.stats['free throws made'] += 1
            offense.stats['free throws made'] += 1
            player.stats['points'] += 1
            offense.stats['points'] += 1
            lastMade = True
        else:
            lastMade = False
    return lastMade

def genFoulType():
    fouls = {
        'shooting': 50,
        'non - shooting': 50
    }
    return weightedDict(fouls)

def genPossesion(offense, defense):
    shotClock = 30
    # need to do a base like the genShot but for now just simulate
    possesionOdds = {
        'attemptShot': 65,
        'foul': 20,
        'turnover': 15
    }
    # possesion = True
    while True:
        outcome = weightedDict(possesionOdds)
        print('outcome is ', outcome)
        if outcome == 'turnover':
            offense.stats['turnovers'] += 1
            break
        elif outcome == 'foul':
            offense.stats['fouls'] += 1
            defense.teamFouls += 1
            foul = genFoulType()
            print(foul)
            # NEED TO ADD BONUS 1 AND 1 FOR NON SHOOINTG FOULS BETWEEN 7-9
            if foul == 'shooting' or defense.teamFouls > 6:
                print('shooting fould')
                if shootFT(offense.players[weightedDict(offense.playerShootClose)], offense, 2):
                    print('made free throw')
                    break
                else:
                    if offRebound(offense, defense):
                        print('non shooting foul')
                        continue
                    else:
                        print('free throw miss and d rebound')
                        break
            else:
                continue
        elif outcome == 'attemptShot':
            if genShot(offense, defense):
                # work on assist generation
                assistChance = 55 + (offense.teamAttr['passing'] - 78)
                randomNumber = uniform(0, 100)
                if assistChance > randomNumber:
                    offense.stats['assists'] += 1
                    assister = offense.players[weightedDict(offense.playerAssist)]
                    assister.stats['assists'] += 1
                print('made')
                break
            else:
                if offRebound(offense, defense):
                    print('off rebound')
                    continue
                else:
                    print('def rebound')
                    break   

def offRebound(offense, defense):
    baseOffRebound = 26
    randomNumber = uniform(0, 100)
    reboundModifier = offense.teamAttr['rebound'] - defense.teamAttr['rebound']
    offReboundChance = baseOffRebound + reboundModifier
    offRebound = offReboundChance > randomNumber
    if offRebound:
        offense.stats['rebounds'] += 1
        rebounder = offense.players[weightedDict(offense.playerRebound)]
        
    else:
        defense.stats['rebounds'] += 1
        rebounder = defense.players[weightedDict(defense.playerRebound)]
    rebounder.stats['rebounds'] += 1
    return offRebound
    


def game(team1, team2):
    offense, defense = team1, team2
    for i in range(140):
        genPossesion(offense, defense)
        offense, defense = defense, offense
    print(offense.score, defense.score)

team1 = team()
team2 = team()

game(team1, team2)

for p in team1.players:
    print(p.stats)
print(team1.stats)
print(team2.stats)

