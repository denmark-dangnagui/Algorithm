class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
print(node.data, node.next)

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

# LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self,value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next

        cur.next = Node(value)

    def print_all_nodes(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self,index):
        cur = self.head
        cur_index = 0
        while cur_index is not index:
            cur_index += 1
            cur = cur.next

        return cur.data


linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(12)
linked_list.append(8)
print("---------------------------")
linked_list.print_all_nodes()
print("---------------------------")
get_node = linked_list.get_node(1)



# [5] -> [3]-> [7]-> [6]

