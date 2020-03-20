'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# UNDERSTAND:
#   Passes a word in the function that COUNTS number of times "th" pops up
#           case will matter
#   only use recursion NO LOOPS


def count_th(word):
    # Plan
    #   create counter
    count = 0
    #   create base cases: word needs to be at least 2 letters aka "th"
    if len(word) < 2:
        return count == 0
    else:
        #   needs to look at word in 2's
        if word[:2] == "th":
            count += 1
        #   if "th":
        #       count += 1
        #   return count
        # TBC
        else:
            count_th(1 + word[:2])

    return count


print(count_th("thwethab"))
