class Task:
    id = 0
    def __init__(self, description: str, programmer: str, workload: int):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.__mark = False
        
    def __str__(self):
        print_mark = "NOT FINISHED"
        if self.__mark:
            print_mark = "FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {print_mark}"
        
    def is_finished(self):
        return self.__mark
    
    def mark_finished(self):
        self.__mark = True
        

class OrderBook():
    def __init__(self):
        self.__orders = []
    
    def add_order(self, description: str, programmer: str, workload: int):
        self.__orders.append(Task(description, programmer, workload))
    
    def all_orders(self):
        return self.__orders
    
    def programmers(self):
        return list(set([order.programmer for order in self.all_orders()]))

    def mark_finished(self, id: int):
        for order in self.all_orders():
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"ID does not exist! Now ID max value is {len(self.all_orders())} your input is {id}")
    
    def finished_orders(self):
        return [order for order in self.all_orders() if order.is_finished()]
    
    def unfinished_orders(self):
        return [order for order in self.all_orders() if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        if programmer not in self.programmers():
            raise ValueError(f"Programmer does not exist!")
        
        finished_orders = [order for order in self.__orders if order.programmer == programmer and order.is_finished()]
        unfinished_orders = [order for order in self.__orders if order.programmer == programmer and not order.is_finished()]
        
        finished_workload = sum(order.workload for order in finished_orders)
        unfinished_workload = sum(order.workload for order in unfinished_orders)

        return (len(finished_orders), len(unfinished_orders), finished_workload, unfinished_workload)


if __name__ == "__main__":
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)
    t.add_order("program mobile app", "Andy", 5)
    t.add_order("program something with pygame", "Andy", 50)
    t.add_order("code better facebook", "Jonas", 5000)
    t.mark_finished(1)
    t.mark_finished(2)
    p = t.status_of_programmer("Andy")
    print(p)
    
