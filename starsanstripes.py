#PIL for image processing
from PIL import Image
#Processes csv's
import pandas as pd
#Math... math
import math

#Base flag with no stars
flag = Image.open("Images/flag.png")

#Want to change the stars into something else? Simply rename the image to "star.png" and put it in the folder "Images"
star = Image.open("Images/star.png")

#Loading data using pandas
data = (pd.read_csv('Data/usstatesdata.csv'))
data_ = data
data = data.to_dict()


#Makes a list of states
states = data['States']

#Stores Statistic Choices
stats = []

index = 1

#Intrustions for Custom Data
print("")
print("Custom Data: ")
print("If you wish to add some custom data, access 'usstatedata.csv' in the 'Data' folder.")
print("If you wish to add more data, simply add an extra column, formated the same as the other columns.")
print("If you wish to add more states, simply add an extra row.")
print("You need to fill in the 'X' and 'Y' criteria along with the statistic you wish to display")
print("Thanks for using this script!")
print("")

#Multiple Choice Question
print("Which statistic do you want the stars to be propotioned to?")
print('')

#Records and Displays choices
for i in data_.columns:
    if i != "States" and i != "X" and i != "Y":
     stats.append((index, i))
     print(str(index), ". ", i)
     index += 1


#User Input
print('')
stat = int(input("Choose Statistic: "))
print('')
print('Try to experiment with the scaling factor until you get the stars to look just right!')
scalingFactor = float(input("Scaling Factor: "))
stat = stats[stat-1][1]

#Contrusts and Pastes stars
for i in states:

    x = (math.sqrt((data[stat][i]))) * scalingFactor
    x = int(x - (x%1)) + 1
    y = x
    newstar = star.resize((x, y), Image.ANTIALIAS)

    x = data['X'][i]-(x/2)
    x = int(x-(x%1)) + 10
    y = data['Y'][i]-(y/2)
    y = int(y-(y%1)) + 10

    flag.paste(newstar,(x, y) , newstar)

print("")
print("Shout out to https://wikitable2csv.ggor.de, if it weren't for this website, I wouldn't be able to extract data from wikipedia")
print("Get data from wikipedia: https://en.wikipedia.org/w/index.php?search=List+of+U.S.+States+and+territories+by&title=Special%3ASearch&go=Go&ns0=1")
print("Chrome Extension that does similar function: https://chrome.google.com/webstore/detail/wiki-table-copier/cegjnpfjgdddnpckhgpfbaiblpbjopjc")
print("Other wikipedia tools: https://en.wikipedia.org/wiki/Wikipedia:Tools")


#Show flag
flag.show()