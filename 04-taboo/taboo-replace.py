#-*- coding: utf-8 -*-

def main():
    filtered = open('./filtered_words.txt', 'r').readlines()
    print filtered
    sentence = ''
    while sentence != '#':
        sentence = ''
        sentence = raw_input("Please input your word: ")
        for word in filtered:
            if sentence.count(word.replace('\n', '')) > 0: 
                print sentence.replace(word.replace('\n', ''), "和谐社会")
                break
        else:
            print sentence

if __name__ == '__main__':
    main()
