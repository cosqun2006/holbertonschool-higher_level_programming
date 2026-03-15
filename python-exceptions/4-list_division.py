#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        div_result = 0
        try:
            # Bölməni yerinə yetirməyə çalışırıq
            div_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except TypeError:
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            # Xəta olsa da, olmasa da nəticəni siyahıya əlavə edirik
            new_list.append(div_result)

    return new_list
