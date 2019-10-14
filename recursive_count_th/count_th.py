'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    def word_looper(word, count=0):

        if len(word) < 2:
            return count
        if word[0] == 't':
            if word[1] == 'h':
                count += 1
        return word_looper(word[1:], count)

    return word_looper(word)
