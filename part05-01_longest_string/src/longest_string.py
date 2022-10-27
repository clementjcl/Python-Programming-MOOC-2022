# Write your solution here
def longest(strings: list):
    long = ""
    for i in strings:
        if len(i) > len(long):
            long = i
    return long
    

if __name__ == "__main__":
    strings = ["first", "second", "third"]
    print(longest(strings))