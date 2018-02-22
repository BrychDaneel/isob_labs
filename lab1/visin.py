def encrypt(s, key):
    anum = ord('z') - ord('a') + 1
    res = []
    i = 0
    for c  in s:
        if c > 'z' or c < 'a':
            res.append(c)
            continue

        c_num = ord(c) - ord('a')
        delta = ord(key[i % len(key)]) - ord('a')
        new_c_num = (c_num + delta + anum) % anum
        new_c = chr(new_c_num + ord('a'))
        res.append(new_c)
        i += 1
    return ''.join(res)

def dencrypt(s, key):
    anum = ord('z') - ord('a') + 1
    res = []
    i = 0
    for c  in s:
        if c > 'z' or c < 'a':
            res.append(c)
            continue

        c_num = ord(c) - ord('a')
        delta = ord(key[i % len(key)]) - ord('a')
        new_c_num = (c_num - delta + anum) % anum
        new_c = chr(new_c_num + ord('a'))
        res.append(new_c)
        i += 1
    return ''.join(res)
