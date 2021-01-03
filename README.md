# Beta-Distribution-Plotter
This is a an application which plots a beta probability density for probability. It can calculate the probability of a range of probabilities


This program is designed to plot the probability density function for a situation
in which there is limited data which can either be good or bad. This function can show
where the probability is most likely to lie but also how certain of it lying there you can be.
It can also calculate the mean and standartd deviation of this distribution. 
Another feature, is the ability to plot the cumulative probabiltiy for this situation.
From this you can calculate the likelihood of the probability of the outcome lying
within a certain range of probabilities.
Points to note:

-Probability density is an alternative to plotting probability as the probability of
a probability being any one value will always be 0, this is the nature of a continuous variable.
With probability density, the area underneath the graph is probability. It is a mass of probability in a sense

-Cumulative Probability is the integral of the probability denisty funciton
and shows the summed likelyhood of the probability being any one of the previous probabilities

-Laplace's rule of succesion has been used to calculate the mean which is also the expected
probability of getting a good outcome from the next trial

-The shape parameters are 1 less than the good and bad outcomes therefore 1 is added to both

-The range is used to calculate the probability of a probability lying between
two values of probability, it takes the maximum value for cumulative probability
and subtracts the minimum

-Error checking functions have been included to ensure only positive integer values
or float values (for the range between 0 and 1) have been used for inputs

-To use this program make sure you have numpy, matplotlib, scipy and pysimplegui installed

https://numpy.org/install/

https://matplotlib.org/users/installing.html#id8

https://www.scipy.org/install.html

https://pysimplegui.readthedocs.io/en/latest/

Written by Joe Parker
Edited Last 03/01/21
