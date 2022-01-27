# Q2
# node of a linked list, having data and a pointer to the next node
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class contains a node object as the head


class linked_list:
    def __init__(self):
        self.head = None

# function to print the contents of the linked list
# if not empty otherwise print
# the message "Linked list is empty"


def print_linked_list(singly_linked_list):
    if singly_linked_list.head is None:
        print("The linked list is empty.")
        return
    current = singly_linked_list.head
    while current is not None:
        print(current.data, end=" ")
        current = current.next
    print()

# function to insert a node into the linked list
# insertion at the beggining of the linked list


def insert_node(sll, value):
    if(sll.head is None):
        sll.head = node(value)
        return
    new_node = node(value)
    new_node.next = sll.head
    sll.head = new_node


# enter the number of elements in the linked list
# we don't need to enter the number of elements in the linked list
# since we can add or remove elements from the linked list
# unlike the array, however, only for testing purposes, we will
singly_linked_list = linked_list()
noOfElements = None
while noOfElements is None:
    try:
        noOfElements = int(
            input())
    except ValueError:  # if the input is not an integer
        # prompt the user to enter an integer
        print("Invalid input. Please enter an integer.")

# inserting new elements into the linked list
# check for proper input
elements = input().split()
for i in range(noOfElements):
    value = None
    while value is None:
        try:
            value = int(elements[i])
            insert_node(singly_linked_list, value)
        except ValueError:  # if the input is not an integer
            # prompt the user to enter an integer
            print("Invalid input. Please enter an integer.")

# call the function to print the linked list
print_linked_list(singly_linked_list)
