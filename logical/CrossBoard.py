def sum(a,b,c):
    return a+b+c
def PrintBoard(xstate,zstate):




    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    zero = {"X" if xstate[0] else ("O" if zstate[0] else 0)}
    one = {"X" if xstate[1] else ("O" if zstate[1] else 1)}
    two = {"X" if xstate[2] else ("O" if zstate[2] else 2)}
    three = {"X" if xstate[3] else ("O" if zstate[3] else 3)}
    four = {"X" if xstate[4] else ("O" if zstate[4] else 4)}
    five = {"X" if xstate[5] else ("O" if zstate[5] else 5)}
    six = {"X" if xstate[6] else ("O" if zstate[6] else 6)}
    seven = {"X" if xstate[7] else ("O" if zstate[7] else 7)}
    eight = {"X" if xstate[8] else ("O" if zstate[8] else 8)}

    print(f"{zero}| {one} | {two}")
    print(f"{three} | {four} | {five}")
    print(f"{six} | {seven} | {eight}")

    turn=1 # 1 for X and 0 for O

    def CheckWint(xstate,zstate):
        xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[1,4,7],[0,4,8],[2,4,6]]
        for win in xwins:
            if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
                print("X's won the match")
                return 1
            if (sum(zstate[win[0]], zstate[win[1]], zstate[win[2]]) == 3):
                print("O's won the match")
                return 0
        return -1

    while(True):




        if(turn==1):
            print("X's chance")
            vlaue=int(input("Enter the value"))
            xstate[vlaue]=1

        else:
            print("Y's chance")
            vlaue = int(input("Enter the value"))
            zstate[vlaue]=1
            cwin=CheckWint(xstate,zstate)
            if (cwin!=-1):
                print("Match over")
                break
        turn=1-turn


print("Vlues should not be equal to 9")
PrintBoard(9,9)

