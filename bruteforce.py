from index import login
import time
# open file dsmail.txt

with open('dsmail.txt', 'r') as f:
    lines = f.readlines()
    with open('dspassword.txt', 'r') as file:
        passwords = file.readlines()
    for i in range(1, len(lines)):
        for password in passwords:
            username = lines[i].rstrip('\n')
            password = password.rstrip('\n')
            login(username, password, i)
            time.sleep(1)
