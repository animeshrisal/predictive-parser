class First:
    def __init__(self, key):
        self.key = key
        self.values = []

    def setValues(self, values):
        self.values.append(values)

    def getValues(self):
        return self.values

    def getFirstName(self):
        return self.key

    def setFirstName(self, key):
        self.key = key

    def filterNone(self):
        self.values = list(filter(None.__ne__, self.values))

class Follow:
    def __init__(self, key):
        self.key = key
        self.values = []

    def setValues(self, values):
        self.values += values

    def getValues(self):
        return self.values

    def getFirstName(self):
        return self.key

    def setFirstName(self, key):
        self.key = key

    def removeRepeated(self):
        newVal = []
        for i in self.values:
            if i not in newVal:
                newVal.append(i)

        self.values = newVal


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
    follow = Follow(x)
    if x == start_symbol:
        follow.setValues('$')
    for val in list_of_keys:
        if isinstance(eval(val), list):
            for term in eval(val):
                for char in term:
                    if x == char:
                        if x == val:
                            continue
                        else:
                            follow.setValues(getFollow(x , val))    
                            pass
                            
        else:
            for term in eval(val):
                if x == term:
                    if x == val:
                        continue
                    else:
                        follow.setValues(getFollow(x , val))  
                        pass
                    
    return follow

def getFollow(x, term):
    print(x, ' ',term)
    if isinstance(eval(term), list):
        for z in eval(term):
            counter = 0
            text = z
            for char in z:
                if x == char:
                    if text[counter] == text[-1]: #checks if character is last element of char
                        return get_follow_object(x, term)

                    else:
                        if text[counter+1] in list_of_keys:
                            return get_first_object(text[counter], text[counter+1])

                        else:
                            return text[counter+1]
                
                counter += 1

    else:
        counter = 0
        text = eval(term)
        for char in text:
            if char == x:
                if text[counter] == text[-1]:
                    if text[counter] in list_of_keys:
                        return get_follow_object(x, term)

                else:
                    if text[counter+1] in list_of_keys:
                        return get_first_object(term, text[counter+1])
                    else:
                        return text[counter+1]

            counter += 1

def get_first_object(x, term):
    print(term, ' ', x, 'wew')
    tempVal = ''
    for first in list_of_firsts:
        if term == first.getFirstName():
            if 'm' in first.getValues():
                tempVal = first.getValues()
                tempVal.remove('m')
                tempVal += get_follow_object(x, x)
                return tempVal
            else:
                return first.getValues()

def get_follow_object(x, term):
    for follow in list_of_follows:
        if term == follow.getFirstName():
            return follow.getValues()

###########################
#Grammar

E = 'Te'
e = ['+Te', 'm']
T = 'Ft'
t = ['*Ft', 'm']
F = ['(E)', 'i']

############################

list_of_keys = []
print("Add all the keys in the grammar. Press cont to start the parsing")


while True:
    text = input()
    if text == 'cont':
        break
    else:
        list_of_keys.append(text)

list_of_firsts = []
list_of_follows = []

start_symbol = input("Enter Start Symbol")

for x in list_of_keys:
    list_of_firsts.append(getFirst(x))

for x in list_of_firsts:
    x.filterNone()
    print(x.getValues())

for x in list_of_keys:
    list_of_follows.append(findChar(x))

for x in list_of_follows:
    x.removeRepeated()
    print(x.getFirstName(), ' ', x.getValues())