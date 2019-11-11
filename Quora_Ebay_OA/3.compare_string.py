# Compare the String with Frequency
# Input: S1 = "babzccc", S2 = "abbzczz" Output: True
# Explaination:
# Count_S1 = {"a":1, "z":1, "b":2, "c":3}
# Count_S2 = {"a":1, "c":1, "b":2, "z":3}

from collections import Counter


def compare_string(S1, S2):
    count1 = Counter(S1)
    count2 = Counter(S2)
    if sorted(list(count1.keys())) != sorted(list(count2.keys())):
        return False
    if sorted(list(count1.values())) != sorted(list(count2.values())):
        return False

    return True


S1 = "babzccc"
S2 = "abbzczz"
print(compare_string(S1, S2))

S1 = "babzcccm"
S2 = "bbazzczl"
print(compare_string(S1, S2))