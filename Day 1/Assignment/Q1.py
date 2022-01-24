import sys


def reverse_array(arr):
    # reverse the array using slicing
    # copies and returns the copy instead of in-place reversing
    # space complexity: O(n)
    # time complexity: O(n)
    # return arr[::-1]

    # reverse the array using iterator
    # iterates over the elements of the array in reverse order
    # in-built function reversed() returns reverse iterator
    # space complexity: O(1)
    # time complexity: O(n)
    # return [element for element in reversed(arr)]

    # reverse the array using reverse method
    # reverses the array in-place
    # space complexity: O(1)
    # time complexity: O(n)
    arr.reverse()
    return arr


# enter the number of elements in the array
noOfElements = None
while noOfElements is None:
    try:
        noOfElements = int(input())
    except ValueError:  # if the input is not an integer
        # prompt the user to enter an integer
        print("Invalid input. Please enter an integer.")

# empty list/array initialization
arr = []
# enter the elements of the array
elements = input().split()
for i in range(noOfElements):
    value = None
    while value is None:
        try:
            value = int(elements[i])
            arr.append(value)
        except ValueError:
            # prompt the user to enter an integer
            print("Invalid input. Please enter an integer.")
# print the array
print("The array is: ", arr)
# reverse the array
arr = reverse_array(arr)
# print the reversed array
print("The reversed array is: ", arr)
