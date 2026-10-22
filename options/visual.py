import numpy as np
import matplotlib.pyplot as plt

def call_payoff(strike):
    """
    This is to plot the payoff matrix of both long and short 
    calls against price of the underlying
    Takes the strike price as the main argument and plots the payoff of both
    long and short options
    """
    
    St = [x for x in range(int(strike*2))]
    fig,(ax1, ax2) = plt.subplots(1,2,figsize = (10,7))
    payoff = [max(0, x - strike) for x in St]
    ax1.plot(St, payoff)
    ax1.set_xlabel("S(t)")
    ax1.set_ylabel("Payoff")
    ax1.set_title("Long call")
    ax1.axvline(x=strike, color='red', linestyle='--')
    
    payoff = [min(0, strike - x) for x in St]
    ax2.plot(St, payoff)
    ax2.set_xlabel("S(t)")
    ax2.set_ylabel("Payoff")
    ax2.set_title("Short call")
    ax2.axvline(x=strike, color='red', linestyle='--')

    fig.tight_layout()
    plt.show()


def put_payoff(strike):
    """
    Same as above put now we can do it for puts instead
    """
    St = [x for x in range(int(strike*2))]
    fig,(ax1, ax2) = plt.subplots(1,2,figsize = (10,7))
    payoff = [max(0, strike - x) for x in St]
    ax1.plot(St, payoff)
    ax1.set_xlabel("S(t)")
    ax1.set_ylabel("Payoff")
    ax1.set_title("Long put")
    ax1.axvline(x=strike, color='red', linestyle='--')
    
    payoff = [min(0, x - strike) for x in St]
    ax2.plot(St, payoff, )
    ax2.set_xlabel("S(t)")
    ax2.set_ylabel("Payoff")
    ax2.set_title("Short put")
    ax2.axvline(x=strike, color='red', linestyle='--')

    fig.tight_layout()
    plt.show()
