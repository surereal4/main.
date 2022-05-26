# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(fileName):
    # [assignment] Add your code here 
    file = open(fileName, "r")
    for line in file:
        words = line.split()
        return words
print(read_file_content("story.txt"))

def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    count = len(text)
    print("Numbers of words in the texts of the file: ", count)
count_words()