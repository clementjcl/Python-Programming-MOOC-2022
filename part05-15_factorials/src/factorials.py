def factorials(n: int):
    dictionary = {}
    f = 1
    for i in range(1, n + 1):
        f *= i
        dictionary[i] = f
    return dictionary



if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])