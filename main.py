from dotenv import load_dotenv

from src.ssh import get_process_list

# load env variables
load_dotenv()


def start() -> None:
    process_list: list = get_process_list()
    # for process in process_list:
    #     print(process)
    # return
    formatted_output_dict = {}
    for i in process_list:
        formatted_output_dict[i[0]] = {
            "load": i[1],
            "active": i[2],
            "sub": i[3],
            "desc": " ".join(i[4:])
        }
    print("\n\n\n")
    for k in formatted_output_dict:
        print(k, formatted_output_dict[k])
    # print(formatted_output_dict)


if __name__ == '__main__':
    start()
