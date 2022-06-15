from genericpath import exists
from pick import pick
from colorama import Fore, Back
import shutil
import psutil
import subprocess
import os
import time
import sys

# findprocessbyname

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# startup

os.system('title Loading...')

# menu

def menu():
    os.system('cls')
    os.system('title ServerRunner - made by noex')
    title = f'''Please select what would you like to do: '''
    options = ['Setup a Server', 'Manage Server', 'Back Up','Monitor CPU and RAM usage', 'Get ngrok IP']
    option, index = pick(options, title, indicator='=>', default_index=0)

    if option == 'Setup a Server':
        setup()
    elif option == 'Manage Server':
        manage()
    elif option == 'Get ngrok IP':
        ngrok()
    elif option == 'Back Up':
        backup()
    elif option == 'Monitor CPU and RAM usage':
        monitor()

# backup

def backup():
    os.system('cls')
    next = input(f"{Fore.YELLOW}Coming soon...{Fore.WHITE}")
    menu()


# monitor

def get_cpu_usage_pct():
    return psutil.cpu_percent(interval=0.5)

def get_ram_usage():
    return int(psutil.virtual_memory().total - psutil.virtual_memory().available)

def monitor():
    os.system('cls')
    print(f'{Fore.GREEN}Starting monitoring{Fore.WHITE}')
    if os.path.exists(f'ServerRunner.py'):
        time.sleep(2.5)
        os.system('start ServerRunner.py')
        while True:
            print('This window is now used for monitoring, opened a new ServerRunner\n \nRAM usage is {Fore.}{} MB'.format(int(get_ram_usage() / 1024 / 1024)) + '\nSystem CPU load is {} %'.format(get_cpu_usage_pct()) + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    else:
        print(f'''{Fore.RED}Couldn't find ServerRunner.py{Fore.WHITE}''')
        time.sleep(0.5)
        menu()

special_characters = '''abcdefghijklmnopqrstuvwxyz0123456789-_'''

def setup():
    folder = input(f'''What should be the name of the Server: ''')
    if any(c in special_characters for c in folder):
        os.mkdir(folder)
    else:
        print(f'''{Fore.RED}Invalid character(s).{Fore.WHITE}''')
        setup()

    titletype = f'Select a Server Type: '
    optionstype = ['Vanilla', 'Spigot', 'Paper']
    optiontype, index = pick(optionstype, titletype, indicator='=>', default_index=0)

    if optiontype == "Vanilla":
        title = f'Select a Server Version: '
        options = ['1.7', '1.8', '1.12', '1.16', '1.17', '1.18','1.19']
        option, index = pick(options, title, indicator='=>', default_index=0)

        if option == '1.19':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/e00c4052dac1d59a1188b2aa9d5a87113aaf1122/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        if option == '1.18':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.17':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.16':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.12':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/8494e844e911ea0d63878f64da9dcc21f53a3463/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.8':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.7':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://launcher.mojang.com/v1/objects/c69ebfb84c2577661770371c4accdd5f87b8b21d/server.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        else:
            os.system('cls')
            print(f'''{Fore.RED}Couldn't set up the server{Fore.WHITE}''')
            os.rmdir(folder)
            time.sleep(3)
            menu()

    elif optiontype == "Spigot":
        title = f'Select a Server Version: '
        options = ['1.7', '1.8', '1.12', '1.16', '1.17', '1.18', '1.19']
        option, index = pick(options, title, indicator='=>', default_index=0)

        if option == '1.19':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://download.getbukkit.org/spigot/spigot-1.19.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        if option == '1.18':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://download.getbukkit.org/spigot/spigot-1.18.2.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.17':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://download.getbukkit.org/spigot/spigot-1.17.1.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.16':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.12':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.8':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.7':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://cdn.getbukkit.org/spigot/spigot-1.7.10-SNAPSHOT-b1657.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        else:
            os.system('cls')
            print(f'''{Fore.RED}Couldn't set up the server{Fore.WHITE}''')
            os.rmdir(folder)
            time.sleep(3)
            menu()

    elif optiontype == "Paper":
        title = f'Select a Server Version: '
        options = ['1.8', '1.12', '1.16', '1.17', '1.18', '1.19']
        option, index = pick(options, title, indicator='=>', default_index=0)

        if option == '1.19':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/14/downloads/paper-1.19-14.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        if option == '1.18':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/379/downloads/paper-1.18.2-379.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.17':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.16':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/790/downloads/paper-1.16.5-790.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.12':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1618/downloads/paper-1.12.2-1618.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        elif option == '1.8':
            os.system('cls')
            print(f'{Fore.BLACK}{Back.WHITE}Started downloading the server jar{Back.BLACK}{Fore.WHITE} \n')
            f = open(f"{folder}/eula.txt", "a")
            f.write("eula=true")
            f.close()
            os.system('curl "https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/443/downloads/paper-1.8.8-443.jar" --output ' + folder + '/' + 'server.jar')
            menu()
        else:
            os.system('cls')
            print(f'''{Fore.RED}Couldn't set up the server{Fore.WHITE}''')
            os.rmdir(folder)
            time.sleep(3)
            menu()
    else:
        os.system('cls')
        print(f'''{Fore.RED}Couldn't set up the server{Fore.WHITE}''')
        os.rmdir(folder)
        time.sleep(3)
        menu()

# manage

def manage():
    os.system('cls')
    title = f'What would you like to do: '
    options = ['Start', 'Kill', 'Reset Files', 'Delete Server', 'Go Back']
    option, index = pick(options, title, indicator='=>', default_index=0)
    if option == 'Start':
        os.system('cls')
        d='.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        print('Servers:\n', folders, '\n')
        server = input('Enter folder name: ')
        memory = input('Enter memory (M): ')
        if os.path.isdir(server):
            print(f'''
{Fore.GREEN}------------------ Starting Server ------------------{Fore.WHITE}
''')
            if os.path.exists(f'ServerRunner.py'):
                print('This console is now a server, opened a new ServerRunner')
                os.system('start ServerRunner.py')
            else:
                print(f'''{Fore.RED}Couldn't find ServerRunner.py{Fore.WHITE}''')
                time.sleep(0.5)
                manage()
            os.system(f'cd {server} && java -Xms{memory}M -Xmx{memory}M -jar server.jar nogui')
            exit = input(f'''
{Fore.RED}------------------ Server Closed ------------------{Fore.WHITE}
''')
            manage()
        else:
            os.system('cls')
            back = input(f'''{Fore.RED}Couldn't find server{Fore.WHITE}''')
            manage()

    elif option == 'Go Back':
        menu()
    elif option == 'Reset Files':
        os.system('cls')
        d='.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        print('Servers:\n', folders, '\n')
        folder = input('Enter folder name: ')
        if os.path.exists(folder):
            sure = input(f'''{Back.WHITE}{Fore.BLACK}NOTE{Back.BLACK}{Fore.WHITE} This action will delete all the files generated by the server

    Are you sure you want to reset all the files? (y/n): ''')
            if sure == ('y'):
                if os.path.isdir(f'{folder}/libraries'):
                    shutil.rmtree(f'{folder}/libraries')
                    print(f'{Fore.GREEN}Successfully removed libraries')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.isdir(f'{folder}/logs'):
                    shutil.rmtree(f'{folder}/logs')
                    print(f'{Fore.GREEN}Successfully removed logs')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.isdir(f'{folder}/versions'):
                    shutil.rmtree(f'{folder}/versions')
                    print(f'{Fore.GREEN}Successfully removed versions')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.isdir(f'{folder}/world'):
                    shutil.rmtree(f'{folder}/world')
                    print(f'{Fore.GREEN}Successfully removed nether')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.isdir(f'{folder}/world_nether'):
                    shutil.rmtree(f'{folder}/world_nether')
                    print(f'{Fore.GREEN}Successfully removed end')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.exists(f'{folder}/banned-ips.json'):
                    os.remove(f'{folder}/banned-ips.json')
                    print(f'{Fore.GREEN}Successfully removed banned-ips.json')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.exists(f'{folder}/banned-players.json'):
                    os.remove(f'{folder}/banned-players.json')
                    print(f'{Fore.GREEN}Successfully removed banned-players.json')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.exists(f'{folder}/ops.json'):
                    os.remove(f'{folder}/ops.json')
                    print(f'{Fore.GREEN}Successfully removed ops.json')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.exists(f'{folder}/usercache.json'):
                    os.remove(f'{folder}/usercache.json')
                    print(f'{Fore.GREEN}Successfully removed usercache.json')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                if os.path.exists(f'{folder}/whitelist.json'):
                    os.remove(f'{folder}/whitelist.json')
                    print(f'{Fore.GREEN}Successfully removed whitelist.json{Fore.WHITE}')
                else:
                    print(f"{Fore.RED}The file does not exist{Fore.WHITE}")
                time.sleep(2.5)
                manage()
        else:
            print(f'''{Fore.RED}Couldn't find server{Fore.WHITE}''')
            time.sleep(2.5)
            manage()
    elif option == 'Kill':
        os.system('cls')
        sure = input(f'''{Back.WHITE}{Fore.BLACK}NOTE{Back.BLACK}{Fore.WHITE} This action will kill the server.
Are you sure you want to do it? (y/n): ''')
        if sure == ('y'):
            os.system('cls')
            if checkIfProcessRunning('java.exe'):
                os.system('taskkill /F /IM java.exe')
                print(f'{Fore.GREEN}Successfully killed the server{Fore.WHITE}')
                time.sleep(2.5)
                manage()
        else:
            os.system('cls')
            print(f'''{Fore.RED}Couldn't kill the server{Fore.WHITE}''')
            time.sleep(2.5)
            manage()
        manage()
    elif option == 'Delete Server':
        os.system('cls')
        d='.'
        folders = list(filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d)))
        print('Servers:\n', folders, '\n')
        folder = input('Enter folder name: ')
        if os.path.isdir(folder):
            sure = input(f'''{Back.WHITE}{Fore.BLACK}NOTE{Back.BLACK}{Fore.WHITE} This action will delete every file generated by the server

Are you sure you want to delete your server? (y/n): ''')
            if sure == ('y'):
                os.system('cls')
                if os.path.isdir(f'{folder}'):
                    shutil.rmtree(f'{folder}')
                    print(f'{Fore.GREEN}Successfully removed server: {folder}{Fore.WHITE}')
                    time.sleep(2.5)
                    manage()
            else:
                manage()
        else:
            print(f'''{Fore.RED}Couldn't find server{Fore.WHITE}''')
            time.sleep(2.5)
            manage

# ngrok

def ngrok():
    os.system('cls')
    if os.path.exists(f'ngrok.exe'):
        port = input('Input a port for your server: ')
        os.system(f'start ngrok tcp -region eu {port}')
        menu()
    else:
        os.system('cls')
        wrong = input(f'''{Fore.RED}Couldn't find ngrok.exe
Install it or rename it, you can find every instruction in the readme.md{Fore.WHITE}''')
        menu()

menu()
