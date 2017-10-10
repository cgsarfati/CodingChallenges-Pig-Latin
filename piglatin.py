"""Turn a phrase into Pig Latin.

This takes a space-separated phrase and returns it in Pig Latin.

Rules:

1. If the word begins with a consonant (not a, e, i, o, u),
   move the first letter to the end and add 'ay'

2. If the word begins with a vowel, add 'yay' to the end

For example:

    >>> pig_latin('hello awesome programmer')
    'ellohay awesomeyay rogrammerpay'

"""

#On runtime r/t for loop


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    # store vowels in set for O1 runtime search
    vowels = set(['a', 'e', 'i', 'o', 'u'])

    # store translated words
    result = []

    # convert str to lst of words
    phrase = phrase.split(" ")

    for word in phrase:
        # if 1st letter consonant, move 1st letter + ay to end of word
        if word[0] not in vowels:
            result.append(word[1:] + word[0] + "ay")
        # if 1st letter vowel, + yay to end of word
        else:
            result.append(word + "yay")

    # convert back to str
    return ' '.join(result)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. REATGAY OBJAY!\n"
