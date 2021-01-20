fish = {
    'Nemo': {
        'type': 'Clownfish',
        'weight': 5,
        'color': 'yellow',
        'stripe color': 'red',
    }
}


def status(name):
    print(fish[name])


def feed(name=None):
    if not name:
        for fishy in fish.values():
            fishy['weight'] += 1
    else:
        if fish[name]['type'] == 'Clownfish' or fish[name]['type'] == 'Tang':
            fish[name]['weight'] += 1
        elif fish[name]['type'] == 'Kong':
            fish[name]['weight'] += 2


def addFish(name, type, weight, color, extra_data=""):
    if type == 'Clownfish':
        fish[name] = {'type': type, 'weight': weight, 'color': color, 'stripe_color': extra_data}
    elif type == 'Tang':
        fish[name] = {'type': type, 'weight': weight, 'color': color, 'short-term memory loss': extra_data}
    elif type == 'Kong':
        fish[name] = {'type': type, 'weight': weight, 'color': color}


def getStatus():
    print(fish)


def removeFish():
    for fishy in fish.values():
        if fishy['weight'] >= 11:
            return fishy


status('Nemo')
feed('Nemo')
status('Nemo')
feed()
status('Nemo')
addFish('Aquaman', 'Kong', 16, 'green')
status('Aquaman')
feed()
status('Aquaman')
feed('Aquaman')
status('Aquaman')
getStatus()
test = removeFish()
del fish[test]
getStatus()
