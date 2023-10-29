import pandas as pd 
import sys
df = pd.read_csv('magicbricks_data.csv')


df['Price_Per_Sqft'] = df['Price'] / df['area']


undervalued_threshold = sys.argv[1]

undervalued_properties = df[df['Price_Per_Sqft'] < undervalued_threshold]


print("Undervalued Properties:")

print(undervalued_properties)
