#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Səhv burada idi: 'value' əvəzinə 'my_list[i]' yazmalısan
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Yalnız tip xətalarını tuturuq (stringləri keçmək üçün)
            pass

    print("")  # Dövr bitəndə yeni sətir
    return count
