from math import log, exp, pow
# needs Dew Point: https://en.wikipedia.org/wiki/Dew_point#Calculating_the_dew_point
# needs Humidex: 

a = 6.112
b = 17.67
c = 243.5

def humidex(temperature, humidity):
    dewpt = dewpoint(temperature, humidity)
    humidex = temperature + 0.5555 * (6.11 * exp(5417.7530 * ( 1/273.16 - 1/(273.16+dewpt) )) - 10)
    return humidex

# not working! 
def dewpoint2(temperature, humidity):
    dewpoint = log(humidity/100) + ((b*temperature)/(c + temperature))
    return dewpoint


def dewpoint(temperature, humidity):
    dewpoint = ((humidity/100)**(1/8)) * (112 + 0.9*temperature) + (0.1 * temperature) - 112
    return dewpoint
