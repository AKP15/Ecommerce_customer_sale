import pandas as pd
df=pd.read_csv('project3_ecommerce_customer_sales.csv')
#princt(df.cated().sum())columns.tolist())
col=['Customer_ID', 'Order_Date', 'Country', 'Category', 'Channel', 'Payment_Method', 'Quantity', 'Unit_Price', 'Discount', 'Sales', 'Shipping_Cost', 'Returned', 'Rating']

#print(df.isnull().sum())
#print(df.duplicated().sum())
#for column in df.columns:
#    print(df[column].value_counts())

new_df=df[['Quantity', 'Unit_Price', 'Discount', 'Sales', 'Shipping_Cost', 'Returned', 'Rating']]
#for column in new_df.columns:
#    print(new_df[column].describe())

df=df.drop_duplicates()
df.loc[303,'Unit_Price']=40
df['Country']= df['Country'].fillna('unknown')
df['Discount']= df['Discount'].fillna(0)
df['Channel']= df['Channel'].str.strip().str.title()
df['Category']= df['Category'].str.strip().str.title()
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    
#print(df['Channel'].value_counts())
#print(df['Category'].value_counts())
#print(df.info())
df.to_csv('cleaned.csv',index=False)
