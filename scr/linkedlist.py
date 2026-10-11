Telebe: Feride Mikayilzade
Qrup: KOM25

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def _init_(self):
        self.head = None
    def insert_at_beginning(self, data):
        yeni_element = Node(data)
         yeni_element.next = self.head
        self.head =  yeni_element
    def insert_at_end(self, data):
         yeni_element = Node(data)
        if self.head is None:
            self.head =  yeni_element
            return
        son_element = self.head
        while son_element.next:
             son_element = son_element.next
    son_element.next =  yeni_element
