
def sumtozero(x):

    for i in x:
        for l in x:
            for k in x:
                try:
                    if (i+l+k==0):
                        print(i)

                except ValueError as err:
                    print(err)


if __name=="__main__":

sumtozero([1,2,3,-6])





