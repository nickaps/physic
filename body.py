import pygame as pg
from vector import Vector

class Body:

        def __init__(self, screen, x, y, charge=0):
                self.screen = screen
                self.position = Vector(x, y)
                self.velocity = Vector.zero()
                self.momentum = Vector.zero()
                self.mass = 1
                self.radius = 1
                self.density = 1
                self.friction = 0.01
                self.elasticity = 0.9
                self.color = (255,255,255)
                self.charge = charge

        def move(self, vec):
                self.position.add(vec)
                
        def movePair(self, x, y):
                self.position.addPair(x, y)

        def setMomentum(self):
                self.momentum = Vector(self.velocity.x * self.mass, self.velocity.y * self.mass)

        def setMass(self, mass):
                self.mass = mass
                self.density = self.mass/self.radius
                self.setMomentum()
                
        def setRadius(self, radius):
                self.radius = radius
                self.density = self.mass/self.radius

        def setColor(self, color):
                self.color = color
        
        def setPos(self, vec):
                self.position.set(vec)

        def accelerate(self, vec):
                self.velocity.add(vec)
                self.setMomentum()
                
        def acceleratePair(self, x, y):
                self.velocity.addPair(x, y)
                self.setMomentum()
        
        def draw(self):
                roundedPos = self.position.round()
                pg.draw.circle(self.screen, self.color, (roundedPos.x, roundedPos.y), self.radius, 0)
                
        def checkCollision(self, other):
                isColliding = False
                distance = Vector.distance(self.position, other.position)
                if distance <= self.radius + other.radius:
                        isColliding = True
                return isColliding

        def collisionCorrection(self, other):
                distance = Vector.distance(self.position, other.position)
                overlap = (self.radius + other.radius) - distance
                direction = Vector(self.position.x - other.position.x, self.position.y - other.position.y).normalized()
                direction.multiplyConstant(overlap)
                self.move(direction)

        def wallCollision(self):
                w,h = pg.display.get_surface().get_size()
                if self.position.x >= w - self.radius:
                        self.position.x = w - self.radius
                        self.velocity.multiplyPair(-1, 1)
                elif self.position.x <= self.radius:
                        self.position.x = self.radius
                        self.velocity.multiplyPair(-1, 1)
                if self.position.y >= h - self.radius:
                        self.position.y = h - self.radius
                        self.velocity.multiplyPair(1, -1)
                elif self.position.y <= self.radius:
                        self.position.y = self.radius
                        self.velocity.multiplyPair(1, -1)

        def step(self):
                self.move(self.velocity)
                self.draw()
