def reverse(n):
    word = " "
    m = len(n) - 1

    while m >= 0:
        word = word + n[m]
        m -= 1
    print(word)

reverse("how are you")