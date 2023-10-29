import pandas as pd 
import sys


df = pd.read_csv(sys.argv[1])

df['Price_Per_Sqft'] = df['Price'] / df['area']


undervalued_threshold = int(sys.argv[2])
# basically you can set the threshold value as you wish based on your preferences to buy the property
undervalued_properties = df[df['Price_Per_Sqft'] < undervalued_threshold]


print("Undervalued Properties:")

print(undervalued_properties)
