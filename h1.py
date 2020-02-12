"""
h1.py
MAMIDI SNEHITHA
FEB 11,2020
"""


def my_extend(items, more_items):
    """
    Creates and returns a new list that has elements in items to which the
    the elements in more_items are added.
    items, more_items: lists
    Returns: list

    Example:
    my_exten([1, 2], ['hi']) returns [1, 2, 'hi']
    """
    new_list=items + more_items
    return new_list

def my_reverse(num_list):
    """
    Creates and returns a new list of numbers that has the numbers in num_list
    but in reverse order
    num_list: list of numbers
    Returns: list of numbers

    Example:
    my_reverse([1, 2, 3]) returns [3, 2, 1]

    Implementation requirements
      Do NOT use list method reverse
      Must use the accumulation pattern
    """


def my_translate(word):
    """
    Converts the word using the translation rules below and returns it.
    Translation Rules:
        last character is moved at the beginning of the word and
        'ly'is added to the end.
        If the word is empty, no conversion is applied
        If the word has one character, the translation is that character
        followed by 'ly'
    word: string
    Returns: string

    Example:
    my_translate('hi') returns 'ihly',
    my_translate('bye') returns 'ebyly'
    """
if __name__ == '__main__':
    # Testing my_extend()
    items=[1,2]
    more_items=["hi"]
    new_list=my_extend(items, more_items)
    print(f'my_extend({items},{more_items}) returns {new_list}')
    # Test_case1 for my_extend()
    items=["sneha","is","crazy"]
    more_items=[" "]
    new_list=my_extend(items, more_items)
    print(f'my_extend({items},{more_items}) returns {new_list}')
    # Test_case2 for my_extend()
    items=["orange","tamato"]
    more_items=["potato",5,6,7]
    new_list=my_extend(items, more_items)
    print(f'my_extend({items},{more_items}) returns {new_list}')
