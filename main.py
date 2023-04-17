# Создаем множества
set_double = set()
set_decimal = set()


def convert_into_set_decimal_from_double(set_double):
    for i in set_double:
        set_decimal.add(int(str(i), base=2))
    return set_decimal


print("Enter letter or digit from 2 to 9 to end.")
while (1):
    print("Input element in binary system.")
    input_value = str(input())
    for i in input_value:
        if i != '1' and i != '0' and i:
            if set_double != set():
                set_decimal = convert_into_set_decimal_from_double(set_double)
                print("Set of binary numbers:\n", *set_double)
                print("Set of decimal numbers:\n", *set_decimal)
            exit()
    if int(input_value) in set_double:
        print("Error. The set already has this element.")
    set_double.add(int(input_value))
