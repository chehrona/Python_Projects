import copy
import random

class Hat:

    def __init__(self, **colorAndNumber):
        self.contents = []
        for entry in colorAndNumber:
            for item in range(0, colorAndNumber[entry]):
                self.contents.append(entry)

    def draw(self, numberToDraw):
        if numberToDraw > len(self.contents):
            return self.contents
        randomDrawnBalls = []
        for draws in range(0, numberToDraw):
            randomBalls = random.choice(self.contents)
            self.contents.remove(randomBalls)
            randomDrawnBalls.append(randomBalls)
        return randomDrawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for experiment in range(0, num_experiments):
        hatCopied = copy.deepcopy(hat)
        randomDraws = hatCopied.draw(num_balls_drawn)
        for key in expected_balls:
            if expected_balls[key] > randomDraws.count(key):
                count -= 1
        count += 1
    return count/num_experiments


hat = Hat(black=6, red=4, green=3)
print(hat.draw(5))
print(experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000))
