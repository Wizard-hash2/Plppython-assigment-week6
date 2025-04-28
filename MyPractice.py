import math
import random #Import some random functionalities from the random
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as Mpd

def mat():
 print(math.sqrt(4))

 print(f"The random numbers from 1 - 10 is ", random.randint(1,10))
 print(f"The random choice is the ", random.choice(['Apple','Food','Getas']))
 today = datetime.date.today()
 print(today)

def NumP():
 MyArr= np.array([1,2,3,7,4]) 
 print(MyArr * 3)
 print(MyArr.max())

def Panda():
 data = {'Names' : ['Aron', 'Ngeno', 'Kipkurui'],
         'Age': [12,24,36],
         'Location': ['Kenya', 'Kiambu','Nakuru'],
         'SideHustle': ['Writer','Trader', 'Learneer']}
 df = pd.DataFrame(data)
 #print('Names:', df[df['Names'] == 'Aron'])

 print(df)
 print('Names:', df[df['Age'] > 20])
 Mpd.bar(df['Location'], df['Names'])
 Mpd.show()

def matro():
 x = [1,2,3,4,5]
 y = [10,20,30,40,50]
 #Mpd.plot(x,y) # for line chart
 Name = ['Aron','Ngenp']
 Age = [12,17]
 # Mpd.bar(Name, Age, color='skyblue') # for the bar chat
 Mpd.pie(Age, labels=Name, autopct = '%1.1f%%' )# for the pie chat
 Mpd.title("My Fisrt graph") 
 Mpd.xlabel('The x')
 Mpd.ylabel('The y')
 Mpd.show()

Panda()
 