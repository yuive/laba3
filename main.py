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

dest = input("Введите пункт назначения: ")
print(f"Поезда с пунктом назначения {dest}:")
file_3 = "Вокзал.txt"
with open(file_3,"r", encoding="utf-8") as file3:
    for line in file3:
        info=line.split()
        if info[1]== dest:
            print(" ".join(info))

price = 50
print(f"Поезда с ценой билета меньше {price}:")
file_3 = "Вокзал.txt"
with open(file_3,"r", encoding="utf-8") as file3:
    for line in file3:
        price_info=line.split()
        if int(price_info[4]) < price:
            print(" ".join(price_info))

file_4 = "Пары.txt"
lessons = {}

with open(file_4, "r", encoding="utf-8") as file4:
    for line in file4:
        parts = line.strip().split(": ")
        subject = parts[0]
        lessons_info = parts[1].split(" ")

        total_lessons = 0
        for lesson_info in lessons_info:
            count, lesson_type = lesson_info.strip("()").split("(")
            total_lessons += int(count)

        lessons[subject] = total_lessons

print(lessons)