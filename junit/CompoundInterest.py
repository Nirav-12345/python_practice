def loan(principal,rate,years):
    p=principal
    r= rate/(12*100)
    n=12*years
    u=p*r
    o=(1-1/((1+r)**n))
    payment=u/o
    return payment

if __name__=="__main__":
    print(loan(100,2,3))