def find_message(text):
    """Find a secret message"""
    message = ""
    while len(text) > 0:
        for ch in list(text):
            if ch.isupper() == True:
                message +=ch
        return message
    return message

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
