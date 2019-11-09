
S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}


def IsIt(Sentence,Word):
    n = 0
    Index = 0
    for i in Word:
        t = Sentence[Index:].find(i)
        if t > -1:
            n += 1
            Index += t + 1
    if n == len(Word):
        return n
    return 0

def Challenge(Sentence,SetOfWords):
    n = ""
    for i in SetOfWords:
        if IsIt(Sentence,i) > len(n):
            n = i
    return n

print(Challenge(S,D))
