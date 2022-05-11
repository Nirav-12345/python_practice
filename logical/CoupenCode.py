
import random
def coup():
    x=random.randint(1000,2000)
    y=str(input())
    z=(y+str(x)+y)

    for c in z:
        if c==(x,y):
            print("Alraedy Taken")

        else:
            print(z)


if __name__=="__main__":
    coup()








