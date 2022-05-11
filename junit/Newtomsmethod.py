def squareroot(num):
    c=num


    count=0
    l=0.00001

    while True:
        root=0.5 * (c+(num/c))
        count+=1

        if abs(root-c)<1:
            break


        c=root
        return root
    
if __name__=="__main__":

    print(squareroot((23)))

