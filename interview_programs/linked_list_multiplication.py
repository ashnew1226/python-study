class Node:
    def __init__(self, data):
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

def multiply_lists(head1, head2):
    head1 = reverse(head1)
    head2 = reverse(head2)
    num1 = []
    num2 = []
    while head1:
        num1.append(head1.data)
        head1 = head1.next
    while head2:
        num2.append(head2.data)
        head2 = head2.next
    result = [0] * (len(num1) + len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]
    for i in range(len(result)):
        carry = result[i] // 10
        result[i] = result[i] % 10
        if i + 1 < len(result):
            result[i + 1] += carry

    i = len(result) - 1
    while i > 0 and result[i] == 0:
        print("inside while ")
        i -= 1
        print(i)

    ans = ""
    while i >= 0:
        print(i)
        ans += str(result[i])
        i -= 1

    return ans
# First list: 9 -> 4 -> 6
head1 = Node(3)
head1.next = Node(2)
head1.next.next = Node(1)

# Second list: 8 -> 4
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)

print(multiply_lists(head1, head2))