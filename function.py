def countWordsFromFile():
    fileName = input("enter the file name: - ")
    numberOfWords = 0
    file = open(fileName, 'r')
    for line in file:
        words = line.split()
        numberOfWords + len(words)
        print("number of words: ")
        print(numberOfWords)



        countWordsFromFile(
            
        )