import numpy as np
from visual import call_payoff
from database import compounds

def lower_c(strike, underlying, r, comp, T, plot = True):

    if not isinstance(strike, (int, float)):
            raise TypeError("Strike needs to be number")

    if not isinstance(underlying, (int, float)):
            raise TypeError("Underlying needs to be a number")

    if not isinstance(r, (int, float)):
                raise TypeError("r needs to be a number")

    if not isinstance(T, (int, float)):
                raise TypeError("T Needs to be a number")

    if not isinstance(comp, str):
                raise TypeError("comp needs to be one of d, m, y")
    
    if not isinstance(plot, bool):
        raise TypeError("Needs to be True or False")

    # i = 0
    
    # for x in args:
    #     i += 1
    #     if not x:
    #         raise ValueError(f"No value for {args[i]} ")
    # i = 0

    if comp not in compounds:
           raise ValueError ("Unknown compounding period entered, choose between", compounds)

    price = underlying - strike * (1 +r/(compounds[comp]))**(-T*(compounds[comp]))
    print(f"{price:.2f}")

    if plot == True:
        call_payoff(strike)

def lower_p(strike, underlying, r, comp, T, plot = True):

    if not isinstance(strike, (int, float)):
            raise TypeError("Strike needs to be number")

    if not isinstance(underlying, (int, float)):
            raise TypeError("Underlying needs to be a number")

    if not isinstance(r, (int, float)):
                raise TypeError("r needs to be a number")

    if not isinstance(T, (int, float)):
                raise TypeError("T Needs to be a number")

    if not isinstance(comp, str):
                raise TypeError("comp needs to be one of d, m, y")
    
    if not isinstance(plot, bool):
        raise TypeError("Needs to be True or False")

    # i = 0
    
    # for x in args:
    #     i += 1
    #     if not x:
    #         raise ValueError(f"No value for {args[i]} ")
    # i = 0

    if comp not in compounds:
           raise ValueError ("Unknown compounding period entered, choose between", compounds)

    price = strike * (1 +r/(compounds[comp]))**(-T*(compounds[comp])) - underlying
    print(f"{price:.2f}")

    if plot == True:
        call_payoff(strike)

lower_c(95,100,0.05,"y",1, False)

lower_p(110,100,0.05,"y",1, False)