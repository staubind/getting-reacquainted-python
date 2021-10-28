def longest(s1, s2):
    unique = set()
    unique.update(list(s1))
    unique.update(list(s2))
    return ''.join(sorted(list(unique)))
    
print(longest("aretheyhere", "yestheyarehere")) # 'aehrsty'