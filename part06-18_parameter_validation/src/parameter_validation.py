def new_person(name: str, age: int):
    name_words = name.split()
    if len(name) <= 0 or len(name_words) < 2 or len(name) > 40:
        raise ValueError("Please type in a Name with at least two words" + name)
    
    if age < 0 or age > 150:
        raise ValueError("Please, age has to be from 0 to 150:" + str(age) )
    
    return (name, age)


if __name__ == "__main__":
    print(new_person("Jordi ", 34))