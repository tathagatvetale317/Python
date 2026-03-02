def print_words_by_length(filename, length):
    file = open("Tathagat.txt","r")
    text = file.read()
    file.close()
    words = text.split()
    print(f"Words of length {length}:")
    for word in words:
        if len(word) == length:
            print(word)
# User input 
fname = input("Enter file name: ")
l = int(input("Enter word length: "))
print_words_by_length(fname,l)
