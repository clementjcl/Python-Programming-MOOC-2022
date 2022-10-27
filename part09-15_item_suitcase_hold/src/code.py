class Item:
    def __init__(self, name: str, weight: float):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight    
        self.__item_list = []
                
    def add_item(self, item: Item):
        if (self.weight() + item.weight()) <= self.__max_weight:
            self.__item_list.append(item)
    
    def print_items(self):
        for item in self.__item_list:
            print(item)
    
    def weight(self):
        act_weight = 0.0
        for item in self.__item_list:
            act_weight += item.weight()
        return int(act_weight)
        
    def heaviest_item(self):
        if len(self.__item_list) == 0:
            return None
        else: 
            heaviest_w = 0.0
            for i in self.__item_list:
                if i.weight() > heaviest_w:
                    heaviest_w = i.weight()
                    heaviest = i
            return heaviest
    
    def __str__(self):
        word = "items"
        if len(self.__item_list) == 1:
            word = "item"
        return f"{len(self.__item_list)} {word} ({int(self.weight())} kg)"


class CargoHold:
    def __init__(self, max_weight: float):
        self.__max_weight = max_weight
        self.__cargo_list = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() <= self.weight_available():
            self.__cargo_list.append(suitcase)
        
    def weight_available(self):
        weight_left = self.__max_weight
        weight_act = 0.0
        for s in self.__cargo_list:
            weight_left -= s.weight()
            weight_act += s.weight()
        return weight_left
    
    def print_items(self):
        for suitcase in self.__cargo_list:
            suitcase.print_items()
        
    def __str__(self):
        word = "suitcases"
        if len(self.__cargo_list) == 1:
            word = "suitcase"
        return f"{len(self.__cargo_list)} {word}, space for {self.weight_available()} kg"


if __name__ == "__main__":    
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()