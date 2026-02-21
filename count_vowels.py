#This is for count vowels in a string
def count_vowels(s):
    vov=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for ch in s:
        if ch in vov:
            count+=1
    return count
s=input("Enter a string: ")
print("Number of vowels in the string:",count_vowels(s))
#This is for count non-vowels in a string
def count_non_vowels(s):
    vov=['a','e','i','o','u','A','E','I','O','U']
    count=0
    for ch in s:
        if ch not in vov:
            count+=1
    return count
s=input("Enter a string: ")
print("Number of non-vowels in the string:",count_non_vowels(s))
#combine programs
def count_vowels_and_non_vowels(s):
    vov=['a','e','i','o','u','A','E','I','O','U']
    vowel_count=0
    non_vowel_count=0
    for ch in s:
        if ch in vov:
            vowel_count+=1
        else:
            non_vowel_count+=1
    return vowel_count, non_vowel_count
s=input("Enter a string: ")
vowel_count, non_vowel_count = count_vowels_and_non_vowels(s)
print("Number of vowels in the string:",vowel_count)
print("Number of non-vowels in the string:",non_vowel_count)