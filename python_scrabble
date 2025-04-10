
import math
import random
import string
import os

VOWELS = 'аэиоуөүеы'
CONSONANTS = 'бвгджзклмнпрстфхцчшщёюйя'
HAND_SIZE = 12

SCRABBLE_LETTER_VALUES = {
    'б': 3, 'в': 2, 'г': 3, 'д': 3, 'ж': 5, 'з': 3, 'к': 4, 'л': 2, 'м': 3, 'н': 1, 'п': 3, 'р': 2, 'с': 1,
    'т': 1, 'ф': 8, 'х': 5, 'ц': 5, 'ч': 5, 'ш': 5, 'щ': 8, 'а': 1, 'э': 4, 'и': 1, 'о': 1, 'у': 1, 'ө': 3, 
    'ү': 3, 'я': 3, 'е': 1, 'ё': 1, 'ю': 3, 'й': 3, 'ы': 3
}


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "C:\\Users\\user\\Downloads\\hangman\\words.txt"

def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', encoding='utf-8')

    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
 
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word, n):
    word=word.lower()
    sum=0
    for i in word:
        if i!='*':
            sum+=SCRABBLE_LETTER_VALUES[i]
    ret=sum
    ret*=max(1,(7*len(word)-3*(n-len(word))))
    return ret
def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

def deal_hand(n):

    hand={}
    hand['*']=1
    
    umi_vowels = int(math.ceil(n / 3))

    for i in range(umi_vowels-1):#wildcard egshgiin orond baih tul
    #egshgiin toog negeer hasah
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(umi_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

def update_hand(hand, word):

    word=word.lower()
    new_hand=hand.copy()
    for i in word:
        new_hand[i]=max(new_hand.get(i,0)-1,0)
    return new_hand
def is_valid_word(word, hand, word_list):
    word=word.lower()
    if '*' not in word:
        if word not in word_list:
            return False
        new_hand=hand.copy()
        for i in word:
            if new_hand.get(i,0)-1<0:
                return False
            new_hand[i]=new_hand.get(i,0)-1
        return True
    else:
        new_hand=hand.copy()
        for i in word:
            if new_hand.get(i,0)-1<0:
                return False
            new_hand[i]=new_hand.get(i,0)-1
            
        for j in VOWELS:
            word_copy=word #python string = uildel adilhan khayag ruu handahgui tul ingej bolno 
            word_copy=word_copy.replace('*',j)
            if word_copy in word_list:
                return True
        return False
def calculate_handlen(hand):
    ret=0
    for i in hand.values():
        ret+=i
    return ret

def play_hand(hand, word_list):
    score=0
    finished_by_marks=0
    while calculate_handlen(hand)>0:
        print("\033[34m Current Hand:", end=' ')
        display_hand(hand)
        word=input('\033[31m Enter word, or "!!" to indicate that you are finished: ')
        if word=='!!':
            finished_by_marks=1
            break
        if is_valid_word(word, hand, word_list):
            cur=get_word_score(word, calculate_handlen(hand))
            score+=cur
            print('"',word,'" earned ',cur,' points. Total: ',score,' points')
        else:
            print('\033[31m That is not a valid word. Please choose another word.')
        hand=update_hand(hand, word)
        #print('Current hand:', end=' ')
        #display_hand(hand)
    if finished_by_marks==0:
        print('\033[32m Ran out of letters. Total score: ',score,'\033[33m  points')
    else:
        print('\033[33m Total score: ',score,' points')
    return score
def substitute_hand(hand, letter):
    if letter in VOWELS:
        new_vowels=[]
        for i in VOWELS:
            if i!=letter and (i not in hand.keys()):
                new_vowels.append(i)
        sub=random.choice(new_vowels)
    else:
        new_cons=[]
        for i in CONSONANTS:
            if i!=letter and (i not in hand.keys()):
                new_cons.append(i)
        sub=random.choice(new_cons)
    hand[sub]=hand[letter]
    hand[letter]=0
    return hand
    
def play_game(word_list):
    used_replay=0
    hands=int(input("\033[33m Enter total number of hands: "))
    used_sub=0
    tot=0
    for i in range(hands):
        hand=deal_hand(HAND_SIZE)
        display_hand(hand)
        if used_sub==0:
            use_sub=input("\033[34m Would you like to substitute a letter? ")
            if use_sub=='yes':
                used_sub=1
                letter=input("\033[34m Which letter would you like to replace: ")
                hand=substitute_hand(hand, letter)
                display_hand(hand)
        cur=play_hand(hand,word_list)
        print('\033[33m -----Umi----')
        if used_replay==0:
            replaying=input("\033[34m Would you like to replay the hand? ")
            if replaying=="yes":
                used_replay=1
                hand=deal_hand(HAND_SIZE)
                display_hand(hand)
                cur=play_hand(hand,word_list)
        tot+=cur
    print("\033[32m Total score over all hands:",end=' ')
    print(tot)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
