def decode_string(s):
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            curr = ""
            while stack and stack[-1] != '[':
                curr = stack.pop() + curr
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(curr * int(num))
    return "".join(stack)

# Test cases
# print(decode_string("3[a]2[bc]"))   # aaabcbc
print(decode_string("3[a2[c]]"))    # accaccacc