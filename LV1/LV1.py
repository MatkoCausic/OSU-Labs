# 1)
# working_hours = float(input("Enter working  hours: "))
# pay_per_hour = float(input("Enter pay-per-hour: "))

# def total_euro(working_hours, pay_per_hour):
#     return working_hours * pay_per_hour

# print(total_euro(working_hours, pay_per_hour))

# 2)
# import math
# try:
#     grade = float(input("Enter a grade: "))
# except:
#     print("Variable grade is NaN")
# else:
#     if grade >= 0.0 and grade < 0.6:
#         print("F")
#     elif grade >= 0.6 and grade < 0.7:
#         print("D")
#     elif grade >= 0.7 and grade < 0.8:
#         print("C")
#     elif grade >= 0.8 and grade < 0.9:
#         print("B")
#     elif grade >= 0.9 and grade <= 1:
#         print("A")
#     else:
#         print("Out of bounds")

# 3)
# numerical_list = []

# while True:
#     user_input = input("Unesite broj ili 'Done' za kraj: ")
#     if user_input.lower() == "done":
#         break
#     try:
#         number = float(user_input)
#         numerical_list.append(number)
#     except ValueError:
#         print("Pogrešan unos! Molimo unesite broj.")

# if len(numerical_list) == 0:
#     print("Niste unijeli ni jedan broj.")
# else:
#     count = len(numerical_list)
#     average = sum(numerical_list) / count
#     minimum = min(numerical_list)
#     maximum = max(numerical_list)

#     print(f"\nBroj unesenih brojeva: {count}")
#     print(f"Srednja vrijednost: {average}")
#     print(f"Minimalna vrijednost: {minimum}")
#     print(f"Maksimalna vrijednost: {maximum}")

#     numerical_list.sort()
#     print(f"Sortirana lista: {numerical_list}")

# 4)
# import re
# with open("LV1\song.txt", "r") as file:
#     song = file.read()

# song = re.split(r'[ ,\n]+',song)
# dictionary = {}

# for x in song:
#     x = x.lower()
#     if x not in dictionary:
#         dictionary[x] = 1
#     else:
#         dictionary[x] += 1

# print(dictionary)

# 5)
spam_word_counter = 0
ham_word_counter = 0
spam_counter = 0
ham_counter = 0
spam_with_exclamation = 0

with open("LV1/SMSSpamCollection.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if line.startswith("ham\t"):
            message = line.split("\t", 1)[1]
            words = message.split()
            ham_word_counter += len(words)
            ham_counter += 1
        elif line.startswith("spam\t"):
            message = line.split("\t", 1)[1]
            words = message.split()
            spam_word_counter += len(words)
            spam_counter += 1
            if message.endswith("!"):
                spam_with_exclamation += 1

avg_ham = ham_word_counter / ham_counter if ham_counter else 0
avg_spam = spam_word_counter / spam_counter if spam_counter else 0

print(f"Prosječan broj riječi u ham porukama: {avg_ham:.2f}")
print(f"Prosječan broj riječi u spam porukama: {avg_spam:.2f}")
print(f"Broj spam poruka koje završavaju uskličnikom: {spam_with_exclamation}")