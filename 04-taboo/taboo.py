
def main():
    filtered = open('./filtered_words.txt', 'r').read()
    word = ''
    while word != '#':
        word = ''
        word = raw_input("Please input your word: ")
        if word in filtered:
            print "Freedom"
        else:
            print "Human right"

if __name__ == '__main__':
    main()
