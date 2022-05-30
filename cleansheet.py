
from random import randint, randrange, uniform

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
        PID = 0
        # gen team
        for i in range(5):
            self.players.append(player())
        # calc team ratings
        for person in self.players:
            for attr, value in person.__dict__.items():
                if attr not in ['height', 'weight']:
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
        # print(makeShotChance, randomNumber, 'made')
        return True
    else:
        # print(makeShotChance, randomNumber, 'miss')
        return False
    
    
    # print(off3ptShotModifer)




def genPossesion(offense, defense):
    shotClock = 30
    # need to do a base like the genShot but for now just simulate
    possesionOdds = {
        'attemptShot': 65,
        'foul': 20,
        'turnover': 15
    }
    possesion = True
    while possesion:
        outcome = weightedDict(possesionOdds)
        if outcome == 'turnover':
            possesion = False
        elif outcome == 'foul':
            defense.teamFouls += 1
            possesion = False
        elif outcome == 'attemptShot':
            if genShot(offense, defense):
                possesion = False
            else:
                rebound()

        
        # print(x)
        # if x> 3:
        #     possesion = False
    # print(weightedDict(possesionOdds))
    attemptShot, turnover, foul = 65, 15, 20
    # print(attemptShot + turnover + foul)

# def rebound(offense, defense):
    


team1 = team()
team2 = team()

# makeOrMissShot(team1, team2, team1.players[0], 'three')
# for i in range(20):
#     makeOrMissShot(team1, team2, team1.players[0], 'three')
#     genPossesion(team1,team2)

# genShot(team1, team2)


