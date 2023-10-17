file_1 = "F1.txt"
with open(file_1,"w") as file:
    while True:
        user_input = input("Введите строку: ")
        if user_input:
            file.write(user_input+ "\n")
        else:
            break

file_2 ="F2.txt"
with open(file_1, "r") as file, open(file_2,"w") as file2:
    for line in file:
        words=line.split()
        if len(words)==1:
            file2.write(line)

short_word = None
with open(file_2,"r") as file2:
    for line in file2:
        word=line.strip()
        if short_word is None or len(word)<len(short_word):
            short_word=word
if short_word:
    print("Самое короткое слово: ", short_word)
else:
    print ("Файл пустой")
