#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # نحاول الوصول إلى العنصر في الفهرس i
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        except IndexError:
            print("Traceback (most recent call last):")
            print("IndexError: list index out of range")
            break
        except TypeError:
            print("wrong type")
            continue
    print()
    return count
