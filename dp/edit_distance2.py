# Space optimized "edit distance" algorithm

def editDistance(str1,str2):

    m = len(str1)
    n = len(str2)

    table = [ [0 for _ in range(n+1)] for _ in range(2)]

    for i in range(n+1):
        table[0][i] = i

    for i in range(1,m+1):
        for j in range(0,n+1):

            curr = i % 2
            prev = (i-1) % 2

            if j == 0: 
                table[curr][j] = j
            elif str1[i-1] == str2[j-1]:
                table[curr][j] = table[prev][j-1]
            else:
                table[curr][j] = min([table[curr][j-1],table[prev][j],table[prev][j-1]])+1
    
    return table[m%2][n]

if __name__ == "__main__":
    
    str1 = input("Enter first string:\t")
    str2 = input("Enter second string:\t")

    print(editDistance(str1,str2))