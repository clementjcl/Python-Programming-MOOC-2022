def dict_of_numbers():
    dict_spell = {}
    d = {
        0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
        19 : 'nineteen', 20 : 'twenty',
        30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
        70 : 'seventy', 80 : 'eighty', 90 : 'ninety' 
        }
    
    for key in range(100):
        dict_spell[key] = ""

    for key in dict_spell:
        if key <= 20 or key % 10 == 0:
            dict_spell[key] = d[key]
        elif key < 100:
            dict_spell[key] = f"{d[key // 10 * 10]}-{d[key % 10]}"
    
    #print(dict_spell)
    return dict_spell


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])