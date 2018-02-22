import tgs
import time
import des
from struct import *


my_id, my_key = tgs.register()
print("SERVER_ID: {}".format(my_id))
print("SERVER_KEY: {}".format(my_key))


def get_id():
    return my_id


def request(TGS_enc, AUTH_enc):
    print("="*30 +"REQUEST TO SERVER"+ "="*30)
    print("Input TGS x K_ss_tgs: \n{}\n".format(TGS_enc))
    print("Input AUTH x K_c_ss: \n{}\n".format(AUTH_enc))

    TGS = des.decrypt(TGS_enc, my_key)
    print("TGS: \n{}\n".format(TGS))
    clid, server_id, ticket_time, server_ticket_length, K_c_ss = unpack("QQQQQ", TGS)

    print("UNPACK")
    print("clid: ", clid)
    print("server id: ", server_id)
    print("ticket time: ", ticket_time)
    print("server_ticket_length: ", server_ticket_length)
    print("K_c_ss: ", K_c_ss)

    now = int(time.time())
    if server_id != my_id or now - ticket_time > server_ticket_length:
        print("ERROR")
        exit(1)

    auth = des.decrypt(AUTH_enc, K_c_ss)
    print("AUTH: \n{}\n".format(auth))
    clid2, tm2 = unpack("QQ", auth)

    print("Request client ID: ", clid2)
    print("Request time: ", tm2)

    if clid != clid2 or now - tm2 > server_ticket_length:
        print("ERROR")
        exit(1)

    responce = pack("Q", tm2+1)

    print("Responce: \n{}\n".format(responce))
    res = des.encrypt(responce, K_c_ss)
    print("Responce x K_c_ss: \n{}\n".format(res))
    print()
    print("="*60)
    print()
    return res
