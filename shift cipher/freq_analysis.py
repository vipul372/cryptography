def decrypt(cipher, shift):
    tmp = ''
    for c in cipher:
        if(ord(c)-shift < 97):
            c = chr(26 + ord(c) - shift)
        else:
            c = chr(ord(c) - shift)
        tmp += c
    print(shift, tmp, end=' ---> ')
    chiSq(tmp, shift)

def chiSq(data, shift):
    expected_freq = [8.2, 1.5, 2.8, 4.3, 13, 2.2, 2, 6.1, 7, 0.15, 0.77, 4, 2.4, 6.7, 7.5, 1.9, 0.095, 6, 6.3, 9.1, 2.8, 0.98, 2.4, 0.15, 2, 0.074 ]
    count = []
    score = 0
    global min_score, key
    for i in range(26):
        count.append(data.count(chr(97+i)))
    for i in range(26):
        score += ((count[i] - expected_freq[i]*len(data)*.01)**2)/(expected_freq[i]*len(data)*.01)
    print(score)
    if score < min_score:
      min_score, key = score, shift
    
min_score = 99999999
key = 0
cipher = 'uibpmuibqkaivlkwvaqlmzqvoittxwaaqjqtqbqmaeqttjmquxwzbivbqvbpqakwczam'

for i in range(1,27):
    decrypt(cipher, i)

print("\nPlain text:")
decrypt(cipher, key)
 