#Importing the Required Libraries and Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

#Importing the Necessary Data
google_csv=pd.read_csv("Revenue\Google 2012-20.csv")
yahoo_csv=pd.read_csv("Revenue\Yahoo 2012-20.csv")
netflix_csv=pd.read_csv("Revenue\wNetflix 2012-20.csv")

#Imported Data (Run these Codes only to check if working or not)
#print(google_csv)
#print(yahoo_csv)
#print(netflix_csv)

#Defining a Dictionary for the Years specified in DataFrames
id_dict={2012:0,2013:1,2014:2,2015:3,2016:4,2017:5,2018:6,2019:7}

#Getting Input from User
Start_Year=int(input("Choose an Year (between 2012-2019): "))
End_Year=int(input("Choose an Year (between 2012-2019): "))

#Applying the Input Command on the Dictionary
x_start=int(id_dict[Start_Year])
x_end=int(id_dict[End_Year])+1

#Creating New DataFrames based on User input
mod_gcsv=google_csv[x_start:x_end]
mod_ycsv=yahoo_csv[x_start:x_end]
mod_ncsv=netflix_csv[x_start:x_end]

#numpy.genfromtxt ~ 
#Function of the Code: The set of functions that convert the data of a column to a value.
google_data=np.genfromtxt("Revenue\Google 2012-20.csv",delimiter=",",names=["x", "y"])
yahoo_data=np.genfromtxt("Revenue\Yahoo 2012-20.csv",delimiter=",",names=["x", "y"])
netflix_data=np.genfromtxt("Revenue\wNetflix 2012-20.csv",delimiter=",",names=["x", "y"])

#Creating Patches to Use in Legends
#Why? Because these datas do not have any predefined handles or labels. The Patches are what allow to Create Handles in Legends for easier understanding of the Graph
google_patch=mpatches.Patch(color="blue",label="Google")
nflx_patch=mpatches.Patch(color="green",label="Netflix")
yahoo_patch=mpatches.Patch(color="orange",label="Yahoo")

#Plotting Graph Based on Original Data
plt.suptitle('Revenue over Years Graph')
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.subplot(2,1,1)
plt.title('Overall Graph')
plt.plot(google_csv['Year'],google_csv['Revenue'],yahoo_csv['Year'],yahoo_csv['Revenue'],netflix_csv['Year'],netflix_csv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])

#Plotting Graph Based on User Request
plt.subplot(2,1,2)
plt.title('Graph Based on User Request')
print('Displaying the full graph and a Graph between ',Start_Year,'and ',End_Year)
plt.plot(mod_gcsv['Year'],mod_gcsv['Revenue'],mod_ycsv['Year'],mod_ycsv['Revenue'],mod_ncsv['Year'],mod_ncsv['Revenue'])
plt.xlabel("Years")
plt.ylabel("Revenue")
plt.legend(handles=[google_patch,yahoo_patch,nflx_patch])
plt.show()
