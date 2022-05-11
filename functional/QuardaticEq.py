import cmath

def Quad(a,b,c):
    delta=(b*b)-(4*a*c)
    x1=(-b+cmath.sqrt(delta))/(2*a)
    x2=(-b-cmath.sqrt(delta))/(2*a)
    return x1,x2


if __name__=="__main__":
    Quad(2,1,3)
print(Quad(2,1,3))


