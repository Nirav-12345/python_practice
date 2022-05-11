
def vend(amount):
    total_amount=0
    notes=[2000, 500, 200, 100, 50, 20, 10, 5, 1]
    note_counter=[0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i,j in zip(notes,note_counter):
        if amount >=i:
            j=amount//i
            amount=amount-j * i
            total=i*j
            total_amount=total_amount+total
    return total_amount



print(vend(5432))
