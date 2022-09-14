from dotenv import load_dotenv

from src.ssh import get_ssh_data

load_dotenv()


def start() -> None:
    out: list = get_ssh_data()
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


if __name__ == '__main__':
    start()
