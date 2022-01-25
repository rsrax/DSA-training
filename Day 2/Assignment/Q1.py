class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack_top:
    def __init__(self):
        self.head = None


def push(top, value):
    # push an element to the top of the stack
    new_node = Node(value)
    new_node.next = top.head
    top.head = new_node


def pop(top):
    # pop the top element of the stack
    temp = top.head
    top.head = temp.next
    del temp


def get_max(top):
    # get the maximum element in the stack
    temp_stack = stack_top()
    max_val = None
    temp = top.head
    while temp is not None:
        if max_val is None or temp.data > max_val:
            max_val = temp.data
        push(temp_stack, temp.data)
        pop(top)
        temp = top.head
    while temp_stack.head is not None:
        push(top, temp_stack.head.data)
        pop(temp_stack)
    return max_val


# initialize the stack
stack = stack_top()

no_of_operations = int(input())
for i in range(no_of_operations):
    operation = input().split()
    if int(operation[0]) == 1:
        push(stack, int(operation[1]))
    elif int(operation[0]) == 2:
        pop(stack)
    elif int(operation[0]) == 3:
        print(get_max(stack))
    else:
        print("Invalid operation")
