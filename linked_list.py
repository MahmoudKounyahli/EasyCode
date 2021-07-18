import unittest

class Item():

    def __init__(self, id, value) -> None:
        
        self._id    = id
        self._value = value
        self._next = None

    def __repr__(self) -> str:
        
        repr = "(id : " + str(self._id) + ", value : " +  str(self._value) + ")"
        return repr

class LinkedList():

    def __init__(self) -> None:
        
        self._head = None
        self._tail = None
        self._lenght = 0

    def __repr__(self) -> str:
        
        if self._lenght == 0:
            return "list is empty"

        item = self._head
        rep = ""
        if self._head != None:
            while item._next != None:
                rep += repr(item) + "-->"
                item = item._next
        return rep + repr(item)

    # insert with O(1)
    def insert(self, item : Item) -> None:
        
        if self._head == None:
            self._head = item
            self._tail = item
        else:
            self._tail._next = item
            self._tail = item
        
        self._lenght += 1
        
    # lenght with O(n) in worst case.
    def lenght(self) -> int:
        if self._head != None:
            crr_item = self._head
            count = 0
            while crr_item != None:
                count += 1
                crr_item = crr_item._next
            return count
        else:
            return 0

    # lenght with O(1)
    def lenght(self) -> int:
        return self._lenght

    def find(self, id : int) -> bool:
        if self._lenght == 0:
            return False
        else:
            crr_item = self._head
            while crr_item != None:
                if crr_item._id == id:
                    return True
                else:
                    crr_item = crr_item._next
            return False

    # remove with O(n) in worst case.
    def remove(self, id : int) -> None:
        
        if self._lenght == 0:
            return
        elif self._lenght == 1 and self._head._id == id:
            item_to_remove = self._head
            self._head = None
            self._tail = None
            del item_to_remove
            self._lenght -= 1
        else:
            item_to_remove = self._head
            previous = None
            while item_to_remove != None: # iteration not yet reached next from last item.
                if item_to_remove._id == id and item_to_remove != self._head:
                    previous._next = item_to_remove._next
                    del item_to_remove
                    self._lenght -= 1
                    break     
                elif self._tail._id == id:
                    self._tail = previous
                    del item_to_remove
                    self._lenght -= 1
                    break
                elif self._head._id == id:
                    self._head = item_to_remove._next
                    del item_to_remove
                    self._lenght -= 1
                    break
                else:
                    previous = item_to_remove
                    item_to_remove = item_to_remove._next
                    

class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self._linked_lst = LinkedList()
 
    def test_insert(self):
        self._linked_lst.insert(Item(1, 'a'))
        self.assertEqual(repr(self._linked_lst), '(id : 1, value : a)')
        self._linked_lst.insert(Item(2, 'b'))
        self.assertEqual(repr(self._linked_lst), '(id : 1, value : a)-->(id : 2, value : b)')
        self._linked_lst.insert(Item(3, 'c'))
        self.assertEqual(repr(self._linked_lst), '(id : 1, value : a)-->(id : 2, value : b)-->(id : 3, value : c)')

    def test_lenght(self):
        self.assertEqual(self._linked_lst.lenght(), 0)
        self._linked_lst.insert(Item(1, 'a'))
        self.assertEqual(self._linked_lst.lenght(), 1)
        self._linked_lst.insert(Item(2, 'b'))
        self.assertEqual(self._linked_lst.lenght(), 2)

    def test_remove(self):  
        self._linked_lst.insert(Item(1, 'a'))
        self._linked_lst.insert(Item(2, 'b'))
        self._linked_lst.insert(Item(3, 'c'))
        self._linked_lst.remove(2)
        self.assertEqual(repr(self._linked_lst), '(id : 1, value : a)-->(id : 3, value : c)')
        self._linked_lst.remove(1)
        self.assertEqual(repr(self._linked_lst), '(id : 3, value : c)')
        self._linked_lst.remove(1)
        self.assertEqual(repr(self._linked_lst), '(id : 3, value : c)')
        self._linked_lst.remove(3)
        self.assertEqual(repr(self._linked_lst), 'list is empty')



if __name__ == '__main__':
    unittest.main()

