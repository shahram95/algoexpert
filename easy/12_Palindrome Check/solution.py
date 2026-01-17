def isPalindrome(string):
    # return string == string[::-1]

    lp = 0
    rp = len(string)-1

    while lp<=rp:
        if string[lp] != string[rp]:
            return False
        lp += 1
        rp -= 1
    return True