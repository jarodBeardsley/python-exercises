#1. Return counts of letters in a string
def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

#2. Find the sum of the first n positive integers
def sum_ints(n):
    """sum = 0
    for num in range(1, n+1):
        sum += num"""
    return int(n * (n+1)/2)

#3. Replace occurences of first letter in a string except the original
def char_change(str):
    letter = str[0]
    str = str.replace(letter, '$')
    str = letter + str[1:]
    return str

   
#4. Count occurences of a word in a sentence 
"""
Periods? Capital letters? Other punctuation?
"""
def word_count(str):
    word_count = dict()
    words = str.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

#5. Remove duplicates from a list and returns the list
def dedupe(list):
        dupes = set()
        unique_items = []
        for x in list:
            if x not in dupes:
                unique_items.append(x)
                dupes.add(x)
        unique_items.sort()
        return unique_items
        #return sorted(unique_items)


#6. Find second smallest number in a list
def second_smallest(numbers):
    pass

#print(char_frequency("Want to go out sometime?"))
#print(sum_ints(5))
#print(char_change("Let's go out sometime."))
#print(word_count("Don't know about you: I need some ice cream. Some cream with you, cause you're on my mind."))
#print(dedupe([10, 10, 20, 25, 23, 350, 350, 60, 70, 66, 60, 60, 61, 51]))