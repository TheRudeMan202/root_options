import numpy as np
from visual import call_payoff, put_payoff
from database import compounds

def lower_c(strike, underlying, r, comp, T, plot = True):

    """
    Takes in the strike price, price of the underlying, interest rate
    compounding frequency in 4 options (check database.py for more info),
    time periods in years and will also plot the payoffs

    Prices the lower bound of a call option

    Raises type errors if the the inputted values are of the wrong type

    Raises Value errors for the strings that need to be inputted as these
    are double checked against a dictionary of set options
    """

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

    if comp not in compounds:
           raise ValueError ("Unknown compounding period entered, choose between", compounds)

    price = underlying - strike * (1 +r/(compounds[comp]))**(-T*(compounds[comp]))
    print(f"{price:.2f}")

    if plot == True:
        call_payoff(strike)

def lower_p(strike, underlying, r, comp, T, plot = True):

    """
    Identical to the code above except used to price the lower bound of a put
    """
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

    if comp not in compounds:
           raise ValueError ("Unknown compounding period entered, choose between", compounds)

    price = strike * (1 +r/(compounds[comp]))**(-T*(compounds[comp])) - underlying
    print(f"{price:.2f}")

    if plot == True:
        put_payoff(strike)
