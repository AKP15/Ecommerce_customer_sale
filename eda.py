import pandas as pd 
df=pd.read_csv('cleaned.csv')
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
print(df.columns.tolist())
# Total Revenue| Total Orders| Total Quantity Sold| Average Order Value| Return Rate| Average Rating
total_revenue = df["Sales"].sum()
total_orders = df["Customer_ID"].nunique()
total_quantity = df["Quantity"].sum()
aov = total_revenue / total_orders
return_rate = df["Returned"].mean() * 100
avg_rating = df["Rating"].mean()
#print(f"Total Revenue: ${total_revenue:,.2f}")
#print(f"Total Orders: {total_orders:,}")
#print(f"Total Quantity: {total_quantity:,}")
#print(f"AOV: ${aov:,.2f}")
#print(f"Return Rate: {return_rate:.2f}%")
#print(f"Average Rating: {avg_rating:.2f}")

#Revenue by Category>>>
revenue_by_category=df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
#print(revenue_by_category)

#sales performance by Channel>>>
revenue_by_channel=df.groupby('Channel')['Sales'].sum().sort_values(ascending=False)
#print(revenue_by_channel)

#Revenue by Payment>>>
revenue_by_payment=df.groupby('Payment_Method')['Sales'].sum().sort_values(ascending=False)
#print(revenue_by_payment)


#revenue by country>>>
revenue_by_country=df.groupby('Country')['Sales'].sum().sort_values(ascending=False)
#print(revenue_by_country)

#Monthly Revenue Trend>>>
df["Month"] = df["Order_Date"].dt.to_period("M")
revenue_by_month = df.groupby("Month")["Sales"].sum().sort_values(ascending=False)
#print(revenue_by_month)

#Return Rate by Category
ret_df=df[df['Returned']==1]
returned_order_by_category=ret_df.groupby('Category')['Returned'].count()
total_order_by_category=df.groupby('Category')['Returned'].count()
return_rate=returned_order_by_category/total_order_by_category*100
#print(return_rate)

#Average rating by return rate 
#Split the data into two groups
ret_df=df[df['Returned']==1]
non_ret_df=df[df['Returned']==0]
returned_average_rating=ret_df.groupby('Returned')['Rating'].mean()
non_returned_average_rating=non_ret_df.groupby('Returned')['Rating'].mean()
#print(returned_average_rating)
#print(non_returned_average_rating)

#Return rate by channel 
return_by_channel=ret_df.groupby('Channel')['Returned'].count()
total_by_channel=df.groupby('Channel')['Returned'].count()
return_rate_by_channel=return_by_channel/total_by_channel*100
#print(return_rate_by_channel)

#Return by catagory and channel 
return_cc=ret_df.groupby(['Category','Channel'])['Returned'].count()
total_cc=df.groupby(['Category','Channel'])['Returned'].count()
return_rate_cc=return_cc/total_cc * 100
#print(return_rate_cc.sort_values(ascending=False))


bins=[28,214,372,1248]
labels=['low','medium','high']
df['Spending']=pd.cut(df['Sales'],bins,labels=labels)
ret_df=df[df['Returned']==1]
return_by_spending=ret_df.groupby('Spending')['Returned'].count()
total_by_spending=df.groupby('Spending')['Returned'].count()
return_rate_by_spending=return_by_spending/total_by_spending * 100
#print(return_rate_by_spending)

#ratings by category
ratings_by_category=df.groupby('Category')['Rating'].mean()
#print(ratings_by_category)

#connect Sales and Rating
corr_df=df[['Sales','Rating']]
#print(corr_df.corr())

#dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

fig.suptitle(
            "Ecommerce Customer Sales",
            fontsize=20,
            fontweight="bold"
                    )
kpi_style = {
            "boxstyle": "round,pad=0.8",
            "edgecolor": "gray",
            "facecolor": "white"
                    }

fig.text(
            0.12, 0.90,
            f"Total Revenue\n${total_revenue:,.2f}",
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            bbox=kpi_style
        )

fig.text(
            0.37, 0.90,
            f"Total Orders\n{total_orders:,}",
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            bbox=kpi_style
        )

fig.text(
            0.62, 0.90,
            f"Quantity Sold\n{total_quantity:,}",
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            bbox=kpi_style
        )

fig.text(
            0.87, 0.90,
            f"Average Order Value\n${aov:,.2f}",
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            bbox=kpi_style
        )
