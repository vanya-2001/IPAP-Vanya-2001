# Управление циклом break (безусловный выход из цикла) и continue (пропуск конкретной итерации на этом шаге)
# for x in range(5):
#     if x == 4:
#          break
#
#     print(x)
# else:
#     print("Done")


string = "Во сколько буквей!"

for letter in string:
    if letter == " ":
        continue
    print(letter, end="")
string = "Во сколько 2буквей!"
for letter in string:
    if letter == "2":
        break
    print(letter, end="")