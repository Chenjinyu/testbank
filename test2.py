# from config.LogConfig import FileAndConsoleLogConfig
# import test
# logging = FileAndConsoleLogConfig()

# logging.info('starting logging')

# test.test_fun()

# logging.info('end logging')


# test_list = [5, 4, 2, 1]
# print(test_list)
# test_sum = sum(sorted(test_list, reverse=True)[:2])
# print(test_sum)


# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# print(set(nums[0]).intersection(set(nums[1]),set(nums[2])))

from collections import namedtuple, Counter, OrderedDict, UserList
from typing import List
# # Define a named tuple
# Person = namedtuple("Person_test", ["name", "age", "gender"])

# # Create an instance
# person1 = Person(name="Alice", age=30, gender="Female")
# print(person1)


# test = ['red', 'blue', 'red', 'green', 'blue', 'blue']
# print(Counter(test).most_common(2))

# d = OrderedDict.fromkeys('abcde')
# d.move_to_end('a')
# print(d)
# d.move_to_end('e', last=False)
# print(d)

# class MyList(UserList):
#     def __init__(self, initial_list:List=[]):
#         modified_list = list(map(lambda x: str(x) + " Chen", initial_list))
#         super().__init__(modified_list)
#     def append(self, item):
#         print('Append item:', item)
#         super().append(item * 2)
        
# my_list = MyList([1, 2, 3])
# my_list.append(4)
# print(my_list)

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
        
class MyDeQueue():
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.size = 0
        
    
    def is_empty(self):
        return self.size == 0
    
    def append(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.size += 1
        
    def appendleft(self, value):
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            raise IndexError('pop from an empty deque')
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value
        
    def popleft(self):
        if self.is_empty():
            raise IndexError('pop from an empty deque')
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value
    
    def __len__(self):
        return self.size
    
    def __repr__(self) -> str:
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return f'Deque({values})'
    
deque = MyDeQueue()
deque.append(1)
deque.append(2)
deque.appendleft(0)
print(deque)  # Output: Deque([0, 1, 2])
print(deque.pop())  # Output: 2
print(deque)  # Outp

temp = [73,74,75,71,69,72,76,73]
print(2 * [0] * len(temp))
print(max(temp[:2]))