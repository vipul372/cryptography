from find_key_length import kasiskiMethod

# chi square test
def chiSq(data):
    freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4,
            6.7, 7.5, 1.9, 0.095, 6, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074]
    count = []
    score = 0
    for i in range(26):
        count.append(data.count(chr(97+i)))
    for i in range(26):
        score += ((count[i] - freq[i]*len(data)*0.01)**2)/(freq[i]*len(data)*0.01)
    return score

# provides key letter by applying frquency analysis
def get_key_letter(text):
    chi = []
    for shift in range(26):
        tmp = ''
        for i in text:
            if ord(i)-shift < 97:
                i = chr(26 + ord(i) - shift)
            else:
                i = chr(ord(i) - shift)
            tmp += i
        chi.append(chiSq(tmp))
    return chi.index(min(chi))

# decryption of vigenere cipher
def decrypt(cipher, key):
  #repeating the key in cyclic manner until it's length isn't equal to the length of cipher text
  key = list(key)
  if len(cipher) != len(key):
    for i in range(len(cipher)-len(key)):
      key.append(key[i % len(key)])
  key = "" . join(key)
  #decrypting the cipher text
  plain_text = []
  for i in range(len(cipher)):
    p = (ord(cipher[i]) - ord(key[i]) + 26) % 26
    p += ord('A')
    plain_text.append(chr(p))
  return ''.join(plain_text)


def find_key_value(cipher, key_length):
  # Splitting cipher into key_length sized parts
  cipher = cipher.lower()
  cipher_list = list(cipher)
  splitted_cipher = []
  for k in range(key_length):
    partial_cipher = []
    for i in range(0, int(len(cipher_list) / key_length), 6):
        partial_cipher.append(cipher_list[i+k])
    str1 = ''
    str1.join(partial_cipher)
    splitted_cipher.append(partial_cipher)
  # Converting key segments into actual key value
  key_letters = []
  for i in range(key_length):
    key_letters.append(chr(97+get_key_letter(splitted_cipher[i])))
  key = ''.join(key_letters)
  return key

# test
cipher = 'KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST'
key_length = kasiskiMethod(cipher)
key = find_key_value(cipher, key_length=6)
plain_text = decrypt(cipher.lower(), key)
print("Key:::>> ", key.upper())
print("Plain text:::>> ", plain_text)
