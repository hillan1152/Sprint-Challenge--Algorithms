
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# UNDERSTAND
#       Must find instances of lowercase 'th'
#       Go through word 2 letters at a time
#       Case matters
#       only recursion


def count_th(word):
    # keep count of th
    count = 0
    # Base Case, length can no go below 2
    if len(word) < 2:
        return count
    # Does the word even exist?
    if len(word):
        two_letters = word[0:2]
        #   Do the next two letters contain th
        if two_letters == 'th':
            # add one
            count += 1
        # recall count_th and add count
        return count_th(word[1:]) + count


a = [1, 2, 3, 4]
print("Move to next number", a[1:])
print("2 digits? --> ", a[0:2])
