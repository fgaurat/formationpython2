# -*- coding: utf-8 -*-


def the_function(*params_val,k1="val k1",k2="val k2",**toto):
    """
    the_function fait des trucs
    """
    print(k1)
    print(params_val)
    print(toto)


the_function(val=1)
the_function(1,2,valtoto=123)


print(the_function.__doc__)