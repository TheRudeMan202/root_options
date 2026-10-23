#Option_price

`Option_price` is a package to find the lower bound of a put or call option,it
also plots the  payoff diagram of this option but the user can choose whether or not they want this included

There are two main functions:

`lower_c()` for call
`lower_p()` for puts

both pricing functions require the same inputs

```python
lower_p(strike, underlying, r, comp, T, plot = True)
```

`strike` and `underlying` need to be numbers (float or int)

`r` is the risk free interest rate with which the option will be priced by, also needs to be a number

`comp` is the compounding rate but the input needs to be one of the following: 
"d" - this is daily and will divide by 365
"m" - this is monthly and will divide by 12
"bi" - this is bi-annual and will divide by 2
"y" - this is yearly and is not compounded

`T` is the time period in years, this needs to be a a number as well, do not calculate the compounded periods yourself i.e. if it is semi annual over 2 years T = 2 not 4

`plot` is whether o\r not the payoff diagram is to be plotted alongside, if no input is entered for this it is assumed to be true and will be plotted


Installation 
```sh
pip install -e .
```

```python
import matplotlib.pyplot as plt
from visual import call_payoff, put_payoff
from database import compounds

```

```sh
python demo/demo01.py
```