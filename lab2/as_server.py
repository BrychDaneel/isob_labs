import des
import random
from struct import *
import time
import tgs

client_keys = {}

AS_TGS = 16204593401359085
TGS_ID = tgs.TGS_ID
TICKET_LENGHT = 60 #sec

def register():
    clid = random.randrange(0,256,1)
    key = des.get_random_key()
    client_keys[clid] = key
    return clid, key


def get_ticket(clid):
    print("\n\n" + "="*30 + format("REQUEST TO AS(clid={})").format(clid) + "="*30)
    if clid not in client_keys:
        print("\nERROR :FAILD TO FOUND CLIENT")
        exit(1)

    clkey = client_keys[clid]
    print("K_c: {}".format(clkey))
    tm = int(time.time())
    print("now: {}".format(tm))
    C_TGS = des.get_random_key()
    print("GENERATE K_c_tgs key: {}".format(C_TGS))
    TGT = pack("QQQQQ", clid, TGS_ID, tm, TICKET_LENGHT, C_TGS)
    print("\npacked TGT(clid, TGS_ID, now, TICKET_LENGHT, C_TGS): {}\n".format(TGT))
    TGT_enc = des.encrypt(TGT, AS_TGS)
    print("\nencrypted TGT x K_as_tgs: {}\n".format(TGT_enc))

    responce = bytearray()
    responce.append(len(TGT_enc) // 256)
    responce.append(len(TGT_enc) % 256)
    responce = responce + TGT_enc + pack("Q", C_TGS)
    print("\n Packed responce(TGT_enc, K_c_tgs):  {}\n".format(responce))

    res = des.encrypt(responce, clkey)
    print("\n Encrypted responce([TGT_enc, K_c_tgs] x K_c):  {} \n".format(res))
    print("="*60)
    print()
    return res
