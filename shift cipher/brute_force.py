def brute_force():
  best_match = 0
  best_match_text = ''
  for key in range(1, len(letters)+1):
    plain_text = ''
    for symbol in cipher:
      num = (letters.find(symbol)-key) % 26
      plain_text = plain_text + letters[num]
    print('Key #%s: %s' % (key, plain_text))

    detected_words = 0
    word = ''
    for i in range(len(plain_text)):
      word += plain_text[i]
      if word in database:
        detected_words = detected_words + 1
        word = ''

        if detected_words > best_match:
          best_match_text = plain_text
          best_match = detected_words

  print("\nPlain text:", best_match_text)


def dictionary():
    f = open('dictionary.txt')
    words_list = []
    for word in f.read().split('\n'):
        words_list.append(word)
    f.close()
    return(words_list)

cipher = 'uibpmuibqkaivlkwvaqlmzqvoittxwaaqjqtqbqmaeqttjmquxwzbivbqvbpqakwczam'

letters = 'abcdefghijklmnopqrstuvwxyz'

database = dictionary()
brute_force()
 