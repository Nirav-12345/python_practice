import random
import numpy as np



def s(money,bets,goal):
    win=0
    lose=0
    count=0

    for i in range(bets):
        toss=random.random()
        count +=1
        if toss < .50:
            money -= 1
            lose+=1
        else:

            money += 1
            win+=1


        if money==goal:
            print("You won at",str(count))


        elif money == 0:
            print("You lose")









    print(win)
    print(lose)
    print((win*100)/count)
    print((lose*100)/count)








if __name__=="__main__":
    print(s(10,9,5))














































import random
import numpy as np
































































































