import itertools

fname = "sowpods.txt"
fh = open(fname)

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

bank = raw_input("Enter letter combination: ")
z = bank.lower()
z = z.replace(" ","")
z = z.replace(",","")
foo = []
combo = []
match = []
score = 0
final = []

#Dictionary of words.
for words in fh:
    #strip the /n from each word in text file
    i = words.strip()
    i = i.lower()
    foo.append(i)

#Make a list of every combination of letters for entry.
for L in range(0, len(z) + 1):
    for subset in itertools.permutations(z, L):
        x = list(subset)
        str1 = ''.join(x)
        combo.append(str1)

#Match words with rack of letters. Append to a list named match[].
for each in foo:
    for every in combo:
        if each in every:
            if each not in match:
                match.append(each)
            #print each

#Score each matching word.
for element in match:
    #print element
    score = 0
    for letter in element:
        for k, v in scores.iteritems():
            if letter is k:
                score = score + v
    result = score, element
#    print result
    final.append(result)

final.sort()
final.reverse()
for lines in final:
    print lines