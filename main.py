import pandas as pd
import matplotlib.pyplot as plt
import os

def get_state(address):
    return address.split(',')[2].split(' ')[1]
all_data = pd.read_csv("all_data.csv")
all_data['Month'] = all_data['Order Date'].str[0:2]
# nan_df = all_data[all_data.isna().any(axis=1)]
all_data = all_data.dropna(how='all')
all_data = all_data[all_data["Order Date"].str[0:2] !='Or']
# all_data['Month'] = all_data['Order Date'].str[0:2]
# all_data["Month"] = all_data['Month'].astype('int32')
all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])
all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])
all_data["Sales"] = all_data["Quantity Ordered"]*all_data["Price Each"]
# results = all_data.groupby("Month").sum()
# months = range(1,13)
# plt.bar(months,results['Sales'])
# plt.show()

# all_data['City'] = all_data['Purchase Address'].apply(lambda x: x.split(',')[1]+' ('+get_state(x)+')')
# results = all_data.groupby('City').sum()
# cities = [city for city, df in all_data.groupby('City')]
# plt.bar(cities, results['Sales'])
# plt.xticks(cities,rotation='vertical',size=8)
# plt.show()

# all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
# all_data["Hour"] = all_data['Order Date'].dt.hour
# all_data['Minute'] = all_data['Order Date'].dt.minute
# hours = [hour for hour ,df in all_data.groupby('Hour')]
# results = all_data.groupby('Hour').count()
# plt.bar(hours,results['Sales'])
# plt.plot(hours, all_data.groupby(['Hour']).count())
# plt.show()

product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']
print(quantity_ordered)
products = [product for product, df in product_group]
plt.bar(products, quantity_ordered)
plt.xticks(products, rotation = 'vertical',size = 8)
plt.show()
