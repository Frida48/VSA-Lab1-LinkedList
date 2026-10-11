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
    # Node silmek funksiyasi
    def delete_node(self, key):
        gecici = self.head
   
        if gecici is not None:
            if gecici.data == key:
                self.head = gecici.next
                gecici = None
                return "Silindi"
                
        while gecici is not None:
            if gecici.data == key:
                break
            evvelki_node = gecici
            gecici = gecici.next
            
        if gecici == None:
            return "Element tapilmadi"
            
        evvelki_node.next = gecici.next
        gecici = None
        return "Silindi"

    def search_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False
