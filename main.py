import paramiko
import osg
from dotenv import load_dotenv

load_dotenv()

ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file("/home/xpert/.ssh/id_rsa", password=os.getenv("PASSWORD"))

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.105.47.207', username="root", pkey=k)

ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("systemctl list-units --no-page")
out: list = ssh_stdout.readlines()[1:-7]
out = list(map(lambda x: x.split(), out))

dic = {}

for i in out:
    print(i)
    dic[i[0]] = {
        "load": i[1],
        "active": i[2],
        "sub": i[3],
        "desc": " ".join(i[4:])
    }

print(dic)
