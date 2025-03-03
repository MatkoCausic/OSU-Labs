# 1. zadatak
# euroPerHour = 8.5

# working_hours = int(input())

# total_euro = euroPerHour * working_hours

# print(f"Plata jest: ", total_euro)

# 2. zadatak
# def fun():
#     if percent >= 0.9:
#         print("A")
#     elif percent >= 0.8:
#         print("B")
#     elif percent >= 0.7:
#         print("C")
#     elif percent >= 0.6:
#         print("D")
#     elif percent <0.6:
#         print("F")
#     else:
#         print("Not right number")

# try:
#     percent = float(input())
#     if 0.0 <= percent <= 1:
#         fun()
#     else:
#         print("Not right number")
# except ValueError:
#     print("Input is not float.")

# 3. zadatak

# def fun():
#     list = []
#     while(True):
#         user_input = input()
#         if user_input == "Done":
#             break
#         elif user_input >= "a" & user_input <= "z" | user_input >= "A" & user_input <= "Z":

#         else:
#             user_input = int(user_input)
#             list.append(user_input)
    
#     print(len(list),sum(list)/len(list),min(list),max(list))
#     print(list.sort())
#     return

# fun()

# 5. zadatak

spam_words = 0
ham_words = 0
file = "SMSSpamCollection.txt"

with open(file, "r",encoding="UTF-8"):
    for line in file:
        messageType,content = line.strip().split("\t", 1)
        if messageType == "spam":
            spam_words += content.split().count()
        else:
            ham_words += content.split().count()

    print(ham_words)
    print(spam_words)
