DATA = [6,20,9,12,8,7,15,31,16]

def main():
    print(min(DATA))
    DATA.remove(min(DATA))
    print(min(DATA))

if __name__ == "__main__":
    main()
