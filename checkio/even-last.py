def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if array:
        return sum(array[::2]) * array[-1] 
    else:
        return 0
#This was so aggravting. The last part kept messing me up, and I kept rewriting my code not realizing that it was working on all but the last one.

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
