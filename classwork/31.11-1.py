def climber(n):
    s = ['']*(n+1)
    for i in range(0, len(s)):
        s[0] = 1
        s[1] = 1
        for i in range(2, len(s)):
            s[i] = s[i-1]+s[i-2]
        return s[-1]
    print(climber(5))