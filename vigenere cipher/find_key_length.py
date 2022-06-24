from math import sqrt

# cipher = "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUDDKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYCQKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRLSVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMVGKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFSPEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHIFFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"
# cipher = "CHREEVOAHMAERATEDBIAXXWTNXBEEOPHBSBQMQEQERBWRVXUOAKKAOSXXWEAHBWGJMMQMNKGRFVGXWTRZXWIAKLXFPSKBYCARNDCMGTSXNXBTUIADNGMGPSRELXNJELXVRVPRTULHDNUWTWDTYGBPHXTFALJHASVBFXNGLLCHRZBWELEKMSJIKNBHWRJGNMGJSGLXFEYPHAGNRBIEQJTAMRVLCRREMNDGLXRRIMGNSNRWCHRQHAEYEVTAQEBBIPEEWEVKAKOEWADRENXNTBHHCHRTKDNVRZCHRCLQOHPWQAIIWXNRMGWOIIFKEE"
cipher = "DAZFISFSPAVQLSNPXYSZWXALCDAFGQUISMTPHZGAMKTTFTCCFXKFCRGGLPFETZMMMZOZDEADWVZWMWKVGQSOHQSVHPWFKLSLEASEPWHMJEGKPURVSXJXVBWVPOSDETEQTXOBZIKWCXLWNUOVJMJCLLOEOFAZENVMJILOWZEKAZEJAQDILSWWESGUGKTZGQZVRMNWTQSEOTKTKPBSTAMQVERMJEGLJQRTLGFJYGSPTZPGTACMOECBXSESCIYGUFPKVILLTWDKSZODFWFWEAAPQTFSTQIRGMPMELRYELHQSVWBAWMOSDELHMUZGPGYEKZUKWTAMZJMLSEVJQTGLAWVOVVXHKWQILIEUYSZWXAHHUSZOGMUZQCIMVZUVWIFJJHPWVXFSETZEDF"

# returns the position of all repeated substrings
def get_repeated_substring_pos(message):
  substring_pos = {}
  for j in range(2, len(message)//2):
    for i, char in enumerate(message):
      substring = message[i:i+j]
      if substring in substring_pos.keys():
        substring_pos[substring].append(i)
      else:
        substring_pos[substring] = [i]
  repeated_substring = list(filter(lambda k: len(substring_pos[k]) >= 2, substring_pos))
  repeated_substring_pos = [substring_pos[d] for d in repeated_substring]
  return repeated_substring_pos

# returns distance between repeated substrings
def get_distances(repeated_substring_pos):
  distances = [(some_substring[i+1]-some_substring[i]) for some_substring in repeated_substring_pos for i in range(len(some_substring)-1) ]
  return list(filter(lambda d: d > 0, distances))

# returns factors of a given nummber
def get_factors(number):
    factors = set()
    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            factors.add(i)
            factors.add(number//i)
    return sorted(factors)

# candidate key length will be multiple of most frequest factors
def get_candidate_key_lengths(factors):
    factor_list = [factors[lst][fact] for lst in range(len(factors)) for fact in range(len(factors[lst]))]
    candidate_lengths = sorted(set(factor_list), key = lambda f: f>2 and factor_list.count(f), reverse=True)
    return candidate_lengths


def kasiskiMethod(cipher):
  repeated_substring_pos = get_repeated_substring_pos(cipher)
  distances = get_distances(repeated_substring_pos)
  if len(distances) == 0:
    print("Kasiski method failed! - No repeated substrings")
    return -1
  factors = [get_factors(i) for i in distances]
  candidate_key_lengths = get_candidate_key_lengths(factors)
  print(candidate_key_lengths)
  #selecting the best candidate key
  for i in range(len(candidate_key_lengths)):
    for j in range(i):
      if candidate_key_lengths[i] % candidate_key_lengths[j] != 0:
        return candidate_key_lengths[i-1]
  return candidate_key_lengths[0]

keyLength = kasiskiMethod(cipher)
print("Key length:::>> ", keyLength)