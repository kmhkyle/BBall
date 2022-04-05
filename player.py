from random import randint


postitions = {'PG': {'speed': 95}, 'SF': {'speed': 75}, 'C': {'speed': 55}}


# class player:
#     def __init__(self, position):
#         self.three_pointer = 75
#         self.speed = postitions[position]['speed']
    


# def genPlayer():
#     pass

# chrispaul = player('PG')
# lebron = player('SF')
# embiid = player('C')
# print(chrispaul.speed)
# print(lebron.speed)
# print(embiid.speed)

# class player:
#     def __init__(self, *kwargs):
#             self.__dict__.update(*kwargs)

class player:
    def __init__(self, attribute_ranges):
        self.height = randint(72, 82)
        self.weight = randint(200, 300)
        self.attributes = attribute_ranges
        for k,v in attribute_ranges.items():
            attribute_ranges[k] = self.height * v
        # self.__dict__.update(*attribute_ranges)
        # for 
    
        
            
y = {'speed': 75, '_dank': 6, '_fs': 420}
test = ['speed', 'fast', 'three']
x = player(y)
print(x.attributes['speed'])
# print(x.height, x. weight)
