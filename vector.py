import numpy as np

class Vector:

        x = 0
        y = 0
        magnitude = 0

        def __init__(self, x, y):
             self.x = x
             self.y = y
             self.setMag()

        def setMag(self):
             self.magnitude = np.sqrt((self.x**2) + (self.y**2))

        def normalized(self):
                normalizedVector = Vector(self.x/self.magnitude, self.y/self.magnitude)
                return normalizedVector

        def set(self, vec):
                self.x = vec.x
                self.y = vec.y
                self.setMag()

        def setPair(self, x, y):
                self.x = x
                self.y = y
                self.setMag()

        def add(self, vec):
                self.x += vec.x
                self.y += vec.y
                self.setMag()

        def addPair(self, x, y):
                self.x += x
                self.y += y
                self.setMag()
                
        def sub(self, vec):
                self.x -= vec.x
                self.y -= vec.y
                self.setMag()
                
        def subPair(self, x, y):
                self.x -= x
                self.y -= x
                self.setMag()

        def multiply(self, vec):
                self.x *= vec.x
                self.y *= vec.y
                self.setMag()
                
        def multiplyConstant(self, c):
                self.x *= c
                self.y *= c
                self.setMag()

        def multiplyPair(self, x, y):
                self.x *= x
                self.y *= y
                self.setMag()

        def divide(self, vec):
                self.x /= vec.x
                self.y /= vec.y
                self.setMag()
                
        def dividePair(self, x, y):
                self.x /= x
                self.y /= y
                self.setMag()

        def round(self):
                newVec = Vector(int(np.round(self.x)), int(np.round(self.y)))
                return newVec

        def dot(self, vec):
                product = (self.x * vec.x) + (self.y * vec.y)
                return product

        @staticmethod
        def addvectors(v1, v2):
                return Vector(v1.x + v2.x, v1.y + v2.y)
        @staticmethod
        def subvectors(v1, v2):
                return Vector(v1.x - v2.x, v1.y - v2.y)
        @staticmethod
        def multiplyvectors(v1, v2):
                return Vector(v1.x * v2.x, v1.y * v2.y)
        @staticmethod
        def multiplyconstant(v1, c):
                return Vector(v1.x * c, v1.y * c)
        @staticmethod
        def dividevectors(v1, v2):
                return Vector(v1.x/v2.x, v1.y/v2.y)
                
        @staticmethod
        def distance(v1, v2):
                d = np.sqrt(((v2.y-v1.y)**2) + ((v2.x-v1.x)**2))
                return d

        @staticmethod
        def zero():
                return Vector(0,0)

        @staticmethod
        def one():
                return Vector(1,1)
