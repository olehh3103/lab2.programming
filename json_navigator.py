"""My 2 task"""
import json
print('Hi, i`m json navigator. Pls, write "help" to see what i can do')
def info_printer():
    """
    function print info
    """
    print("help - all posible comands\n\
\tpath - Path to the JSON-file you want me to work with\n\
back - to see the previous information\n\
\tdir - all posible keys and index in curent dict or list\n\
bye - to stop the programm\n\
\tif u want to go DEEPER print 'dir' and choose a possible variable\n\
or just print an index or key")

def open_file(path):
    """
    function open json file and return data
    """
    with open(path) as file:
        info = json.load(file)
    return info


def main():
    """
    main function which asks inputs and check them
    and loop through the json-file
    """
    all_res = []
    path = ""
    while True:
        if len(all_res) != 0 and isinstance(all_res[-1], (str, int, bool)):
            print("There is no further continuation\n\
please, write 'back'")
        part = input(">>> ")
        part = part.replace("'", "").replace('"', '')
        if part == "help":
            info_printer()
        elif part == 'path':
            while True:
                if path != "":
                    all_res.clear()
                    print("Now we`ll work with new JSON-file")
                path = input("print the path\n>>> ")
                if path == "bye":
                    return print("Bye!)")
                try:
                    data = open_file(path)
                    print(json.dumps(data, indent=2))
                    all_res.append(data)
                    info_printer()
                    break
                except FileNotFoundError:
                    print("oh, something went wrong, try again")
        elif part == 'bye':
            print("Bye!)")
            break
        elif part == "back" and len(all_res) > 1:
            all_res.pop(-1)
            print(json.dumps(all_res[-1], indent=2))
        elif part == "back" and len(all_res) <= 1:
            print("u are not deep enough to go back")
        elif path != "" and part == "dir":
            if isinstance(all_res[-1], list):
                if len(all_res[-1]) == 0:
                    print(f"u can choise index 0")
                else:
                    print(f"u can choise index from 0 to {len(all_res[-1]) - 1}")
                while True:
                    choise = int(input(">>> "))
                    if choise == "bye":
                        return print("Bye!)")
                    if 0 <= choise <= len(all_res[-1]) - 1:
                        print(json.dumps(all_res[-1][choise], indent=2))
                        all_res.append(all_res[-1][choise])
                        break
                    else:
                        print("oh, something went wrong, try again")
            elif isinstance(all_res[-1], dict):
                print(f"u can choise one of the keyes from this list\n\
{all_res[-1].keys()}")
                while True:
                    choise = input(">>> ")
                    if choise in all_res[-1].keys():
                        print(json.dumps(all_res[-1][choise], indent=2))
                        all_res.append(all_res[-1][choise])
                        break
                    elif choise == "bye":
                        return print("Bye!)")
                    else:
                        print("oh, something went wrong, try again")
            else:
                print("There is no further continuation\n\
please, write 'back'")
        elif path == "":
            print("pls, write 'path', because i don`t have date to work with")
        elif isinstance(all_res[-1], dict) and part in all_res[-1].keys():
            print(json.dumps(all_res[-1][part], indent=2))
            all_res.append(all_res[-1][part])
        elif part.isnumeric():
            if isinstance(all_res[-1], list) and 0 <= int(part) <= len(all_res[-1]):
                print(json.dumps(all_res[-1][int(part)], indent=2))
                all_res.append(all_res[-1][int(part)])
            else:
                print("oh, I don't understand you, try again")
        else:
            print("oh, I don't understand you, try again")

main()
# /mnt/d/labs/2half/lab2.programming/twitter2.json
