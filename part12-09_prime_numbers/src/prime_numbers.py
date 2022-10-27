def prime_numbers():
    num = 2
    while True:
        prime = True
        for i in range(2, num - 1):
            if num % i == 0:
                prime = False         
        if prime:
            yield num
        num += 1
            

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))