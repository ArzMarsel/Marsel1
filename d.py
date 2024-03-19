listofwords = []

def func(word_list):
    for word in word_list:
        print(len(word))


while True:
    listofwords.append(input('Введите слово'))
    print(listofwords[-1])
    if listofwords[-1].isdigit():
        func(listofwords)
        break
