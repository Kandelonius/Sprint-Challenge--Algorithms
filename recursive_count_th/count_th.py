'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word, count = 0):
    count = 0
    # global count
    if len(word) == 0:
        count = 0
        return count
    if len(word) == 1:
        return count
    if word[0] == "t" and word[1] == "h":
        # count += 1
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])

#     print(word[0] and word[1])
word = "abcthxyz"
print(count_th(word))
