def anti_vowel(t):
    v = 'aeiouAEIOU'
    g = ''
    for i in t:
        for c in v:
            if i == c:
                break
        else:
            g += i
    print(g)


anti_vowel("umbrella")