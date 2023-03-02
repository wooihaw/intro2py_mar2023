import sys

ans = input('Do you want to quit?')

if ans in ('y', 'Y', 'yes', 'YES'):
    print("Exiting the program")
    sys.exit(0)
else:
    print("Continue")
    for i in range(10):
        print(i)
