fi=int(input("¿Cuantas filas tiene la primera matriz? "))
col1=int(input("¿Cuantas columnas tiene la primera matriz? "))
col2=int(input("¿Cuantas columnas tiene la segunda matriz? "))

mat1=[]
for i in range (fi):
    mat1.append([0]*col1)


mat2=[]
for i in range (col1):
    mat2.append([0]*col2)

print ("Para tu Primera matriz: ")
for i in range (fi):
    for j in range (col1):
        mat1[i][j]=float(input("Cual es el numero en la posicion (%d,%d): " % (i,j)))

print ("Para tu Segunda matriz: ")
for i in range (col1):
    for j in range (col2):
        mat2[i][j]=float(input("Cual es el numero en la posicion (%d,%d): " % (i,j)))


matf=[]
for i in range (fi):
    matf.append([0]*col2)


for i in range (fi):
    for j in range (col2):
        for k in range (col1):
            matf[i][j] += mat1[i][k] * mat2[k][j]

for i in range (fi):
    print(matf[i])
