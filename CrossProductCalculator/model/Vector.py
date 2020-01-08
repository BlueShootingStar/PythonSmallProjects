class Vector:
    def __init__(self, x, y, z):
        self.x = x        
        self.y = y        
        self.z = z
    
    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getZ(self):
        return self.z

    def setZ(self, z):
        self.z = z

    @staticmethod
    def calculateCrossProduct(vectorA, vectorB):
        vectorABx = vectorA.getY()*vectorB.getZ() - vectorB.getY()*vectorA.getZ()
        vectorABy = -(vectorA.getX()*vectorB.getZ() - vectorB.getX()*vectorA.getZ())
        vectorABz = vectorA.getX()*vectorB.getY() - vectorB.getX()*vectorA.getY()

        vectorAB = Vector(vectorABx, vectorABy, vectorABz)

        return vectorAB
    
    def toString(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

        

