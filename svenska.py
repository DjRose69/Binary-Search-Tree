
from bintreeFile import Bintree

svenska = Bintree()

print()
print('Skriver ut kryptiskt meddelande...')
print()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:
            print(f'{ordet} ', end = '')
        else:
            svenska.put(ordet)             # in i sökträdet
