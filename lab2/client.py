#!/usr/bin/env python3


import as_server
import tgs
import server
import des
from struct import *
import time


my_id, my_key = as_server.register()
print("CLIENT_ID: {}".format(my_id))
print("CLIENT_KEY: {}".format(my_key))


print("="*60)
print("REQUET TO AS SERVER: client_id ({})".format(my_id))
ticket_enc = as_server.get_ticket(my_id)
print("as_ticket X K_c: {}\n".format(ticket_enc))

ticket = des.decrypt(ticket_enc, my_key)
print("as_ticket: {}\n".format(ticket))

TGT_enc_len = ticket[0] * 256 + ticket[1]
TGT_enc = ticket[2: 2 + TGT_enc_len]
C_TGS, = unpack("Q", ticket[2 + TGT_enc_len :])

print("K_c_tgs: {}\n".format(C_TGS))
print("TGT x K_as_tgs: {}\n".format(TGT_enc))

tm = int(time.time())
print("now: ", tm)

auth = pack("QQ", my_id, tm)
print("AUTH: {}\n".format(auth))

auth_enc = des.encrypt(auth, C_TGS)
print("AUTH: {}\n".format(auth))

print("REQUEST TO TGS")
ticket_enc = tgs.get_ticket(TGT_enc, auth_enc, server.get_id())
print("Ticket x K_c_tgs:\n {}\n".format(ticket_enc))

ticket = des.decrypt(ticket_enc, C_TGS)
print("Ticket:\n {}\n".format(ticket))

TGS_enc_len = ticket[0] * 256 + ticket[1]
TGS_enc = ticket[2: 2 + TGS_enc_len]
K_c_ss, = unpack("Q", ticket[2 + TGS_enc_len :])

print("TGS_enc:\n{}\n".format(TGS_enc))
print("K_c_ss: {}".format(K_c_ss))

request_time = int(time.time())
auth2 = pack("QQ", my_id, request_time)
auth2_enc = des.encrypt(auth2, K_c_ss)
print("AUTH2:\n{}\n".format(auth2))
print("AUTH2 x K_c_ss:\n{}\n".format(auth2_enc))

print("REQUEST TO SERVER")
responce_enc = server.request(TGS_enc, auth2_enc)

responce = des.decrypt(responce_enc, K_c_ss)
resp_time, = unpack("Q", responce)

print("Print server responce X K_c_ss: \n{}\n".format(responce_enc))
print("Print server responce: \n{}\n".format(responce))


print("*"*60)
print("Send time: ", request_time )
print("Recv time: ", resp_time  )

if resp_time != request_time + 1:
    print("ERROR")
    exit(1)


print("\nSUCSESSS!!!!")
