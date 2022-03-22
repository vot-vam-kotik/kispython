def replacing(text):
    text = list(text)
    # print(text)
    quotes = []
    for i in range(len(text)):
        if text[i] == "\"" or text[i] == "\'":
            quotes.append(i)
    # print(quotes)

    for left_kav in quotes[0:-1:2]:
        text[left_kav] = "«"

    # print(quotes[1::2])

    for right_kav in quotes[1::2]:
        text[right_kav] = "»"

    text = ''.join(text)
    return text


s = "g\"g\"g g 'g'"
print(replacing(s))
