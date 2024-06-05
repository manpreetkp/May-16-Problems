mylist = []

if not mylist:
    print ("This list is empty.")
else:
    maximum = mylist[0]

    for a in mylist:
        if a > maximum:
            maximum = a

    print (maximum)
