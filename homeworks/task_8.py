def main(string):
    dict = []
    dict1 = []
    mydict = {}
    i = 0
    c = 0
    i1 = 0
    while (i < len(string)):
        i = string.find('"', i)
        if i == -1:
            break
        m = i + 1
        substr = ''
        while(string[m] != '"'):
            substr = substr + string[m]
            m += 1
        i = m + 1
        dict.append(substr)
        i1 = string.find('\'', i1)
        if i1 == -1:
            break
        m1 = i1 + 1
        substr1 = ''
        while (string[m1] != '\''):
            substr1 = substr1 + string[m1]
            m1 += 1
        i1 = m1 + 1
        dict1.append(substr1)
        mydict[substr] = substr1
    return(mydict)

print(main("(( .begin new 'leorza' |> @\"erzain_974\"; .end; .begin new 'riar'|>@\"atla\";.end;.begin new 'beriar_721' |> @\"reusza\";.end; .beginnew'labi_15' |>@\"ceesala_854\"; .end; ))"))