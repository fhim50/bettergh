f = open('text.txt', 'r')

def split_string(source,splitlist):
    output = []

    atsplit = True# at any split point
    for char in source:
        if char in splitlist:
            atsplit = True

        else:
            if atsplit:
                output.append(char)
                atsplit = False
            else:
                # add character to last word
                output[-1] = output[-1] + char
    
    return output

  





out = split_string(['A man AMA'] ,"A")
print out
'''
out1 = split_string(out , ' \ ')
print out1
'''
