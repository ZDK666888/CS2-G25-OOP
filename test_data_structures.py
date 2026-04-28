import unittest
# 导入你写的所有数据结构
from Modules.doubly_linked_list import DoublyLinkedList, Node
from Modules.stack import Stack
from Modules.queue import Queue
from Modules.tree import Tree, TreeNode
from Modules.binary_search_tree import BinarySearchTree, BSTNode
from Modules.hash_table import HashTable

#1. DoublyLinkedList
class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_empty_list(self):

        self.assertEqual(self.dll.size, 0)
        self.assertEqual(self.dll.traverse_forward(), "")

    def test_append(self):

        self.dll.append(1)
        self.dll.append(2)
        self.assertEqual(self.dll.size, 2)
        self.assertEqual(self.dll.traverse_forward(), "1 <-> 2")

    def test_prepend(self):

        self.dll.prepend(1)
        self.dll.prepend(2)
        self.assertEqual(self.dll.traverse_forward(), "2 <-> 1")

    def test_remove_head(self):

        self.dll.append(1)
        self.dll.append(2)
        self.dll.remove(1)
        self.assertEqual(self.dll.traverse_forward(), "2")

    def test_remove_tail(self):

        self.dll.append(1)
        self.dll.append(2)
        self.dll.remove(2)
        self.assertEqual(self.dll.traverse_forward(), "1")

    def test_remove_not_exist(self):

        self.dll.append(1)
        self.dll.remove(99)
        self.assertEqual(self.dll.size, 1)


#2. Stack
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):

        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)

    def test_pop_empty(self):

        self.assertEqual(self.stack.pop(), None)

    def test_peek(self):

        self.stack.push(5)
        self.assertEqual(self.stack.peek(), 5)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)

    def test_is_empty_size(self):
        self.assertEqual(self.stack.is_empty(), True)
        self.stack.push(1)
        self.assertEqual(self.stack.is_empty(), False)
        self.assertEqual(self.stack.size(), 1)


#3. Queue
class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue_dequeue(self):

        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.assertEqual(self.queue.dequeue(), "A")
        self.assertEqual(self.queue.dequeue(), "B")

    def test_dequeue_empty(self):

        self.assertEqual(self.queue.dequeue(), None)

    def test_peek(self):
        self.queue.enqueue(100)
        self.assertEqual(self.queue.peek(), 100)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), None)

    def test_is_empty_size(self):
        self.assertEqual(self.queue.is_empty(), True)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)


#4. Tree
class TestTree(unittest.TestCase):
    def test_tree_creation(self):

        tree = Tree("Root")
        self.assertEqual(tree.root.data, "Root")

    def test_add_child_and_traversal(self):

        tree = Tree("Root")
        Tree.add_child(tree.root, "Child1")
        Tree.add_child(tree.root, "Child2")

        result = Tree.level_order(tree.root)
        self.assertEqual(result, "Root -> Child1 -> Child2")


#5. Binary Search Tree
class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_insert_inorder(self):

        values = [5, 3, 7, 2, 4]
        for val in values:
            self.bst.insert(val)

        self.assertEqual(self.bst.inorder(self.bst.root), "2 -> 3 -> 4 -> 5 -> 7")

    def test_empty_bst(self):

        self.assertEqual(self.bst.inorder(self.bst.root), "")


#6. Hash Table
class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_put_get(self):

        self.ht.put("name", "Alice")
        self.ht.put("age", 20)
        self.assertEqual(self.ht.get("name"), "Alice")
        self.assertEqual(self.ht.get("age"), 20)

    def test_update_key(self):

        self.ht.put("id", 1001)
        self.ht.put("id", 1002)
        self.assertEqual(self.ht.get("id"), 1002)

    def test_remove_key(self):

        self.ht.put("test", 123)
        self.ht.remove("test")
        self.assertEqual(self.ht.get("test"), None)

    def test_get_not_exist(self):

        self.assertEqual(self.ht.get("null"), None)

# 运行所有测试
if __name__ == '__main__':
    unittest.main()