#!/usr/bin/python3
"""Miras alma yoxlanılması modulu"""


def inherits_from(obj, a_class):
    """Obyektin verilmiş sinifdən (birbaşa və ya dolayısı ilə)
    miras alıb-almadığını yoxlayır.

    Args:
        obj (any): Yoxlanılacaq obyekt.
        a_class (type): Müqayisə ediləcək sinif.

    Returns:
        True əgər obyekt mirasçıdırsa və özü deyilsə; əks halda False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
