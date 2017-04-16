import os

red = '\033[1;31m'
green = '\033[1;32m'
white = '\033[1;37m'
reset = '\033[0m'

abs_dir = os.path.dirname(os.path.abspath(__file__))

print(green+'[*] trying to update cheetah'+reset)
if os.path.exists(os.path.join(abs_dir,'.git')) == True:
    print(green+'[*] the .git directory is existing.'+reset)
    os.chdir(abs_dir)
    print(white+'[^] trying use git pull to update cheetah'+reset)
    try:
        os.system('git pull origin master')
    except Exception as e:
        print(red+'[!] '+str(e)+reset)
        exit(1)
    print(white+'[=] update completed'+reset)
    exit(0)
else:
    print(green+'[*] the .git directory is not existing.'+reset)
    os.chdir(abs_dir)
    print(white+'[^] trying use git clone to clone latest cheetah'+reset)
    try:
        os.system('git clone https://github.com/sunnyelf/cheetah.git')
    except Exception as e:
        print(red+'[!] '+str(e)+reset)
        exit(1)
    print(white+'[=] update completed'+reset)
    exit(0)