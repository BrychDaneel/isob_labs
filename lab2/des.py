import des_const as dc
import random


def binaryze(b, cnt=0):
    res = []
    while b:
        res.append(b & 1)
        b >>= 1

    for _ in range(cnt - len(res)):
        res.append(0)

    return reversed(res)


def debinaryze(seq):
    b = 0
    for bit in seq:
        b = (b << 1) + bit
    return b


def keys_gen(key):
    byts = [[] for i in range(8)]
    for i, bit in enumerate(key):
        byts[i // 7].append(bit)
    for byt in byts:
        ch = 0
        for bit in byt:
            ch = ch ^ bit
        byt.append(ch ^ 1)

    nk = []
    for byt in byts:
        nk = nk + byt

    c0 = [nk[pos-1] for pos in dc.C0]
    d0 = [nk[pos-1] for pos in dc.D0]

    res = []
    ci, di = c0, d0
    for shift in dc.SH:
        ci = ci[shift:] + ci[:shift]
        di = di[shift:] + di[:shift]
        full_key = ci + di
        res.append([full_key[pos-1] for pos in dc.K])

    return res

def f(d, key):
    ext_d = [d[pos-1] for pos in dc.E]
    add_d = [ext_d[i] ^ key[i] for i in range(len(ext_d))]

    s_res = []
    for block_id in range(8):
        block_start = block_id * 6
        a = add_d[block_start] * 2 + add_d[block_start+5]
        b = 0
        sh = 8
        for pos in range(block_start+1, block_start+5):
            b += sh * add_d[pos]
            sh >>= 1

        s_res += binaryze(dc.S[block_id][a][b], 4)

    return [s_res[pos-1] for pos in dc.P]


def encrypt(mesg, key):
    mesg_add = bytearray([len(mesg) // 256, len(mesg) % 256])
    while (len(mesg_add) + len(mesg)) % 8:
        mesg_add.append(random.randrange(0,256,1))


    keys = keys_gen(binaryze(key, 56))
    mesg_ext = mesg_add + mesg

    result = bytearray()
    for bs in range(0, len(mesg_ext), 8):
        d = []
        for i in range(bs, bs+8):
            d.extend(binaryze(mesg_ext[i], 8))

        d_ip = [d[pos-1] for pos in dc.IP]
        dl, dr = d_ip[:32], d_ip[32:]
        for roundn in range(16):
            new_dl = dr
            f_res = f(dr, keys[roundn])
            new_dr = [f_res[pos] ^ dl[pos] for pos in range(len(f_res))]
            dl, dr = new_dl, new_dr

        new_d = dl + dr
        d_res = [new_d[pos-1] for pos in dc.IP_n]
        for i in range(0, 64, 8):
            result.append(debinaryze(d_res[i:i+8]))

    return result


def decrypt(mesg, key):
    keys = keys_gen(binaryze(key, 56))

    result = bytearray()
    for bs in range(0, len(mesg), 8):
        d = []
        for i in range(bs, bs+8):
            d.extend(binaryze(mesg[i], 8))

        d_ip = [d[pos-1] for pos in dc.IP]
        dl, dr = d_ip[:32], d_ip[32:]
        for roundn in range(15, -1, -1):
            new_dr = dl
            f_res = f(dl, keys[roundn])
            new_dl = [f_res[pos] ^ dr[pos] for pos in range(len(f_res))]
            dl, dr = new_dl, new_dr

        new_d = dl + dr
        d_res = [new_d[pos-1] for pos in dc.IP_n]
        for i in range(0, 64, 8):
            result.append(debinaryze(d_res[i:i+8]))

    ln = result[0] * 256 + result[1]
    exceed = len(result) - ln
    return result[exceed:]


def get_random_key():
    return random.randrange(0,1<<56,1)
