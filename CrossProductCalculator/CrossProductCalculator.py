while True:
    vectorAx, vectorAy, vectorAz = input('Enter the x, y, z coordinates of your first vector: ').split()
    try:
        vectorAx = int(vectorAx)
        vectorAy = int(vectorAy)
        vectorAz = int(vectorAz)
    except ValueError:
        print('Insert integers for your coordinates.')
        continue
    while True:
        vectorBx, vectorBy, vectorBz = input('Enter the x, y, z coordinates of your second vector: ').split()
        try:
            vectorBx = int(vectorBx)
            vectorBy = int(vectorBy)
            vectorBz = int(vectorBz)
        except ValueError:
            print('Insert integers for your coordinates.')
            continue
        break
    crossProductABx = vectorAy*vectorBz - vectorBy*vectorAz
    crossProductABy = -(vectorAx*vectorBz - vectorBx*vectorAz)
    crossProductABz = vectorAx*vectorBy - vectorBx*vectorAy
    print('the cross product between the first and second vector is',crossProductABx,crossProductABy,crossProductABz)
    break
