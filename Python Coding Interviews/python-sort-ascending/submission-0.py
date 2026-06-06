def sort_words(a):
    for c in a :
        if not isinstance(c, str) :
            b = 0
        else :
            a.sort()
            b = a
    return b

def sort_numbers(a):
    for c in a :
        if not isinstance(c, int) :
            b = 0
        else :
            a.sort()
            b = a
    return b

def sort_decimals(a):
    for c in a :
        if not isinstance(c, float) :
            b = 0
        else :
            a.sort()
            b = a
    return b

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))