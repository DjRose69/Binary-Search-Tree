class BSTNode:
    # Klass för Binary Search Tree nodes
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # self.left och self.right är "pekare" som pekar till 
        # antingen vänstra eller högra "barnet" till parent-noden.
        # initialiseras till none

class Bintree:
    def __init__(self):
        self.root = None # initialiseras till none

    def put(self, newvalue):
        # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue)

    def __contains__(self, value):
        # True om value finns i trädet, False annars
        return finns(self.root,value) # returerar och följaktligen AKTIVERAR 
                                      # finns-funktionen...

    def write(self):
        print('\nSkriver ut trädet in-order:\n')
        # Skriver ut trädet i inorder
        skriv(self.root)
        print("\n")

def putta(first, newvalue):
    # hjälpfunktion för att sortera in newvalue
    # i trädet

    if first == None:
        # om first är None, skapa ny nod
        # mha BSTNode
        root = BSTNode(newvalue)
        return root  
    
    elif 

    elif newvalue < first.value:
        # om nya värdet är mindre än värdet på parent-noden,
        # så undersöker vi på den vänstra sidan av noden
        if first.left == None:
            # om vänstra "barnet" inte finns, 
            # skapa ny nod på denna plats.
            first.left = BSTNode(newvalue)
        else:
            # om vänstra barnet finns, anropa
            # rekursivt samma funktion och
            # gå igenom processen en gång till.
            putta(first.left, newvalue)
    
    elif newvalue > first.value:
        if first.right == None:
            # exakt samma process fast vi söker
            # på det högra "barnet" till parent-nodrn
            # om det nya värdet är större.
            first.right = BSTNode(newvalue)
            
        else:
            putta(first.right, newvalue)
        
    return first



def finns(first, value):
    # funktion för att se ifall värde
    # existerar i det binära trädet 
    # eller ej.

    if first == None:
        # i det fallet att värdet
        # som analyseras är None, så finns det sökta värdet
        # inte i trädet
        return False

    elif first.value == value:
        # returnerar true 
        return True

    elif value < first.value:

        # söker på vänstra sidan av noden om det
        # sökta värdet är mindre än det aktuella värdet,
        # returnerar samma funktion rekursivt...
        return finns(first.left, value)

    else:
        # söker på högra sidan av noden, returnerar
        # samma funktion rekursivt....
        if value > first.value:
            return finns(first.right, value)


def skriv(root):
    # skriver ut trädet in-order
    if root != None:
        # om noden inte är None...

        skriv(root.left) # rekursera först på det vänstra barnet
                    
        print(root.value) # sedan printa värdet på noden


        skriv(root.right) # nu rekurserar vi på det högra barnet

# Det vi gör är alltså:
# 1. Korsar det vänstra sub-trädet 
# 2. Besöker roten
# 3. Korsar det högra sub-trädet
# tills dess att alla noder har besökts


# def main():
#     tree = Bintree()
#     lista = [5, 6, 1, 3, 6, 7, 9, 10, 10, 10]
#     # lägger in dubletter för att visa att de ej läggs till i trädet
#     for element in lista:
#         tree.put(element)
#     tree.write() # skriver ut noderna in-order
#     print(tree.__contains__(10)) # skriver ut true eftersom det finns i trädet
#     print(tree.__contains__(11)) # skriver ut false eftersom det inte finns

# main()





