# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
        
    def add(self, person: Person):
        self.people.append(person)
        
    def is_empty(self):
        if len(self.people) > 0:
            return False
        return True
    
    def print_contents(self):
        total_height = 0
        for person in self.people:
            total_height += person.height
        print(f"There are {len(self.people)} persons in the room, and their combined height is {total_height} cm")
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")
            
    def shortest(self):
        if len(self.people) > 0:
            lowest_mesure = self.people[0].height
            for person in self.people:
                if person.height <= lowest_mesure:
                    lowest_mesure = person.height
                    lowest_person = person
            return lowest_person
        else:
            return None
    
    def remove_shortest(self):
        if self.shortest() is not None:
            shortest_person = self.shortest()
            for person in self.people:
                if person.name == shortest_person.name:
                    self.people.remove(person)
                    return shortest_person 
        else:
            return None
        
        
if __name__ == "__main__":
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()