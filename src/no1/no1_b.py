def isSubstring(s1, s2):
    print "true" if s1 in s2 or s2 in s1 else "false"


s1 = raw_input()
s2 = raw_input()
isSubstring(s1, s2)