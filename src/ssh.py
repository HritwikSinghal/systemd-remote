import os

import paramiko


# todo: get host name:port list from file
# todo: get ssh key, pass from file
# todo: multi-threaded


def get_process_list() -> list:
    ssh = paramiko.SSHClient()
    k = paramiko.RSAKey.from_private_key_file("/home/hritwik/.ssh/id_rsa", password=os.getenv("PASSWORD"))
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('172.105.47.207', username="root", pkey=k)
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("systemctl list-units --no-page")
    out: list = ssh_stdout.readlines()[1:-7]
    out = list(map(lambda x: x.split(), out))
    return out
