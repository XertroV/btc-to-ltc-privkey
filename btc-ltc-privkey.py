#!/usr/bin/env python

# public domain

from base58 import *
from hashlib import sha256

def dsha256(data):
   return sha256(sha256(data).digest()).digest()

privkey1 = raw_input("Input Privkey (BTC or LTC) in base58 WIF (starts with 5)\r\n > ")

privkey_bytes = b58decode(privkey1, 33)

privkey_version = privkey_bytes[0]
privkey_noversion = privkey_bytes[1:-4]

if privkey_version == chr(0x80):
  privkey_return = chr(0xb0) + privkey_noversion
else:
	privkey_return = chr(0x80) + privkey_noversion
	
checksum = dsha256(''.join(privkey_return))

privkey_return += checksum[:4]

print "New Privkey: ", b58encode(privkey_return)

raw_input("\r\nenter to quit")
