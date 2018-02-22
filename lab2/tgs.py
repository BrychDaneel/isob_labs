import des
import random
from struct import *
import time

server_keys = {}


AS_TGS = 16204593401359085
TGS_ID = 823953
SERVER_TICKET_LENGHT = 60 #sec


def register():
    serv_id = random.randrange(0,256,1)
    key = des.get_random_key()
    server_keys[serv_id] = key
    return serv_id, key


def get_ticket(TGT_enc, AUTH_enc, server_id):
    print("\n\n" + "="*30 + format("REQUEST TO TGS") + "="*30)
    print("INPUT TGT x K_as_tgs: {}\n".format(TGT_enc))
    print("INPUT AUTH x K_c_tgs: {}\n".format(AUTH_enc))
    print("SERVER_ID: {}".format(server_id))

    TGT = des.decrypt(TGT_enc, AS_TGS)
    print("\ndecrypted TGT: {}\n".format(TGT))
    clid, tgs_id, tm1, ticket_length, C_TGS = unpack("QQQQQ", TGT)

    print("UNPACK")
    print("Client ID: ", clid)
    print("tgs_id: ", tgs_id)
    print("ticket time: ", tm1)
    print("ticket time length: ", ticket_length)
    print("K_c_tgs: ", C_TGS)

    if server_id not in server_keys:
        print("ERROR: INVALID SERVER")
        exit(1)

    now = int(time.time())
    if now - tm1 > ticket_length or tgs_id != TGS_ID:
        print("ERROR: INVALID TIME")
        exit(1)

    AUTH = des.decrypt(AUTH_enc, C_TGS)
    clid2, tm2 = unpack("QQ", AUTH)

    if now - tm2 > ticket_length or clid != clid2:
        print("ERROR: INVALID TIME")
        exit(1)

    K_c_ss = des.get_random_key()
    print("GEnerated K_c_ss: ", K_c_ss)

    TGS = pack("QQQQQ", clid, server_id, now, SERVER_TICKET_LENGHT, K_c_ss)
    print("\npacked TGS: \n", TGS)
    TGS_enc = des.encrypt(TGS, server_keys[server_id])
    print("\nEncrypted TGS: \n", TGS_enc)

    responce = bytearray()
    responce.append(len(TGS_enc) // 256)
    responce.append(len(TGS_enc) % 256)
    responce = responce + TGS_enc + pack("Q", K_c_ss)

    print("\nPacked responce( TGS x K_ss_tgs, K_c_ss): \n", responce)

    res = des.encrypt(responce, C_TGS)
    print("\nResponce x K_c_tgs: \n", res)
    print("="*60)
    print()
    return res
