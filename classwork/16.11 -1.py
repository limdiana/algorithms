class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


start_node = ListNode(5, ListNode(3, ListNode(4, ListNode(5))))
ptr = start_node

while ptr != None:
    print(ptr.val)
    ptr = ptr.next
print(f'Ссылка а 1 вершину не изменилась: {start_node.val}')