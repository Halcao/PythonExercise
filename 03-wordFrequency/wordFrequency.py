import sys


content = []
def initialize(str):
    n = 1
    while n < len(str):
        if ((str[n] >= 'a' and str[n] <= 'z') or (str[n] >= 'A' and str[n] <= 'Z')) :
            print "ies"
count = []
def main():
    print sys.argv
    f = open(sys.argv[1], 'r')
    content = f.read(-1).replace('\n', ' ')
    content.replace(',', ' ')
    content.replace('.', ' ')
    content.replace(',', ' ')
    content.replace('"', ' ')
    content.replace("'", ' ')
    content = content.split(' ')
    #print content
    for word in content:
        n = 0
        for word2 in content:
            if word == word2:
                n += 1
                content.remove(word2)
        count.append(n)
        print word + ": " + str(n)

if __name__ == '__main__':
    main()

