from string import digits

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


class OrderBookApplication:
    def __init__(self):
        self.__orderbook = OrderBook()
    
    def help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')
    
    def add_order(self):
        description = input('description: ')
        programmer_workload = (input('programmer and workload estimate: ')).split()
        try:
            self.__orderbook.add_order(description, programmer_workload[0], int(programmer_workload[1]))
            print('added!')
        except:
            print('erroneous input')
    
    def finished_tasks(self):
        finished = self.__orderbook.finished_orders() 
        if finished == []:
            print('no finished tasks')
        else:
            for task in finished:
                print(task)
    
    def unfinished_tasks(self):
        unfinished = self.__orderbook.unfinished_orders()
        if unfinished == []:
            print('no unfinished tasks :)')
        else:
            for task in unfinished:
                print(task)
    
    def mark_finished(self):
        try:
            id_num = int(input('id: '))     
            self.__orderbook.mark_finished(id_num)
            print('marked as finished')
        except:
            print('erroneous input')     
            
    def programmers(self):
        for programmer in self.__orderbook.programmers():
            print(programmer)
            
    def status_of_programmer(self):
        try: 
            programmer = self.__orderbook.status_of_programmer(input('programmer: '))
            print(f"tasks: finished {programmer[0]} not finished {programmer[1]}, hours: done {programmer[2]} scheduled {programmer[3]}")
        except:
            print('erroneous input')
        
    def execute(self):
        self.help()
        while True:
            print('')
            command = input("command: ")
            if command == '0':
                break
            elif command == '1':
                self.add_order()
            elif command == '2':
                self.finished_tasks()
            elif command == '3':
                self.unfinished_tasks()
            elif command == '4':
                self.mark_finished()
            elif command == '5':
                self.programmers()
            elif command == '6':
                self.status_of_programmer()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = OrderBookApplication()
application.execute()