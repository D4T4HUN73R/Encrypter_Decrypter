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
""" A simple Python script that encrypts a text file. """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from cryptography.fernet import Fernet
# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# GENERATE KEY
key = Fernet.generate_key()

# STORE KEY
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

# LOAD KEY    
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

# FUNCTION FOR ENCRYPTION
f = Fernet(key)

# READ FILE AND STORE
with open('mytext.txt', 'rb') as original_file:
    original = original_file.read()

# ENCRYPT TEXT
encrypted = f.encrypt(original)

# SAFE ENCRYPTED TEXT
with open ('enc_mytext.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
