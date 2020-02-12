### my_extend()
```
def my_extend(items, more_items):
    """
    Creates and returns a new list that has elements in items to which the
    the elements in more_items are added.
    items, more_items: lists
    Returns: list

    Example:
    my_exten([1, 2], ['hi']) returns [1, 2, 'hi']
    """
```
* Concatenates **more_items** to **items** and assigning it to variable named **new_list**
* Returns **new_list**


### my_reverse()
```
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
```
* length of **num_list** is assigned to a variable name **size**,of type integer
* get the last index of sequence by decreasing size by one because list index starts from zero and assign it to **last_index**
* number of times the loop should be iterated is half of size of sequence. so, variable **its** is assigned as half of size of sequence
* Define and initialize an accumulator called **k**, of type integer that returns range of number of iterations to be performed
* use a for loop with loop variable called **i** to iterate over **k**
    * performing a classic swap
        * value of last_index of num_list is assigned to temporary variable, named **temp**
        * value of num_list of index **i** is stored in last_index of num_list
        * temp is stored in num_list of index i
    * decrement the **last_index** by one
* Returns **num_list**


### my_translate()
```
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
```
* length of word is assigned to a variable named **length**
* use if statement to check word is empty
    * assigning **word** to **translated_word**
* use if statement to check length is greater than zero
    * use if statement to check length of word is equal to one
        * Concatenates string "ly" to **word** and assigned to variable named, **translated_word**
    * use else statement
        * except first and last character, remaining characters are assigned to **newstring**, so that positions of that characters wont be changed
        * Concatenates last character of word, newstring and starting character of word using string slicing and assigned it to **laststring**
        * Concatenates string "ly" to laststring and assigned to **translated_word**
* Returns translated_word
