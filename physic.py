import pygame as pg
from vector import Vector
from body import Body

class Universe:

        running = True
        bgColor = (0,0,0)

        #gravity = 0.0001
        gravity = 0
        
        def __init__(self):
                self.screen = pg.display.set_mode((800,500))
                self.clock = pg.time.Clock()
                pg.display.flip()
                self.bodies = []

        def getNewestParticle(self):
                return self.bodies[len(self.bodies)-1]
        
        def inverseSquare(self, x):
                n = 1 / (x**2)
                return n
        
        def chargeForce(self):
                for b in self.bodies:
                        averageMovement = Vector.zero()
                        for i in self.bodies:
                                if b is not i:
                                        distance = Vector.distance(b.position, i.position)
                                        direction = Vector.subvectors(i.position, b.position).normalized()
                                        magnitude = self.inverseSquare(distance/4) * -(b.charge * i.charge) * 3
                                        direction.multiplyPair(magnitude, magnitude)
                                        averageMovement.add(direction)
                        averageMovement.dividePair(len(self.bodies), len(self.bodies))
                        b.accelerate(averageMovement)
                        

        def conserveMomentum(self, one, other, normal):

                relativeVelocity = Vector.subvectors(other.velocity, one.velocity)

                e = 1
                j = -(1.0 + e) * Vector.dot(relativeVelocity, normal)
                j /= (1.0 / one.mass) + (1.0 / other.mass)

                other.accelerate(Vector.multiplyconstant(normal, j / other.mass))
                one.accelerate(Vector.multiplyconstant(normal, -j / one.mass))

        def spawn(self, x, y, radius, mass):
                self.bodies.append(Body(self.screen, x, y))
                self.bodies[len(self.bodies)-1].setRadius(radius)
                self.bodies[len(self.bodies)-1].setMass(mass)
                
        def spawn(self, x, y, radius, mass, charge):
                self.bodies.append(Body(self.screen, x, y))
                self.bodies[len(self.bodies)-1].setRadius(radius)
                self.bodies[len(self.bodies)-1].setMass(mass)
                self.bodies[len(self.bodies)-1].charge = charge
        
        def collision(self):
                for b in self.bodies:
                        b.wallCollision()
                        for i in self.bodies:
                                if b is not i:
                                        colliding = b.checkCollision(i)
                                        if colliding:
                                                b.collisionCorrection(i)
                                                self.conserveMomentum(b, i, Vector.subvectors(b.position, i.position).normalized())

        def worldStep(self):
                #clear screen
                self.screen.fill(self.bgColor)

                #main
                for b in self.bodies:
                        b.acceleratePair(0,self.gravity)
                        b.step()

                self.collision()
                self.chargeForce()
                
                #update display
                pg.display.flip()

        def main(self):
                for event in pg.event.get():
                        if event.type == pg.QUIT:
                                self.running = False

                self.worldStep()
                if self.running == False:
                        pg.quit()

