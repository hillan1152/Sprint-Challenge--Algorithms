'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# UNDERSTAND:
#   Passes a word in the function that COUNTS number of times "th" pops up
#           case will matter
#   only use recursion NO LOOPS
import math


def count_th(word):
    # Plan
    #   create counter thought for loop, couldn't do it, so just added a digit.

    #   create base case: word needs to be at least 2 letters aka "th"
    if len(word) >= 2:
        #  needs to look at letters in 2's for lowercase "th"
        if word[:2] == "th":
            # if its true return 1 and restart recursion at the next available letter
            return 1 + count_th(word[1:])
        else:
            # if the next two letters != "th", restart recursion at the next available letter
            return count_th(word[1:])
    else:
        # if the length of the remaining letters goes below 2, return 0 and end recursion.
        return 0


# def other_count(word, count):
#     if len(word) >= 2:
#         #   needs to look at word in 2's
#         if word[:2] == "th":
#             count += 1
#             return other_count(word[1:], count)
#         else:
#             return other_count(word[1:], count)
#     else:
#         return 0

# other_count(word, count)
# return count


print(count_th("thwethab"))
