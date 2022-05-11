def chilWin(t,v):

    try:
        if t < 50 and (v < 120 or v > 3):
            w= 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v**0.18
            return w


    except ValueError as err:
        return err

if __name__=="__main__":
    chilWin(2000,345)
print(chilWin(27,34))



