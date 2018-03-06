def censor(text, word):
  text = text.lower()
  word = word.lower()
  words = text.split()
  star = "*" * len(word)
  for badword in words:
    if badword == word:
      element = words.index(badword)
      words.insert(element, star)
      words.remove(badword)
  result = " ".join(words)
  print(result)
censor("get the fuck out of here", "fuck")



