# modules
import sys
import os
import getpass
import platform
from time import sleep

if platform.system() == "Darwin":
    print("Darwin")

# Displays supported OS names
print("Supported OS: Windows, MacOS, Linux, RaspberryPi")

while True:
    # lets user type in a sort of device
    text = str(input("Operating System Name: "))

    # if the user types in MacOS
    if text == "MacOS":
        # if the platform system is Darwin
        if platform.system() != "Darwin":
            print("Error: System is required to be Darwin.")
        # otherwise
        else:
            print("\u001b[32;1mOS: \u001b[0m" + text)
            print("\u001b[32;1mUser: \u001b[0m" + getpass.getuser())
            while True:
                # loading animation
                anim = "-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\"
                for l in anim:
                    # outputs a bouncing dash icon
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sys.stdout.write('\b')
                    sleep(0.2)
                os.system("mkdir vdk")
                os.system("mkdir vdk/lib")
                f = open("vdk/INFO.txt", "w+")
                # writes the username and system in the file
                f.write("Username: " + getpass.getuser() + " System Name: " + platform.system())
                f.close()

                # project thing
                project = open("vdk/main.cpp", "w+")
                project.write("""#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
""")
                project.close()

                # debug file
                run = open("vdk/debug.py", "w+")
                run.write("""import os

os.system("g++ main.cpp")
os.system("./a.out")""")

                # exit the interpreter
                exit()
            break
    # if the user types in Windows
    elif text == "Windows":
        # the operating ystem name isn't nt
        if os.name != "nt":
            print("Error: Operating System name is required to be nt.")
        # otherwise
        else:

            print("\u001b[32;1mOS: \u001b[0m" + text)
            print("\u001b[32;1mUser: \u001b[0m" + getpass.getuser())
            while True:
                anim = "-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\"
                for l in anim:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sys.stdout.write('\b')
                    sleep(0.2)
                os.system("mkdir vdk")
                os.system("mkdir vdk/lib")
                f = open("vdk/INFO.txt", "w+")
                # writes the username and system in the file
                f.write("Username: " + getpass.getuser() +
                        " System Name: " + platform.system())
                f.close()

                # project thing
                project = open("vdk/main.cpp", "w+")
                project.write("""#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
""")
                project.close()

                # debug file
                run = open("vdk/debug.py", "w+")
                run.write("""import os

os.system("g++ main.cpp")
os.system("./a.out")""")
                exit()
    # if the user types in Linux
    elif text == "Linux":
        # if the platform system is Linux
        if platform.system() != "'Linux'":
            print("Error: System name is required to be Linux.")
        else:
            print("\u001b[32;1mOS: \u001b[0m" + text)
            print("\u001b[32;1mUser: \u001b[0m" + getpass.getuser())
            while True:
                anim = "-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\"
                for l in anim:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sys.stdout.write('\b')
                    sleep(0.2)
                os.system("mkdir vdk")
                os.system("mkdir vdk/lib")
                f = open("vdk/INFO.txt", "w+")
                # writes the username and system in the file
                f.write("Username: " + getpass.getuser() +
                        " System Name: " + platform.system())
                f.close()

                # project thing
                project = open("vdk/main.cpp", "w+")
                project.write("""#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
""")
                project.close()

                # debug file
                run = open("vdk/debug.py", "w+")
                run.write("""import os

os.system("g++ main.cpp")
os.system("./a.out")""")
                exit()
    elif text == "RaspberryPi":
        # if the platform system is Ubuntu
        if platform.system() != "'Linux'":
            print("Error: System name is required to be Linux.")
        else:
            print("\u001b[32;1mOS: \u001b[0m" + text)
            print("\u001b[32;1mUser: \u001b[0m" + getpass.getuser())
            while True:
                anim = "-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\-_/\\"
                for l in anim:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    sys.stdout.write('\b')
                    sleep(0.2)
                os.system("mkdir vdk")
                os.system("mkdir vdk/lib")
                f = open("vdk/INFO.txt", "w+")
                # writes the username and system in the file
                f.write("Username: " + getpass.getuser() +
                        " System Name: " + platform.system())
                f.close()

                # project thing
                project = open("vdk/main.cpp", "w+")
                project.write("""#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}
""")
                project.close()

                # debug file
                run = open("vdk/debug.py", "w+")
                run.write("""import os

os.system("g++ main.cpp")
os.system("./a.out")""")
                exit()
    # if the user doesn't type in the right device
    else:
        print("Error: No such device")
        
