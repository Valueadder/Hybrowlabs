
from collections import Counter
# Using sorted method


def Anagram(s1, s2):
    if (sorted(s1) == sorted(s2)):
        return True
    else:
        return False


# Using counter method


def Anagram_Checker(s1, s2):
    if (Counter(s1) == Counter(s2)):
        return True
    else:
        return False


if __name__ == "__main__":
    string1 = input("Enter the first string:\n")
    string2 = input("Enter the second string:\n")
    print(Anagram(string1, string2))
    print(Anagram_Checker(string1, string2))
