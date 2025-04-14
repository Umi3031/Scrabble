# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <Umirsyerik>
# Collaborators : <angiin khuukhduudees zubulguu absan>
# Time spent    : <1 doloo honog>
"""
ugen togloom ni Scrabble togloomtoi tustui. Toglogchid uurt baigaa usguudeer neg esbel tuunees olon
ug buteej, buteesen zub ug bolgonooroo onoo abakh ba onoog ugiin urt bolon usgiin toond undeslej ugnu
HAND_SIZE toglogchid hand_size toonii sanamsargui useg olgokh buguud neg useg khed ch baij bolno
*Neg usgiig neg l udaa khereglene
*Neden ch ug buteej bolno
*Zarim useg khereglegdekhgui uldej bolno
*Gart uldsen usgiin khemjee onoond nuluulnu
*Ugiin onoog 2 bureldekhuun khesgiin urjbereej bodogdono
*Ug bolgonii onoonii niilbereer niit onoo bodogdono
*1-r ugend baigaa usguudiin onoonuudiin niilber
*[7*usgiin_urt-3*(n-usgiin_urt)] esbel 1
*Gar gedeg ni toglogch togloomiin turshid gart aguulagdaj baigaa usguudiig khelne
"""
import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "C:\\Users\\user\\Downloads\\hangman\\words.txt"

def load_words():
    """
    Ene funktsiin uureg n file dotorkh  ugsiig unshij, jijug usguudtei
    (lowercase) jagsaalt(list) helbereer butsaakh yum. 
    Yamar neg parametergui asjillana
    File dotor udgiig unshij jagsaalt bolgon butsaana 
    Ug funkts n jijig usguudees burdekh ugsiin jagsaalt butsaana
    WORDLIST_FILNAME khuvsgchid khadgalagdsan nertei fileiig inshikh
    gorimtoi ('r') neene. inFile khuvsagch ni file unshikhad ashiglagdakh file object
    wordlist=[]-- hooson jagsaalt uusgekh. 
    for line in inFile:-- ni fileiin bukh muriig neg negeer unshikh dabtalt (loop) yum.
    wordlist.append(line.strip().lower())-- muriig tseberlekh ba jijig usgeer khurbuulekh
    line.strip() muriin ekhend ba tugsguld baigaa khooson zai, shine muriin
    temdegtiin (\n) khasna. .lower() usgiig jijig usgeer khurbuulne.
    append() Tukhain ugiig wordlist jagsaaltad nemne. 
    print(" ",len(wordlist),"words loaded: ")-- achaalsan ugsiin niit toog kheblekh
    return wordlist-- bukh ugsiig aguulsan wordlist-iig funktsiin garts (return value)
    bolgon butsaana. 
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    ugugdsun mur(string) esbel jagsaalt(list)-iin elementuudiin dabtamjiig
    (frequency) toolj, tedgeeriig aguulsan toli bichig (dictionary) butsaadag
    sequence parammetr n mur(string) esbel jagsaalt(list) baij bolno6 Funkts ni
    tukhain sequence-iin element buriin dabtamjiig(frequency) toolno. 
    sequence-iin elementuudiin dabtamjiig khadgalsan toli bichig butsaana.
    Key ni tukhain sequence dotor baiga uur uur elementuud
    value n tedgeer kheden udaa dabtagdsan bolokhiig ilerkhiilne.
    freq={}-elementiin dabtamjiig khadgalakh khooson toli bichig uusgene.
    for x in sequence: -- sequence-iin bukh elementuudiig neg negeer (x)
    abch dabtana
    freq[x]=freq.get(x, 0)+1
    freq.get(x, 0) ni x element freq toli bichig dotor baigaa esekhiig shalgana.
    khereb baigaa bol tukhain elementiin utgiig abna.
    khereb baikhgui bol 0 gej uzne. Daraan +1 zamaar x-iin toog negeer nemegduulne.
    return freq-- toli bichgiig butsaana
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Scrabble togloomiin ugiin onoog tootsoolokh uuregtei. Ugiin onoo ni 
    khoyor burglees burgene:
    1. Ugiin usguudiin niilber onoonii
    2. Tusgai tootsoolol( undsendee ugiin urt bolon gariin urttain kholbootoigoor nemegdel onoo.)
    word parametr ni Scrabble togloomiin ug. 
    n ni gariin urt buyu toglogchiin gartaa baigaa usgiin too.
    word=word.lower()-- ugiin jijig usgeer khurbuulekh
    sum=0-- ni ugiin usguudiin onoonii niilberiig khadgalakh huvsagch 
    for i in word: if i!='*': sum+=SCRABBLE_LETTER_VALUES[i] -usguudiin onoog tootsoolokh
    for i in word:-- ugiin bukh usguudiig neg negeer shalgaana. 
    if i!='*' - kherbee useg ni '*' bish bol (khereb yamar negen tusgai temgegt baikhgui bol)
    sum+=SCRABBLE_LETTER_VALUES[i]-usgiin onoog SCRABBLE_LETTER_VALUES nertei toli 
    bichgees abch, sum khubsagchid nemne. 
    ret=sum-- ret khubsagchid ugiin ankhnii onoog khadgalna.
    ret*=max(1,(7*len(word)-3*(n-len(word))))--khoyor dakhi burdel-nemegdel onoo
    1-ees baga baij bolokhgui, tiimees 1-ees baga utgatai tokhioldold 1-g ashiglana.
    return ret-- khoyor burdeltei onoonii niilberiig ret khubsagchid khadgalsan buguud ene utgiig butsaana
    """
    word=word.lower()
    sum=0
    for i in word:
        if i!='*':
            sum+=SCRABBLE_LETTER_VALUES[i]
    ret=sum
    ret*=max(1,(7*len(word)-3*(n-len(word))))
    return ret

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Scrabble togloomiin gart baigaa usguudiig delgetsend kharuulakh uuregtei. Gariin
    usguudiig toli bichig(dictionary) khelbereer ugch, usguudiin toog ni toolon
    kharuulakh bolno
    hand parametr ni toli bichig buguud usguud bolon tedgeeriin too khadgalsan baidag
    Ex: {'a':1, 'x':2, 'l':3; 'e':1}
    for letter in hand.key(): -- toli bichiin tulkhuuruudiin dabtakh hand.key() ni
    gariin usguudiin ashiglagddag. Ex: "a", "x", "l", "e" gesen utguudiig aguulna
    for j in range (hand[letter]):-- hand[letter] ni tukhain usgiin toog olj abdag
    ex: "x" usgiin too 2 , tiiimees range(hand[letter]) ni 2 udaa dabtagdana.
    print(letter, end='')--ni usgiig kheblekh buguud shiljuulsen murd (\n) shiljikhgui, kharin '' 
    zaagch khooson oron duriin ashiglan urgeljluulne. Ingesneer bukh usguud ni neg murund 
    kheblegdekh bolno.
    print()-usguudiig kheblesnii daraa, hooson mur heblej, daraagiin contentiin hoorond zain uusgej ugnu
    """ 
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Snamasarguigeer gar(hand) uusgekh. gar burd neg wildcard-tai baina. 
    Ene funkts n niit usegnii 1/3(VOWELS) n egshig useg, uldsen n giguulegch useg baikh gar uusgene. Mun
    garand baigaa usguudiin too ni n baina. Usguudiig toli bichig (dictionary) helbereer khadgaldag buguud 
    usguudiin too ni tus buriin toog ilerkhiilne. hand={}-- garaa hadgalkhiin tuld hooson toli bichig uusgene.
    hand['*']=1--tusgoi temdegt *-iig 1 udaa garaand nemne. 
    umi_vowels=int(math.ceil(n/3))-- VOWELS usguudiin toog tootsoolokh
    math.ceil(n/3) ni n/3-iin khamgiin oirkhon bukhel toog avch baina. 
    for i in range(umi_vowels-1):-- umi_vowels-1 uudaa dabtana. 
    x=random.choice(VOWELS)--VOWELS-iin sanamsargui usgiig songono.
    hand[x]=hand.get(x, 0)+1--tukhain usgiig garaand nemne
    for i in range(umi_vowels, n):-- umi_vowels-ees ekhelj, n-d khurekh khurtel CONSONANTS usguudiig songono.
    x=random.choice(CONSONANTS)-- CONSONANTS-iin sanamsargui usgiig songono. 
    hand[x]=hand.get(x, 0)+1 tukhain duugui usgiin garand usgiig garaand  nemne.
    return hand-- garand baigaa usguudiin too bolon tedgeeriin dabtaltiig khadgalsan toli bichig butsaana.
    """
    
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

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Togloomiin garand baigaa usguudiin tukhain ugeer shinechlekh uuregtei funkts yum.
    Useg buriin too garand baigaa toogoor khayazgarlagdana. Useg ni garand baikhgui bol uurchlult orokhgui. 
    kharin useg garand baidag too n ugt hargalzakh toonoos ikh baibal garand too ni 0 bolj shinechlegdene. 
    hand-- parametr n gar dakhi usguudiig bolon tedgeeriin toog hadgalsan toli bichig
    word-- parametr ni zohioson ug
    word=word.lower()-- ugiin bukh usgiig jijig bolgokh
    new_hand=hand.copy()-- gariig khuulbarlana, ingesneer undsen gariig uurchlukhgui. kharin new_hand dakhi usguudiig 
    shinechlekh bolno. 
    for i in word: -- ugiin bukh usguudiig dabtaj, tus tusad ni garand baikh toog shalgana. 
    new_hand[i]=max(new_hand.get(i, 0)-1,0)-- new.hand.get(i,0) ni tukhain usgiin garand baigaa toog abakh buguud khereb baikhgui bol 
    0 butsaah bolno. usgiin too n garand kh toonoos ikh baibal 0 bolj shinechlegdene.
    max(...,0) ashiglasanaar garandakh usgiin too 0-ees baga bolokhgui
    retrun new_hand shine gar toli bichgiig butsaaj ugnu.
    """
    word=word.lower()
    new_hand=hand.copy()
    for i in word:
        new_hand[i]=max(new_hand.get(i,0)-1,0)
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Ene funkts  ni ugugdsun ug(word), khereglegchiin gar (hand), bolon zubshuurugdsun ugsiin jagsaalt(word_list)-iin
    daguu tukhain ug zub esekhiig shalgakh zoriulalttai. 
    word(shalgakh ug(string))
    hand (kheereglegchiin gar dakhi usguud (dict- tulkhuur ni useg utga ni too))
    word_list (Bolomjit usgiin jagsaalt (list of str) Butsaakh utga-> True (khereg ug zub bol), False (khereb buruu bol))
    word=word.lower()-- ugsiin jijig usgeer khurbuulekh 
    if '*' not in word:-- wildcard baikhgui esekhiig shalgakh
    if word not in word_list: return False-- ug zubshuurugdsun jagsaaltad baigaa esekhiig shalgakh. Bikhgui bol False butsaana.
    new_hand=hand.copy()-- undsen hand-iig uurchlukhgyi tuld khuulbar uusgekh.
    for i in word: -- ugiin useg buriig shalgana
    new_hand.get(i, 0)-1<0-- khereb tukhain useg baikhgui esbel khetersen bol False butsaana.
    new_hand[i]=new_hand.get(i,0)-1-- usgiig hand-aas hasna return True bukh nukhtsuk khangagdbal True butsaana
    else: -wildcard(*) orson tokhioldold bilne
    new_hand=hand.copy() -gariin usguudiin khuulbar uusgekh.
    for i in word: if new_hand.get(i, 0)-1<0: return False
    new_hand[i]=new_hand.get(i,0)-1 jiriin ugiin jagsalttai adilkhan hand dotor baigaa esekhiig shalgana, 
    for j in VOWELS: - wildcard-iih bukh egshgeer orluulj turshikh
    word_copy=word, wprd_copy=word_copy.replace('*',j) word-iig uurchlukhguigeer khuulbarlaj, *-iig egshgeer orluulakh
    word_copy ni word-iin lhubilbar buguud *-iin orond egshug orno
    ig word_copy in word_list: return True khereb word_copy ni ugsiin jagsaaltad baibal True butsaana. 
    return False yamar ch egshgeer oruulaad zub ug bolokhgui bol False butsaakh
    """
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
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """
    hand: tulkhuur ni useg(string), utga ni tukhain usgiin too(int) baikh dictionary
    butsaakh utga: hand dotorkh niit usgiin too
    ret-- niit usgiin toog khadgalakh khuvtsagch
    for i in hand.values():- gariin(hand) usguudiin toon utguud deer dabtalt khiikh
    hand.values() ni dictionary-iin bukh utgiig aguulna. Utga ni int
    ret+=i niit usgiin toog nemekh hand dotorkh bukh utguudiig khoorond ni nemj ret d khadgalna
    """
    ret=0
    for i in hand.values():
        ret+=i
    return ret

def play_hand(hand, word_list):

    """
    Hereglegchid ugugdsun hand-iig ashiglan tohglookh bolomjiig olgodog. Toglogch ug oruulj, onoo tsugluulj, bukh usgee duusgamagts 
    esbel !! gej bichikhed togloom duusdag
    hand-usgiin toog hadgalagch dictionary
    word_list nukh bolomjit usgiig khadgalsan jagsaalt
    butsaakh utga: toglogchiin tsugluulsan niit onoo
    score-onoo hadgalakh finished_by_marks-!! ashiglaj duussan eskhiig khadgalakh khubsagch
    finished_by_marks=: toglogch !! oruulsan bol 1 oruulaagui bol 0 butsaana
    while calculate_handlen(hand)>0:-- useg duusakh hurtel togloltiig urgeljuulene. 
    herbe hand-d uldsen useg baibal dabtalt buyu togloom urgejlene. 
    print("Current hand:" , end='') dsiplay_hand(hand) odoogiin handiig kheblekh
    word=input(Enter word, or"!!" to indicate that you are finished: ')
    if word=='!!': (finished_by_marks=1) toglogch !! oruulsan uyd togloom shuud suusna break
    if is_valid_word(word, hand, word_list): toglogchiin oruulsan ug zub esekhiig shalgakh
    ug word_list dotor baigaa eskhiig hand dotorkh usguudeer ugiig burduulj bolokh esekh
    cur=get_word_score(word, calculate_handlen(hand))- ugnii nooog toosolno
    score+=cur -tootsolson onoog nemne
    else:- ug buruu bol ankhaaruulga ugukh
    hand=update_hand(hand, word)-ugend khereglesen usgiig hand-aas khasakh
    if finished_by_marks==0: useg duussan bol
    else: toglogch !! oruulsan bol     niit onoog kheblene
    """
    
    score=0
    finished_by_marks=0
    while calculate_handlen(hand)>0:
        print("Current Hand:", end=' ')
        display_hand(hand)
        word=input('Enter word, or "!!" to indicate that you are finished: ')
        if word=='!!':
            finished_by_marks=1
            break
        if is_valid_word(word, hand, word_list):
            cur=get_word_score(word, calculate_handlen(hand))
            score+=cur
            print('"',word,'" earned ',cur,' points. Total: ',score,' points')
        else:
            print('That is not a valid word. Please choose another word.')
        hand=update_hand(hand, word)
        #print('Current hand:', end=' ')
        #display_hand(hand)
    if finished_by_marks==0:
        print('Ran out of letters. Total score: ',score,' points')
    else:
        print('Total score: ',score,' points')
    return score
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """
    funkts ni hereglegchees songoson neg usgiig sanamsarguigeer shineusgeer solikh bolomjiig olgodog
    Shine useg ni umnu ni khereglegdeegui, VOWELS esbel CONSONANTS usguudiin sanamsargui songolt baikh yostoi.
    if letter not in VOWELS: khereb ugugdsun useg egshig bol
    khuuchin usegtei dabkhtsakhgui, gard baikhgui shine egshig usgiin jagsaalt uusgene. new_vowels=[i for i in VOWELS
    if i!=letter and i not in new_hand]
    sub=random.choice(new_vowels) bolomjit egshgees sanamsargui songokh
    else: consonants -aas yag sainii argaar
    hand[sub]=hand[letter] hand[letter]=0 return hand hand-iig shuud uurchilun butsaana
    """
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
    """
    khereglegchiin toglokh togloomiin tsubraliig udirdakh funkts
    word_list- parametr nb togloomnd ashiglakh bolomjit ugiin jagsaalt.
    uesd_replay khubisagchiig 0 gej ankhnii utgiig onooj baina. Ene n khereglegch dahin toglokh bolomjiig neg uf=daa l ashiglaj
    bolokhiig khyanakhad ashiglagdana. hereglegchees toglokh garuudiin niit toog asuuj, hands hubsagchid khadgalna
    used_sub khubsagch ni useg oruulakh fun ktsiig neg l udaa ashiglakh bolomjtoi baidliig khyanakhad ashiglagdana.
    tot=0 tot khubtsagch ni niit onoog khadgalakh zoriulalttai.
    hand=deal_hand(HAND_SIZE) funkts ni shine gar uusgej, hand huvsagchid khadgalna
    id used_sub==0: khereb kherglegch umnu n useg oruulj baigaagui, bol daraakh code ajillana used_input("") if useb_sub=='yes':--
    khereb kherglegch yes gej oruulbal used_sub=1 bolgoj dahin useg solikh bolomjgui bolgoj baina
    letter=input("")--khereglegchees yamar usgiig solikhiig khusej baigaag asuuna
    hand=substitute_hand(hand, letter)-funktsiig ashiglaj tukhain gariin letter usgiig shine usegeer solino
    display_hand(hand) usgiig solisnii daraa shine gariig kharuulna
    cur=play_hand(hand, word_list) funkts ni tukhain garaaar togloj, absan onoog cur khubsagchid khadgalna
    if used_replay==0:--kherbee khereglegch umnu n dakhin toglokh bolomjoo ashiglaagui bol replaying=input("")
    kherglegchees ene gariig dakhin toglokhiig khusej baigaa esekhiig asuuna. if replaying=="yes":
    khereb yes gej khariulbal: used_replay=1 bolgoj, dakhin toglokh bolomjgui bolgono. 
    hand=deal_hand(HAND_SIZE) shine gar uusgene display_hand(hand) dakhin toglokh shine gariig delgetsend kharuulna.
    cur=play_hand(hand, word_list)--shine gariig togluulj, shine onoog cur khubsagchid khadgalna. tot+=cur
    cur-g tot-d nemne print("") niit onoog kheblekhees umnu todorkhoilokh khesgiig kheblene. print(tot)
    tot khubsagchiig utga buyu niit onoog kheblene.
    """
    used_replay=0
    hands=int(input("Enter total number of hands: "))
    used_sub=0
    tot=0
    for i in range(hands):
        hand=deal_hand(HAND_SIZE)
        display_hand(hand)
        if used_sub==0:
            use_sub=input("Would you like to substitute a letter? ")
            if use_sub=='yes':
                used_sub=1
                letter=input("Which letter would you like to replace: ")
                hand=substitute_hand(hand, letter)
                display_hand(hand)
        cur=play_hand(hand,word_list)
        print('-----Umi----')
        if used_replay==0:
            replaying=input("Would you like to replay the hand? ")
            if replaying=="yes":
                used_replay=1
                hand=deal_hand(HAND_SIZE)
                display_hand(hand)
                cur=play_hand(hand,word_list)
        tot+=cur
    print("Total score over all hands:",end=' ')
    print(tot)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
