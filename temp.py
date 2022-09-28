def word_value(input_word):
      values = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26
      }
      value = 0
      for letter in input_word:
          value += values[letter]
      print(value)

def hight(x):
    word_list = x.split(" ")

    word_values = []
    for w in word_list:
        word_values.append(word_value(w))

    max_value = max(word_values)
    max_index = word_values.index(max_value)

    print(word_list[max_index])

word_value("yaroslav")
hight("yaroslav")

# =============================================================================
# 113
# 113
# yaroslav
# =============================================================================
