from model.Vector import *
import sys

def main():
    while True:
        vectorA = None
        vectorB = None
        vectorAB = None

        while True:
            try:
                vectorAx, vectorAy, vectorAz = input('Enter the x, y, z coordinates of your first vector: ').split()
                vectorA = Vector(int(vectorAx), int(vectorAy), int(vectorAz))
                break
            except:
                print('Insert 3 integers spliting by a space character for your coordinates.')
                continue

        while True:
            try:
                vectorBx, vectorBy, vectorBz = input('Enter the x, y, z coordinates of your second vector: ').split()
                vectorB = Vector(int(vectorBx), int(vectorBy), int(vectorBz))
                break
            except:
                print('Insert 3 integers spliting by a space character for your coordinates.')
                continue
        
        vectorAB = Vector.calculateCrossProduct(vectorA, vectorB)

        print('The cross product between the first and second vector is:', vectorAB.toString())

        yes = {'yes','y', 'ye', ''}
        no = {'no','n'}

        while True:
            choice = input("*** Restart program? [Y/n]: ").lower()

            if choice in yes:
                break
            elif choice in no:
                sys.exit()
            else:
                print("Please respond with 'yes' or 'no'")

        print()
main()

