def checkio(words):
    count = 0
    wrds = words.split()
    for word in list(wrds):
        if word.isdigit() == False:
            count = count +1
        elif count < 3:
            count = 0 
    if count >= 3:
        return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
