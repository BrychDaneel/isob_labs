def encrypt(s, key):
    anum = ord('z') - ord('a') + 1
    res = []
    for c  in s:
        if c > 'z' or c < 'a':
            res.append(c)
            continue

        c_num = ord(c) - ord('a')
        new_c_num = (c_num + key + anum) % anum
        new_c = chr(new_c_num + ord('a'))
        res.append(new_c)
    return ''.join(res)

def dencrypt(s, key):
    anum = ord('z') - ord('a') + 1
    res = []
    for c  in s:
        if c > 'z' or c < 'a':
            res.append(c)
            continue

        c_num = ord(c) - ord('a')
        new_c_num = (c_num - key + anum) % anum
        new_c = chr(new_c_num + ord('a'))
        res.append(new_c)
    return ''.join(res)
