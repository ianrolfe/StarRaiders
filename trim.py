if __name__ == "__main__":
    f = open("001-112.txt", "r")
    for l in f:
        print l[14:].rstrip()

