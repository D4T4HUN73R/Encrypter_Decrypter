#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By : TheDataHunter - https://github.com/TheDataHunter
# Created Date : 08/08/2022
# version ='1.0'
# status : RFU (ready for use)
# license : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# copyrights : 
# ---------------------------------------------------------------------------
""" A simple Python script that decrypts a text file. """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from cryptography.fernet import Fernet
# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# LOAD KEY    
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

# FUNCTION FOR DECRYPTION
f = Fernet(key)

# READ FILE AND STORE
with open('enc_mytext.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

# DECRYPT TEXT
decrypted = f.decrypt(encrypted)

# SAFE DECRYPTED TEXT
with open('dec_mytext.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
