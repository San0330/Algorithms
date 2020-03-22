# Recursive method to solve coin change problem

# approach - 1
# start : index from which we use the coins array
# to avoid using the coins that are already used
# i.e. 5 = (2 + 2 + 3) and (3 + 2 + 2) both are counted as one
def cc(coins,amount,start=0):

    # if amount is negative, not possible to take is as ans so return 0
    if amount < 0:
        return 0
    # if amount is 0, we have found a possible combination
    elif amount == 0:
        return 1
    
    # initially cnt = 0 , cnt : no of solutions
    cnt = 0
    for i in range(start,len(coins)):
        # sum each solutions from recursive method
        # use ith coin, so for next iteration amount = amount - ith coin
        cnt += cc(coins,amount-coins[i],i)

    # return this cnt to parent method
    return cnt

# approach - 2
# remove the ith coin in recursive branch so that it is not used again
def cc2(coins,amount,i):

    if amount < 0:
        return 0
    elif amount == 0:
        return 1

    if i is 0:
        return 0
    
    # use the ith coin in one branch
    # remove the ith coin in another branch
    return cc2(coins,amount-coins[i-1],i)  + cc2(coins,amount,i-1)        

if __name__ == "__main__":

    # number of coins
    n = int(input())

    # array of n coins, there are infinite coins of amount n
    coins = [int(x) for x in input().split()]

    # amount for which we count the possible combinations of coins
    amount = int(input())

    ans1  = cc(coins,amount)
    ans2  = cc2(coins,amount,n)

    print(ans1,ans2)

