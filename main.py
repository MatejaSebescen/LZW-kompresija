
limit = 2048
current = 265
dictionary = {}

def make_dictionary():
    k = '’'
    dictionary[k] = 0
    k = '”'
    dictionary[k] = 1
    k = '“'
    dictionary[k] = 2
    k = '‘'
    dictionary[k] = 3
    k = '—'
    dictionary[k] = 4
    k = '–'
    dictionary[k] = 5
    k = '…'
    dictionary[k] = 6
    for i in range(255):
        dictionary[chr(i)] = i+7

#START PROGRAM
newf = open("coded.txt", "w", encoding="utf-8")
make_dictionary()

w = ''                                                                      # w = NIL
with open('readme.txt', "r", encoding="utf-8") as f:
    for char in f.read():                                                   # k = file.char
        if (w+char) in dictionary:                                          # is wk in dictionary?
            w = w+char                                                      # YES: w = wk
        else:
            newf.write(chr(dictionary[w]))                                  # newfile[pointer] = dictionary(w)
            print(w + " " + str(dictionary[w]))                             # po ASCII tabeli
            if current < limit:                                             # dictionary[limit] < dictionary[current]
                dictionary[w+char] = current                                # dictionary[current] = wk
                current = current+1                                         # current++
            w = char                                                        # w = k

print(w + " " + str(dictionary[w]))
newf.write(chr(dictionary[w]))                                              # poslednji w

f.close()
newf.close()
exit()
#END PROGRAM