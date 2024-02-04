for number in range(501, 10000):
    octal_number = oct(number)[2:]
    if octal_number[-3:] == '123':
        print("Ответ:", number)
        break