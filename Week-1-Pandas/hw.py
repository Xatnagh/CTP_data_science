import pandas as pd
import numpy as np

df = pd.read_csv('data/listings.csv', sep=',')

#prints out the listings that have price under 100

# print(df[sc][['id','name','price']])
private = df["room_type"] == "Private room"
private_room_percentage = len(df[private])/len(df)*100
print("Private rooms: {:.2f}%".format(private_room_percentage))
print("public room: {:.2f}%".format(100-private_room_percentage))