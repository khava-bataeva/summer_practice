def direction(s, first, second, palindromes):
    while first >= 0 and second < len(s) and s[first] == s[second]:
        palindromes.add(s[first: second + 1])
        first = first - 1
        second = second + 1
        

def findSubstrings(s):
    palindromes = set()
    for i in range(len(s)):
        direction(s, i, i, palindromes)
        direction(s, i, i + 1, palindromes)
    print(palindromes, end = '')


if __name__ == '__main__':
    s = 'aabbdaad'
    findSubstrings(s)
