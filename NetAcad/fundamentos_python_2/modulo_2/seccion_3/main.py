def mysplit1(strng):
    if strng == '' or strng.isspace():
        return []
    list = []
    word = ''
    inword = not strng[0].isspace()

    for x in strng:
        if inword:
            if not x.isspace():
                word = word + x
            else: 
                list.append(word)
                inword = False
        else:
            if not x.isspace():
                inword = True
                word = x
            else:
                pass
    if inword:
        list.append(word)
    return list

print(mysplit1('jeje me llama la atencion todo!'))        