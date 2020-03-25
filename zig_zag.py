import sys,time
indent = 0
try:
    while True:
        if indent <=3:
            print(' '*indent, '******')
            indent = indent + 1
            time.sleep(0.1)
        elif indent > 3:
            for i in range(4):
                indent = indent - 1
                print(' '*indent, '******')
                time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()
        