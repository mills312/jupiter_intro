
def main():
    try:
        open("config.txt")
    except FileNotFoundError as err: 
        print("file not found", err)
    except IsADirectoryError:
        print("found file but no permissions")
    except PermissionError as err:
        print("permissions problem: ", err)
    except(BlockingIOError, TimeoutError) as err:
        print("some performance related issue with the system: ", err)

def main2():
    try:
        open("config.txt")
    except OSError as err:
        if err.errno == 2:
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:
            print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()
    main2()
