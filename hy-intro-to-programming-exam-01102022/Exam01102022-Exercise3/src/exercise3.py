def convert(my_list, my_function):
    result = []
    for number in my_list:
        result.append(my_function(number))
    return result
    
if __name__ == "__main__":
    def to_euro(number):
        return (f"{number} €")
    
    my_list = [2, 3, 4]
    
    euros = convert(my_list, to_euro)
    print(euros)