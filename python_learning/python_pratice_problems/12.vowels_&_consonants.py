import string
def vowels_consonants_counter(s):
    s = s.lower()
    vowels = 0
    consonants = 0
    others = 0
    for i in s:
        if i.isalpha():
            if i in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        else:
            others += 1
    print(f"Vowels : {vowels}\nConsonants : {consonants}\nOther(space/symobls..etc) : {others}")

s = input("Enter a word or sentence to count vowels, Consonants and other(space/symbols..etc) :")
vowels_consonants_counter(s)

# Example output 1 :
'''
Enter a word or sentence to count vowels, Consonants and other(space/symbols..etc) :Hi raju
Vowels : 3
Consonants : 3
Other(space/symobls..etc) : 1
'''

# Example output 2 :
'''
Enter a word or sentence to count vowels, Consonants and other(space/symbols..etc) :This is to inform you all that, the Hope exams for 3rd and 5th semester students will be from 9th October.
Vowels : 27
Consonants : 54
Other(space/symobls..etc) : 25
'''