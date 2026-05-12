
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def add_lists(l1,l2):
    dummy = Node(0)
    temp = dummy
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1:
            s += l1.data
            l1 = l1.next
        if l2:
            s += l2.data
            l2 = l2.next
        carry = s // 10
        temp.next = Node(s % 10)
        temp = temp.next
    return dummy.next
        

def multiply_digits(head,digit):
    dummy = Node(0)
    temp = dummy
    carry = 0
    while head or carry:
        prod = carry
        if head:
            prod += head.data * digit
            head = head.next
        carry = prod // 10
        temp.next = Node(prod % 10)
        temp = temp.next
    return dummy.next

def add_zeros(head,count):
    for _ in range(count):
        new = Node(0)
        new.next = head
        head = new
    return head

def multiply_lists(head1,head2):
    head1 = reverse(head1)
    head2 = reverse(head2)

    result = None
    ptr2 = head2
    shift = 0
    while ptr2:
        product = multiply_digits(head1,ptr2.data)
        product = add_zeros(product,shift)
        result = add_lists(result,product) if result else product
        shift += 1
        ptr2 = ptr2.next
    return reverse(result)
def print_list(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print()

head1 = Node(9)
head1.next = Node(4)
head1.next.next = Node(6)

head2 = Node(8)
head2.next = Node(4)

res = multiply_lists(head1, head2)
print_list(res)