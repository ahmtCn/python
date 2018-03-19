def printMatris(matris,sz):
    for i in range(sz):
        print("")
        for j in range(sz):
            print(matris[i][j],end =" ")
            

def transpose(matris,sz):
     for i in range(0,sz):
          for j in range(i+1,sz):
             
            temp = matris[i][j]
            matris[i][j] = matris[j][i]
            matris[j][i] = temp


def determinant(matris,sz):
    sum = 0

    def minDet(matris,sz,ro,co):
        minimatris = []
        for i in range(0,sz):
            for j in range(0,sz):
                if i == ro or j == co:
                    pass
                else:
                    minimatris.append(matris[i][j])
                    
        return minimatris[0] * minimatris[3] - minimatris[1] * minimatris[2]
        
                    

    if sz == 2:
        return matris[0][0] * matris[1][1] - matris[0][1] * matris[1][0]
    else:
        row = int(input("which row do you want to choose"))
        for i in range(size):
            sum += matris[row][i] * (-1)**(row+i) * minDet(matris,sz,row,i)
        return sum
            


print("This program allows you to calculate determinant or transpoze of a matris")
choice = input("which calculate do you want to do ? transpose or determinant")

tf = True
matrix = []

while tf:
    size = int(input("please specify the row and column size? (2 or 3 max)"))
    
    if size == 2 or size == 3:
        tf = False
    else:
        tf = True


    for i in range(size):
        matrix.append([])
        for j in range(size):
            value = int(input("value"))
            (matrix[i]).append(value)

if choice == "determinant":
    printMatris(matrix,size)
    print(determinant(matrix,size))
elif choice == "transpose":
    transpose(matrix,size)
    printMatris(matrix,size)
else:
    print("wrong bro bye")
    exit
    
    

    




