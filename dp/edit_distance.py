# Space optimized "edit distance" algorithm

def editDistance(str1,str2):

    m = len(str1)
    n = len(str2)

    table = [ [0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(0,m+1):
        for j in range(0,n+1):           

            if j == 0: 
                table[i][0] = i
            elif i == 0:
                table[0][j] = j
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = min([table[i][j-1],table[i-1][j],table[i-1][j-1]])+1
    
    return table,table[m][n]

def editInstruction(str1,str2,table):
    m = len(table)
    n = len(table[0])    

    i,j = m-1,n-1

    print(f"To convert {str1} to {str2}")

    while i+j != 0:
        if i != 0 and table[i][j] == table[i-1][j]+1:
            print(f"delete {str1[i-1]}")
            i -= 1
        elif j != 0 and table[i][j] == table[i][j-1] + 1:
            print(f"insert {str2[j-1]}")
            j -= 1
        elif i != 0 and j != 0 and table[i][j] == table[i-1][j-1]+1:
            print(f"change {str1[i-1]} to {str2[j-1]}")
            i -= 1
            j -= 1       
        elif i != 0 and j != 0 and table[i][j] == table[i-1][j-1]:
            i -= 1
            j -= 1
        else:
            print("ERR !!!")   
    
if __name__ == "__main__":
    
    str1 = input("Enter first string:\t")
    str2 = input("Enter second string:\t")

    table,dist = editDistance(str1,str2)

    print(dist)
    editInstruction(str1,str2,table)