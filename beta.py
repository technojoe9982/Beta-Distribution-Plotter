#importing the right libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import PySimpleGUI as sg


'''
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
With probability density, the area underneath the graph is probability. It is a mass of probability almost
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
'''


#importing methods used for popping up the second windows
from explan1 import explanation1
from explan2 import explanation2


#setting the style for the plot
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = (12, 8)

#setting up two subplots in matplotlib 
fig, axs = plt.subplots(2)
fig.suptitle('Probability and Cumulative Probability Density')
axs[0].set_ylabel('Probability Denisty')
axs[0].set_xlabel('Probability')
axs[1].set_ylabel('Cumulative Probability')
axs[1].set_xlabel('Probability')


def calculate_mean(a, b):
    #this function calculates the mean for the probability density function
    average = ss.beta.mean(a, b)

    _average = str(average)

    window1['MEAN'].update(_average)

def calculate_std(a, b):
    #a function to calculate standard deviation
    std = ss.beta.std(a, b)
    _std = str(std)

    window1['STD'].update(_std)


def calculate_prob(xmin, xmax, a, b):
    #the function which calulates the pobability of a probability lying between two values of probability

    ymax = ss.beta.cdf(xmax, a, b)
    ymin = ss.beta.cdf(xmin, a, b)

    prob = ymax - ymin

    window1['PROBABILITY'].update(str(prob))

def plot_pdf(x_range, a, b, **kwargs):
    #this is a function which plots the beta probability desnity function

    #axises are cleared so when you want to draw a plot with new values you don't have multiple lines
    axs[0].cla()
    #here we plot text which shows the outcomes which are being plotted, done for clarity
    goodOutcomes = "Good outcomes: " + str(a-1)
    badOutcomes = "Bad outcomes: " + str(b-1)
    axs[0].text(0.01, 0.95, goodOutcomes, transform=axs[0].transAxes, fontsize=10)
    axs[0].text(0.01, 0.87, badOutcomes, transform=axs[0].transAxes, fontsize=10)

    #labels are re-wrriten as the axis have just been cleared
    axs[0].set_ylabel('Probability Density')
    axs[0].set_xlabel('Probability')
    x = x_range
    #array of y values are calculated using the betapdf function
    y = ss.beta.pdf(x, a, b)
    #plotting the array of x and y values, takes in extra arguements so it's easy to adjust properties of the line
    axs[0].plot(x, y, **kwargs)
    plt.show()

def plot_cdf(x_range, a, b, **kwargs):
    #this function plots the cumulative distribution
    #this function is also used to calculate the probability of the probability lying between two probabilities

    #axises are cleared so when you want to draw a plot with new values you don't have too many lines
    axs[1].cla()
    #again we are putting text to show the number of outcomes for clarity
    goodoutcomes = "Good outcomes: " + str(a-1)
    badoutcomes = "Bad outcomes: " + str(b-1)
    axs[1].text(0.01, 0.95, goodoutcomes, transform=axs[1].transAxes, fontsize=10)
    axs[1].text(0.01, 0.87, badoutcomes, transform=axs[1].transAxes, fontsize=10)
    #labels are redrawn on the axises after clearing
    axs[1].set_ylabel('Cumulative Probability')
    axs[1].set_xlabel('Probability')

    x = x_range
    y = ss.beta.cdf(x, a, b)
    #array of values are calculated and plotted 
    axs[1].plot(x, y, **kwargs)
    plt.show()

def checkIntadd1(i):
    #this function is designed to check if the input is an integer
    #it is used for the outcome inputs
    try:
        int(i)

    except ValueError:
        window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')
        #if it is not an integer it will return a negative number which will not pass through the if statements which are used
        #to check if the inputs are positive integers
        no = -1
        return no
    


    yes = int(i)+1
    #1 is added here to because our shape parameters need 1 added from the good and bad outcomes
    
    return yes
def checkFloat(f):
    #this function ensures floats are entered for the range
    try:
        float(f)
    except ValueError:
        window1['Error2'].update('ERROR: Please enter a value for range between 0 and 1')

        no = -1
        # a negative number again will not pass through the if statements so it is returned if it is not a float
        return no

    yes = float(f)
    return yes
#setting up an x axis with an array of 5 000 values between 0 and 1

x = np.linspace(0, 1, 5000)

#setting up the gui with pysimplegui
layout1 = [
    [sg.Text('This program is designed to calculate and show where the probability of a situation happening is likely to')],
    [sg.Text('lie when only a limited sample of data is available. It can calculate the mean and standard deviation')],
    [sg.Text(' of this distribution; as well it can calculate the likelihood of the probability lying between')],
    [sg.Text('two values of probability. An example for a use of this is if you are a company and have made')],
    [sg.Text('a small sample of a product and a proportion of the sample has come out faulty and you want to')],
    [sg.Text("know how certain you can be that the next products will or won't come out faulty.")],
    [sg.Text('The program uses the beta function for the probability density and cumulative probability functions.')],
    [sg.Text('PDF = Probability Denisty Function'), sg.Button('PDF Formula')],
    [sg.Text('CDF = Cumulative Distribution Funciton'), sg.Button('CDF Formula')],
    [sg.Text('How many results came back how you wanted them?', font=('Helvetica', 15))],
    [sg.Text('Good outcomes', size =(15, 1)), sg.InputText()],
    [sg.Text('Bad outcomes', size =(15, 1)), sg.InputText()],
    [sg.Text('To calculate a probability lying inbetween a range, enter values here between 0 and 1', font=('Helvetica', 13))],
    [sg.Text('Minimum Probability', size =(15, 1)), sg.InputText()],
    [sg.Text('Maximum Probability', size =(15, 1)), sg.InputText()],
    [sg.Button('Calculate Standard Deviation', size =(30, 1)), sg.Button('Plot PDF', size =(30, 1))],
    [sg.Button('Calculate Mean', size =(30, 1)), sg.Button('Plot CDF', size =(30, 1))],
    [sg.Button('Calculate Probability in a range', size =(30, 1)), sg.Cancel(size =(30, 1))],
    [sg.Text('Mean: '), sg.Text('  ', size =(40, 1), key='MEAN')],
    [sg.Text('Standard deviation: '), sg.Text('  ', size =(40, 1), key='STD')],
    [sg.Text('Probability in a range: '), sg.Text('  ', size =(40, 1), key='PROBABILITY')],
    [sg.Text(''), sg.Text('  ', size =(50, 1), key='Error1')],
    [sg.Text(''), sg.Text('  ', size =(50, 1), key='Error2')]

]

window1 = sg.Window('Probability Densities', layout1)


while True:
    #this while function is used for when the buttons are clicked in turn running the other functions
    event, values = window1.read()



    if event in (sg.WIN_CLOSED, 'Cancel'):
        #event for closing window
        break



    elif event == 'PDF Formula':
        #this event calls a function from another file which creates a new window which displays an image with all the maths for the pdf
        explanation1()

    elif event == 'CDF Formula':
        #this event calls a function from another file which creates a new window which displays an image with all the maths for the cdf

        explanation2()
    elif event == 'Plot PDF':
        #this event is when the plot pdf button is clicked and runs the values through the int checking functions
        favourable_outcomes = int(checkIntadd1(values[0]))
        unfavourable_outcomes = int(checkIntadd1(values[1]))

        if(unfavourable_outcomes > 0 and favourable_outcomes > 0):
            #this if statements ensures the values going into the function are positive which they must be
            #the function to plot the probability density function is called
            plot_pdf(x, favourable_outcomes, unfavourable_outcomes,  color='red', lw=2, ls='-', alpha=0.7)
            window1['Error1'].update(' ')
        else:
            #error message incase the values are negative
            window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')

    elif event == 'Plot CDF':
        #this event is when the plot cdf button is clicked and runs the values through the int checking functions

        favourable_outcomes = int(checkIntadd1(values[0]))
        unfavourable_outcomes = int(checkIntadd1(values[1]))

        if(unfavourable_outcomes >=0 and favourable_outcomes >=0):
            #this if statements ensures the values going into the function are positive which they must be

            plot_cdf(x, favourable_outcomes, unfavourable_outcomes,  color='green', lw=2, ls='-', alpha=0.7)
            window1['Error1'].update(' ')
        else:
            window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')

    elif event == 'Calculate Probability in a range':
        #this event checks for int and float values as appropriate and calls the function to calculate probability
        favourable_outcomes = int(checkIntadd1(values[0]))
        unfavourable_outcomes = int(checkIntadd1(values[1]))
        minProb = float(checkFloat(values[2]))
        maxProb = float(checkFloat(values[3]))

        if(favourable_outcomes >=0 and unfavourable_outcomes >=0 and
           minProb >= 0 and minProb <= 1
          and maxProb >= 0 and maxProb <= 1):
            #if statement which is checking that the good and bad outcomes are postiive and the values for the range lie between 0 and 1
            calculate_prob(minProb, maxProb, favourable_outcomes, unfavourable_outcomes)
            window1['Error1'].update(' ')
            window1['Error2'].update(' ')
            #The error windows are emptied in the case there is no error 
        else:
            window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')
            window1['Error2'].update('ERROR: Please enter a value for range between 0 and 1')

    elif event == 'Calculate Mean':
        #this event checks for ints and also runs the function to calculate the mean
        favourable_outcomes = int(checkIntadd1(values[0]))
        unfavourable_outcomes = int(checkIntadd1(values[1]))

        if(unfavourable_outcomes > 0 and favourable_outcomes > 0):

            calculate_mean(favourable_outcomes, unfavourable_outcomes)
            window1['Error1'].update(' ')
        else:
            window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')

    elif event == 'Calculate Standard Deviation':
        #this event again checks for ints and calls the function to calculate standard deviation
        favourable_outcomes = int(checkIntadd1(values[0]))
        unfavourable_outcomes = int(checkIntadd1(values[1]))

        if(unfavourable_outcomes > 0 and favourable_outcomes > 0):
            window1['Error1'].update(' ')
            calculate_std(favourable_outcomes, unfavourable_outcomes)
        else:
            window1['Error1'].update('ERROR: Please enter a positive integer for the outcomes')



window1.close()
