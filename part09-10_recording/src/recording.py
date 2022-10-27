class Recording:
    def __init__(self, length: int):
        if length < 0:
            raise ValueError("Lenght should be more than 0")
        self.__length = length
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, leng):
        if leng < 0:
            raise ValueError("Lenght should be more than 0")
        self.__length = leng
        
if __name__ == "__main__":
    the_wall = Recording(-1)
    print(the_wall.length)
    the_wall.length = 43
    print(the_wall.length)