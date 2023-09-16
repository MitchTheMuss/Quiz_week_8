import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Create empty lists to store data
years = []
co2 = []
temp = []

try:

    cursor.execute("SELECT years, c02, temp FROM Climate Data")

    data = cursor.fetchall()
    
    for row in data:
        years, c02, temp = row
        years.append(years)
        c02.append(c02)
        temp.append(temp)
    conn.close()

except sqlite3.Error as e:
    print("SQLite error:", e)
    conn.close()

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
plt.savefig("co2_temp_1.png") 
