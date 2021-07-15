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

    def __repr__(self) -> str:
        
        item = self._head
        rep = ""
        if self._head != None:
            while item._next != None:
                rep += repr(item) + "-->"
                item = item._next
        return rep + repr(item)

    def insert(self, item : Item) -> None:
        
        if self._head == None:
            self._head = item
            self._tail = item
        else:
            self._tail._next = item
            self._tail = item
            
    def remove(self, id : int) -> None:
        
        if self._head != None:
            item_to_remove = self._head
            previous = None
            while True:
                if self._head._id == id:
                    self._head = item_to_remove._next
                    del item_to_remove
                    break
                elif item_to_remove._id == id:
                    previous._next = item_to_remove._next
                    if item_to_remove._id == self._tail._id:
                        self._tail = previous
                    del item_to_remove
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

    def test_remove(self):
        
        self._linked_lst.insert(Item(1, 'a'))
        self._linked_lst.insert(Item(2, 'b'))
        self._linked_lst.insert(Item(3, 'c'))
        self._linked_lst.remove(2)
        self.assertEqual(repr(self._linked_lst), '(id : 1, value : a)-->(id : 3, value : c)')
        self._linked_lst.remove(1)
        self.assertEqual(repr(self._linked_lst), '(id : 3, value : c)')
        self._linked_lst.remove(3)
        self.assertEqual(repr(self._linked_lst), None)



if __name__ == '__main__':
    unittest.main()

