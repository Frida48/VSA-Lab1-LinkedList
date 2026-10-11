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

    def reverse_list(self):
        evvelki = None
        current = self.head
        while current:
            novbeti = current.next
            current.next = evvelki
            evvelki = current
            current = novbeti
        self.head = evvelki

    def print_list(self):
        elementler = []
        current = self.head
        while current:
            elementler.append(str(current.data))
            current = current.next
        print(" -> ".join(elementler) + " -> None")

if __name__ == "__main__":
    my_list = LinkedList()
    
    print("--- 1. Insert testleri ---")
    my_list.insert_at_beginning(10)
    my_list.insert_at_beginning(20)
    my_list.insert_at_end(30)
    my_list.insert_at_end(40)
    my_list.print_list()
    
    print("\n--- 2. Delete testi ---")
    my_list.delete_node(20)
    my_list.print_list()
    
    print("\n--- 3. Search testi ---")
    print("30 var mi?:", my_list.search_node(30))
    print("99 var mi?:", my_list.search_node(99))
    
    print("\n--- 4. Reverse testi ---")
    my_list.reverse_list()
    my_list.print_list()
