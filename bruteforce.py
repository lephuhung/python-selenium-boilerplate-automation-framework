from index import login
import time
# open file dsmail.txt

with open('dsmail.txt', 'r') as f:
    lines = f.readlines()
    with open('dspassword.txt', 'r') as file:
        passwords = file.readlines()
    for username in lines:
        for password in passwords:
            username = username.rstrip('\n')
            password = password.rstrip('\n')
            login(username, password)
            time.sleep(6)
