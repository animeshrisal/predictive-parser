class First:
    def __init__(self, key):
        self.key = key
        self.values = set()

    def setValues(self, values):
        self.values.add(values)

    def getValues(self):
        return self.values

    def getFirstName(self):
        return self.key

    def setFirstName(self, key):
        self.key = key

###########################
#Grammar

E = 'Tf'
e = ['+Te', 'm']
T = 'Ft'
t = ['*Ft', 'm']
F = ['(E)', 'i']

############################

list_of_keys = []
print("Add all the keys in the grammar. Press cont to start the parsing")
start_symbol = input('Enter the start symbol')

while True:
    text = input()
    if text == 'cont':
        break
    else:
        list_of_keys.append(text)

list_of_firsts = []
list_of_follows = []

def getFirst(x):
    first = First(x)
    if isinstance(eval(x), list):
        for term in eval(x):
            if term[0] in list_of_keys:
                val = getFirst(term[0])
                val.setFirstName(first.getFirstName())
                return val
                return getFirst(term[0])
            else:
                first.setValues(first.setValues(term[0]))

    else:
        for term in eval(x):
            if term in list_of_keys:
                val = getFirst(term)
                val.setFirstName(first.getFirstName())
                return val
            else:
                first.setValues(first.setValues(term))

    return first

def findChar(x):
    follow = First(x)
    for val in list_of_keys:
        if isinstance(eval(val), list):
            for term in eval(val):
                for char in term:
                    if x == char:
                        print('Found', ' ', x, ' in ', val)
                            
        else:
            for term in eval(val):
                if x == term:
                    print('Found', ' ', x , 'in ' , val)

def getFollow(x):
    pass

for x in list_of_keys:
    list_of_firsts.append(getFirst(x))

for x in list_of_firsts:
    print(x.getValues())

for x in list_of_keys:
    list_of_follows.append(findChar(x))