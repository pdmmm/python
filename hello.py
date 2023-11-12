import sys
if len(sys.argv) > 1:
    first_arg = sys.argv[1]
    try:
        first_arg = int(first_arg)
        if int(first_arg) > 4:
            print ("hello")
        else:
            print ("goodbye")
    except ValueError:
        print("value must be an integer")
else:
    print("Usage: python hello.py <integer>")