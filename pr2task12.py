def replacing(text):
    text = list(text)
    # print(text)
    quotes = []
    for i in range(len(text)): #все кавычки
        if text[i] == "\"" or text[i] == "\'":
            quotes.append(i)
    print(quotes)

    for left_kav in quotes[0:-1:2]: # замена левых
        text[left_kav] = "«"

    print(quotes[1::2]) # парные к предыдущей кавычки

    for right_kav in quotes[1::2]: # замена правых
        text[right_kav] = "»"

    text = ''.join(text)
    return text


s = "g\"g\"g g 'g'"
print(replacing(s))
