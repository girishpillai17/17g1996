def censor(text, word):
    text = text.lower()
    word = word.lower()
    star = "*" * len(word)
    if word in text:
        new_text = text.replace(word, star)
    print(new_text)

censor("get the Fuck out of here you fuCk sHit fuck ing ass", "fuck")