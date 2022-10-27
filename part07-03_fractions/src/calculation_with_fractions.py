import fractions
def fractionate(amount: int):
    new_list = []
    for i in range(amount):
        new_list.append(fractions.Fraction(1,amount))
    return (new_list)
        
    
    

if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))