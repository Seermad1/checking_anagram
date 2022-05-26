
def find_anagrams(word1, word2):
    # [assignment] Add your code here
    word2 = word2.lower().replace(" ", "")
    word1 = word1.lower().replace(" ", "")

    if sorted(word1) == sorted(word2):
        print("These words are anagrams")
        return True

    else:
        print("These words are not anagrams")
        return False

print(find_anagrams("country", "ytrnuoc"))



