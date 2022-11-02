"""
Return how many times 'perk' appears in the string.
However, we will accept anything for the 3rd letter.
For example, 'peak' would be accepted.
"""


def count_instances(word: str):
    word_length = len(word)
    if word_length < 4:
        return 0

    number_of_instances = 0
    i = 0

    while i < word_length:
        if word[i] == "p":
            if i+1 < word_length and i+3 < word_length and word[i+1] == "e" and word[i+3] == "k":
                number_of_instances += 1
                i += 4
        i += 1

    return number_of_instances


if __name__ == "__main__":
    assert count_instances("weperksddpeak22") == 2
    assert count_instances("pe") == 0
    assert count_instances("pe2k2ipeelp1pekk") == 2
