"""
Binary search, also known as logarithmic search, is a search algorithm that finds the 
position of a target value within a sorted array.
"""

# ==================== Binary Search ====================

"""
Find the index of value in array using a binary search.
If the index can not be found, return None.
"""
def binary_search(array, value):
    if array == None: return None
    array.sort()
    return binary_search_recursive(array, value, 0, len(array) - 1)

"""
Perform a binary search recursively between the given indices until the 
value is found at an index or there are no more elements to search.
The array argument must be sorted.
"""
def binary_search_recursive(array, value, lower_index, upper_index):
    # Check if the bounding indices have a middle index.
    # If not, return None
    if lower_index > upper_index: return None
    
    # Get the index in the middle of the lower and upper indices.
    # Use the floor function to take the lower of the middle indices
    # when there is 2.
    index = (lower_index + upper_index) // 2
     
    # Update the search indices based on the value of this middle index
    if array[index] == value:
        # Success, return the index
        return index
    elif array[index] > value:
        # The value at this index is too large.
        # Search to the left from [lowerIndex, index - 1]
        return binary_search_recursive(array, value, lower_index, index - 1)
    else:
        # The value at this index is too small.
        # Search to the right from [index + 1, upperIndex]
        return binary_search_recursive(array, value, index + 1, upper_index)

# ==================== Test ====================

def test_binary_search(array, value, expected_index):
    index = binary_search(array, value)
    if index == expected_index:
        print("Success")
    else:
        print(f"Failure, returned {index} but expected {expected_index}")

def test_all():
    # Integers, None, empty, or one
    test_binary_search(None, None, None)
    test_binary_search(None, 0, None)
    test_binary_search([], 0, None)
    test_binary_search([1], 0, None)
    test_binary_search([100], 100, 0)

    # Integers, basic
    test_binary_search([1, 2, 3], 0, None)
    test_binary_search([1, 2, 3], 1, 0)
    test_binary_search([1, 2, 3], 2, 1)
    test_binary_search([1, 2, 3], 3, 2)
    test_binary_search([1, 2, 3], 4, None)

    # Strings, basic
    test_binary_search(["a", "b", "c"], "", None)
    test_binary_search(["a", "b", "c"], "a", 0)
    test_binary_search(["a", "b", "c"], "b", 1)
    test_binary_search(["a", "b", "c"], "c", 2)
    test_binary_search(["a", "b", "c"], "d", None)

    # Integers, basic, unsorted
    test_binary_search([3, 1, 2], 1, 0)
    test_binary_search([3, 1, 2], 2, 1)
    test_binary_search([3, 1, 2], 3, 2)

    # Integers
    test_binary_search([1, 5, 9, 12, 17], 1, 0)
    test_binary_search([1, 5, 9, 12, 17], 5, 1)
    test_binary_search([1, 5, 9, 12, 17], 9, 2)
    test_binary_search([1, 5, 9, 12, 17], 12, 3)
    test_binary_search([1, 5, 9, 12, 17], 17, 4)
    test_binary_search([1, 5, 9, 12, 17], 0, None)
    test_binary_search([1, 5, 9, 12, 17], 2, None)
    test_binary_search([1, 5, 9, 12, 17], 4, None)
    test_binary_search([1, 5, 9, 12, 17], 6, None)
    test_binary_search([1, 5, 9, 12, 17], 8, None)
    test_binary_search([1, 5, 9, 12, 17], 10, None)
    test_binary_search([1, 5, 9, 12, 17], 11, None)
    test_binary_search([1, 5, 9, 12, 17], 13, None)
    test_binary_search([1, 5, 9, 12, 17], 16, None)
    test_binary_search([1, 5, 9, 12, 17], 18, None)

# ==================== Main ====================

if __name__ == "__main__":
    test_all()