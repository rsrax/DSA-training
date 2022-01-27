# Practice question one
# A function that takes in an array of integers
# and returns True if the array is monotonic and False otherwise.
# The array is monotonic if it is either strictly increasing or strictly decreasing.

def is_monotonic(array):
    is_non_decreasing = True  # Assume array is non-decreasing
    is_non_increasing = True  # Assume array is non-increasing
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            is_non_decreasing = False  # If array is non-decreasing, set to False
        if array[i] > array[i-1]:
            is_non_increasing = False  # If array is non-increasing, set to False
    # Return True if array is non-decreasing or non-increasing
    return is_non_decreasing or is_non_increasing
