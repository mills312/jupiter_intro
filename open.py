
def main():
    try:
        open("/path/to/mars.jpg")
    except FileNotFoundError: 
        print("file not found")

if __name__ == '__main__':
    main()
