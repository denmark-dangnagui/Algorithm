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

        return cur

    def add_node(self, index, value):
        new_node = Node(value)
        # index 가 0일때
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev_node = self.get_node(index-1)
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node

    def delete_node(self, index):
        # index-1 번째 칸을 우선 구하면
        if index == 0:
            self.head = self.get_node(index+1)
        else:
            prev_node = self.get_node(index-1)
            index_node = self.get_node(index)

            prev_node.next = index_node.next




linked_list = LinkedList(5)
print(linked_list.head.data)
linked_list.append(12)
linked_list.append(8)
print("---------------------------")
linked_list.print_all_nodes()
print("---------------------------")
get_node = linked_list.get_node(1)

linked_list.add_node(1,6)
linked_list.print_all_nodes()
linked_list.delete_node(1)
print("---------------------------")
linked_list.print_all_nodes()
linked_list.delete_node(0)
print("---------------------------")
linked_list.print_all_nodes()
# [5] -> [3]-> [7]-> [6]

