from bintreeFile import Bintree

svenska = Bintree()
engelska = Bintree()

# skapar två trädobjekt.

print()
print('Skriver ut de kryptiska meddelandena...')
print()

with open('word3.txt', 'r') as svenskafil:
    for line in svenskafil:
        # för varje rad i filen
        word = line.strip()  # returns a copy of the string by 
                             # removing both the leading and the 
                             # trailing characters
        if word in svenska:
            # om ordet är i det binära trädet,
            # printar vi det (dubletter)
            print(f'{word} ', end = '')
        else:
            svenska.put(word) # annars läggs det till i det binära trädet



wordList = [] # tom lista reda att addera objekt

print()
print()

file2 = open('engelska.txt', 'r').readlines()
for line in file2:
    # för varje rad...
    word = line.split()   # ta bort alla "leading" och "trailing" characters
    if len(word) == 0: # om ordets längd är 0 så ignorerar vi ordet
        pass
    else:
        wordList += word # annars läggs alla ord till i ordlistan

for index in range(len(wordList)):
    if wordList[index] in engelska: # om ordet är i det binära trädet, gör inget
        pass
    else:
        engelska.put(wordList[index])  # annars lägger vi till det i trädet
        if wordList[index] in svenska:
            print(f'{wordList[index]  } ', end = '') # printar enbart ordet om det finns i det andra trädet


           


