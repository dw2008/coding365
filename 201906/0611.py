tableData = [["apples", 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def findLong(alist) :
    result = 0
    for x in alist :
        if len(x) > result :
            result = len(x)
    return result

def printCol(alist) :
    maxLen = findLong(alist)
    for x in alist :
        print(x.rjust(maxLen))

def printTable(table) :
    alist = list()
    rows = len(table[0])
    cols = len(table)
    for row in range(0, rows) :
        thing = ""
        for col in range(0, cols) :
            maxLen = findLong(table[col])
            thing = thing + table[col][row].rjust(maxLen)
            thing = thing + " "
        print(thing)        
printTable(tableData)