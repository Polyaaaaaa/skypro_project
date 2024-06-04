import re

lst = [
    "Номер телефона: +7 (123) 456-7890",
    "Телефон: 123-456-7890",
    "Мобильный: +7 987 654 32 10",
    "Еще один номер: (555) 123-4567"
]
pattern = re.compile(r"\+?[\d\s()-]+")
phone_numbers = []
for item in lst:
    list_ = re.findall(pattern, item)
    for element in list_:
        if element == " ":
            continue
        else:
            phone_numbers.append(element)


print(phone_numbers)