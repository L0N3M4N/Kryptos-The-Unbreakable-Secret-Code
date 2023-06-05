import random 
import time
import math

# solved
k1 = 'EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD'
plaintext1 = 'BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION'
posct1 = 0

# solved
k2 =         'VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGEXWJLLAETG'
plaintext2 = 'ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTXLAYERTWO'
posct2 = 0


# remain unsolved until now  
# copy this original k4 found in CIA sites

k4 = 'OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR'
plaintext4 = 'BERLINCLOCK' 
posct4 = 63

# veteran_cia_ = """
# In 2010, a CIA veteran named David Stein proposed that the last 97 characters of K4 spell out the message “BERLINCLOCK”. 
# But this theory was later debunked by the artist himself.
# In 2016, Sanborn revealed that the first letter of the plaintext of K4 is the letter 'N' and the last letter of the plaintext is 'X'.
# """
# print(veteran_cia_)

# hint = """
#  According to my knowledge cutoff in 2021, the artist James Sanborn has given several hints and clues to help people trying to solve the fourth part of the Kryptos sculpture (K4), however, none of these hints have led to the definite solution of the cipher. Here are some of the hints that have been given:
# -In 2010, Sanborn revealed that the 64th, 65th, 66th, and 67th characters of the encrypted message spell out the letters "NYPV" which is an acronym for "New York Palimpsest V"
# -In 2011, he revealed that the plaintext of the first letter is "N" and the last letter of the plaintext is "X"
# -In 2014, Sanborn said that the plaintext of K4 is a proper noun and its length is less than 80 characters.
# -In 2016, James Sanborn said that the plaintext of K4 is not a word in any language and it is not a name of a person or place.
# """
# print(hint)


# python decrypter modified version  
# create your own version this script is modified.

alph = 'KRYPTOSABCDEFGHIJLMNQUVWXZ'

vig = ['ABCDEFGHIJLMNQUVWXZKRYPTOS',
       'BCDEFGHIJLMNQUVWXZKRYPTOSA',
       'CDEFGHIJLMNQUVWXZKRYPTOSAB',
       'DEFGHIJLMNQUVWXZKRYPTOSABC',
       'EFGHIJLMNQUVWXZKRYPTOSABCD',
       'FGHIJLMNQUVWXZKRYPTOSABCDE',
       'GHIJLMNQUVWXZKRYPTOSABCDEF',
       'HIJLMNQUVWXZKRYPTOSABCDEFG',
       'IJLMNQUVWXZKRYPTOSABCDEFGH',
       'JLMNQUVWXZKRYPTOSABCDEFGHI',
       'LMNQUVWXZKRYPTOSABCDEFGHIJ',
       'MNQUVWXZKRYPTOSABCDEFGHIJL',
       'NQUVWXZKRYPTOSABCDEFGHIJLM',
       'QUVWXZKRYPTOSABCDEFGHIJLMN',
       'UVWXZKRYPTOSABCDEFGHIJLMNQ',
       'VWXZKRYPTOSABCDEFGHIJLMNQU',
       'WXZKRYPTOSABCDEFGHIJLMNQUV',
       'XZKRYPTOSABCDEFGHIJLMNQUVW',
       'ZKRYPTOSABCDEFGHIJLMNQUVWX',
       'KRYPTOSABCDEFGHIJLMNQUVWXZ',
       'RYPTOSABCDEFGHIJLMNQUVWXZK',
       'YPTOSABCDEFGHIJLMNQUVWXZKR',
       'PTOSABCDEFGHIJLMNQUVWXZKRY',
       'TOSABCDEFGHIJLMNQUVWXZKRYP',
       'OSABCDEFGHIJLMNQUVWXZKRYPT',
       'SABCDEFGHIJLMNQUVWXZKRYPTO']

#Find the number of matches (out of a maximum 11)
def findRating(segin, segpt):
    totalmatch = 0
    totallen = len(segin)
    for z in range(0, totallen):
        if segin[z] == segpt[z]:
            totalmatch += 1
    return(totalmatch)


def capsct(strk4):
    testnew = strk4
    
    #Create a list from 0 to the length of the input string
    templist = list(range(0, len(testnew)))
    random.shuffle(templist)
    scramit = ""

    for followit in templist:
            scramit += testnew[followit]

    return(scramit,templist)

#Now that we have a match, find the placement of the original ciphertext letters before they with placed together as BERLINCLOCK 
def makefft(k4in, bcarray):

    uplower = k4in
    
    #Find the original 11 indicies of the scrambled BERLINCLOCK cyphertext
    cipharray = bcarray[63:74]

    #Loop through the berlinclock indicies and make those 11 characters uppercase in the ciphertext
    ulout = ""
    fftprep = []
    for ctall in range(0, len(uplower)):
        flagfound = 0
        for loopca in range(0, len(cipharray)):
            
            #If this is character 13 in the ciphertext and [13] was found in the BC array, we have a match!
            if ctall == cipharray[loopca]:
                flagfound = 1
                break
                
        if flagfound == 1:
            ulout += uplower[ctall].upper()
            fftprep += [1]
        else:
            ulout +=  uplower[ctall].lower()
            fftprep += [0]
        
    return(ulout, fftprep)

print("Starting at " + time.strftime('%X %x %Z') + "\n")
sys.stdout.flush()
    
#Only look at ratings of 8/11 or higher
ratebest = 8
#PLK test at 7
#ratebest = 7
snipbest = ""
wordbest = ""

#for i in range(0, 1):
for i in range(0, 100000):
    
    #scram = k4
    (slist,ctten) = capsct(k4)
    scram = ''.join(slist)
    #print(scram)
    
    kout = ""
    posct = posct4
    groupit = ""
    
    #Do a Vigenere translation based on K1 and K2 on the new random (scram) arrangement
    for j in plaintext4:
        #print("j= " + j)
        alphpos = alph.find(j)
        #print("alphapos= " + str(alphpos))
        
        cttry = scram[posct]
        #print("cttry= " + cttry)
        groupit += cttry
        
        knew = ''
        for k in vig:
            vigtry = k[alphpos]
            if vigtry == cttry:
                #print("k= " + k)
                knew = k[0]
                break
        #print(knew)
        kout += knew
        posct += 1
    
    #At this point. we have scram and kout
    #print(kout + ' = ' + scram)

    #Test for a match of an English word
    fin = open('rockyou.txt') # brute forcing match string

    for linein in iter(fin):

        testin = fin.readline()
        testin = testin.strip()
        testin = testin.upper()
        #testin = "PALIMPSEST"
        #print(testin)
        
	#Only look at dictionary words of at least length 6 or greater
        if len(testin) > 5:
            testline = ""
            testline = testline + testin + testin + testin + testin + testin
            testline = testline + testin + testin + testin + testin + testin
            testline = testline + testin + testin + testin + testin + testin
            #print(testline)
            testseg = testline[posct4:(posct4+len(kout))]
            #print(testseg)
                
            ratenew = findRating(testseg, kout)
            if ratenew >= ratebest:
                #ratebest = ratenew
                snipbest = kout
                wordbest = testin

                (lowerout, arrout) = makefft(k4, ctten)
                
                print("Rating: " + str(ratenew) + " out of " + str(len(kout)))
                print(lowerout)
                #print(arrout)
                print("Groupit: " + groupit)
                print("Segment: " + snipbest)
                print("Word: " + wordbest)
                print(scram)
                #print(ctten)

                
                #longerarrout = arrout + [0,0,0]
                #N = len(longerarrout)
                #print("Len: " + str(N))
                #W = np.fft.fft(longerarrout)
                #freq = np.fft.fftfreq(N,1)
                #absW = abs(W)
                #absW[0] = 0
                #idx = absW.argmax(axis=0) 
                #idxval = (np.amax(absW)+1)
                #max_f = abs(freq[idx])
                #myest = int(round(1/max_f))
                
                #print("Period estimate: ", myest)
                #print("Period estimate: ", (1/max_f))
                #print("Strength: ", idxval)
                #print("")
                
                #plt.subplot(211)
                #plt.scatter([max_f,], [np.abs(W[idx]),], s=100,color='r')
                #plt.plot(freq[:N/2], abs(W[:N/2]))
                #plt.xlabel(r"$f$")

                #plt.subplot(212)
                #plt.plot(1.0/freq[:N/2], abs(W[:N/2]))
                #plt.scatter([1/max_f,], [np.abs(W[idx]),], s=100,color='r')
                #plt.xlabel(r"$1/f$")
                #plt.xlim(0,20)

                #plt.show()
                
    fin.close()          
    if ((i % 1000 == 0) and (i > 0)):
        print("Iteration: " + str(i) + " at " + time.strftime('%X %x %Z'))

print("Done at " + time.strftime('%X %x %Z'))
