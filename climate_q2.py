import matplotlib.pyplot as plt
import pandas as pd

#load data 
downloadfile = pd.read_csv('climate.csv')

years = []
co2 = []
temp = []

#extract the C02 and YEAR x/y columns from the table
gases = downloadfile('C02')
years = downloadfile('Year (decade)')


#create bar chart
plt.figure(figsize=(15,8))
plt.bar(gases, years, color='red')
plt.title('Bar Chart for Gases & Years')
plt.xlabel("Year (decade)")
plt.ylabel("[C02]")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

