from physic import Universe
from time import sleep
import random

universe = Universe()
universe.gravity = 0.03

for i in range(10):
        universe.spawn(random.randint(20,480), random.randint(20,480), 6, 2, 0)
        universe.getNewestParticle().setColor([random.randint(10,255),random.randint(10,255),random.randint(10,255)])
        universe.getNewestParticle().acceleratePair(random.randint(-2,2), random.randint(-2,2))

universe.spawn(300,300, 1,10000,0)
universe.getNewestParticle().acceleratePair(22,22)

while universe.running:
        universe.main()
        sleep(0.01)
