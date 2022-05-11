def Convert1(tempreatue):


    print("Converting celcuies to Fahranhite")

    farahanite=(tempreatue*9/5)+32
    return farahanite


def Convert2(tempr2):
    print("Converting farahnhite to celcuis")

    Celcuis=(tempr2-32)*5/9

    return Celcuis



print(Convert1(23))
print(Convert2(27))