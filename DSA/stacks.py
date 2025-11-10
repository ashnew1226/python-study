# Stacks in python :
# Stack is the linear data structure that follows the LAST IN FIRST OUT (LIFO)
# statck is the data structure that can hold many elements, and the last element added is the fist one to be removed
# Operations on stack : 
# 1) push : adds a new element on the stack
# 2) pop : Removes and returns the top element from the stack
# 3) peek : Returns the top (last) element on the stack
# 4) isEmpty : Checks if the stack is empty
# 5) size : Finds the number of elements in the stack
# stacks can be implemented using arrays or linked lists

# stack = []
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print(f"stack : {stack}")

# topElement = stack[-1]
# print(f"peek : {topElement}")

# poppedElement = stack.pop()
# print(f"pop : {poppedElement}")
# print(f"stack after pop : {stack}")

# isEmpty = not bool(stack)
# print(f"isEmpty is : {isEmpty}")

# print(f"size : {len(stack)}")

# stacks are memory efficient they do not hold the next elements address like linked list do
# easier to implement and understand
