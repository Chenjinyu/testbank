from typing import List
import math

def reverse_words(arr):
    """
    Reverses the order of words in a character array in-place.
    
    Args:
        arr: List of characters with words separated by spaces
    
    Returns:
        The same array with words in reversed order
    
    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) - in-place modification
    """
    if not arr or len(arr) <= 1:
        return arr
    
    # Step 1: Reverse the entire array
    reverse(arr, 0, len(arr) - 1)
    
    # Step 2: Reverse each individual word
    start = 0
    for i in range(len(arr) + 1):
        # When we hit a space or end of array, reverse the current word
        if i == len(arr) or arr[i] == ' ':
            reverse(arr, start, i - 1)
            start = i + 1  # Move to the start of next word
    
    return arr


def reverse(arr, left, right):
    """
    Helper function to reverse a portion of the array in-place.
    
    Args:
        arr: The array to modify
        left: Starting index
        right: Ending index
    """
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

# debug your code below
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print(reverse_words(arr))
