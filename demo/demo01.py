import matplotlib.pyplot as plt
from option_price import lower_c, lower_p



lower_c(95,100, 0.05,"y",1, plot = False)

"""
Choosing not to plot the payoff diagram here but if plot not specified 
then it will be plotted as shown below
"""
lower_p(110,100,0.05,"y",1)
