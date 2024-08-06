#Joseph Gerard, Zach Castenbach, Noah Willhite, Anthony Hawkins
#Imports retail sales data from an Excel file into a PostgreSQL database
#user can retrieve and it will display unique product categories from the database, the program will also display statistics about each product category, including sum, average etc.
#finally, it creates a graph that depicts the data for the choosen category

#importing the necessary libraries
import sqlalchemy

import pandas as pd

import matplotlib.pyplot as plt


# Function converts the user input to an integer

# If it's not an integer, changes it to 3, which will exit the loop

def convertOrExit(userInput) -> int:

    try:

        userInput = int(userInput)

    except:

        userInput = 3


    return userInput


# For fixing categories

productCategoriesDict = {

    'Camera': 'Technology',

    'Laptop': 'Technology',

    'Gloves': 'Apparel',

    'Smartphone': 'Technology',

    'Watch': 'Accessories',

    'Backpack': 'Accessories',

    'Water Bottle': 'Household Items',

    'T-shirt': 'Apparel',

    'Notebook': 'Stationery',

    'Sneakers': 'Apparel',

    'Dress': 'Apparel',

    'Scarf': 'Apparel',

    'Pen': 'Stationery',

    'Jeans': 'Apparel',

    'Desk Lamp': 'Household Items',

    'Umbrella': 'Accessories',

    'Sunglasses': 'Accessories',

    'Hat': 'Apparel',

    'Headphones': 'Technology',

    'Charger': 'Technology'

}


# Takes user input and converts it using the function ^

userInput = input("If you want to import data, enter 1. If you want to see summaries of stored data, enter 2. Enter any other value to exit the program: ")

userInput = convertOrExit(userInput)


# Retrieves data from the excel sheet

df = pd.read_excel("C:\\Users\\joefg\\OneDrive\\Desktop\\Current School\\IS 303\\group\\Retail_Sales_Data.xlsx")

#starts the program, below is the logic if the user inputs 1, or wants to import data
if userInput == 1:

    # Inserts empty columns into the df

    df.insert(2, "first_name", '')

    df.insert(3, "last_name", '')


    # Takes names from "name" column and splits them into firstname and lastname

    for row, col in df.iterrows():

        names = df.at[row, "name"].split("_")

        df.at[row, "first_name"] = names[0]

        df.at[row, "last_name"] = names[1]


    # Deletes original "name" column, now that first and last name are stored

    del df["name"]

    print(df)


    # Fixes category for each product

    df["category"] = df["product"].map(productCategoriesDict)

    

    #below creates a connection to the database
    try:

        # Replace with your own database connection string
        dbURL = ("postgresql+psycopg2://postgres:1985@localhost:5433/postgres") 

        engine = sqlalchemy.create_engine(dbURL)

        connection = engine.connect()

        connection.close()
        
        # Saves the DataFrame to the PostgreSQL database

        df.to_sql("sale", engine, if_exists='replace', index=False)

        # Prints out the success message

        print("You've imported the excel file into your postgres database.")

#exception in case of any error with the connection
    except Exception as e:

        print(f"An error occurred: {e}")


#below is the logic if the user inputs 2, or wants to see the category summarized
if userInput == 2:

    try:

        # part 2:2, printing each of categories. Replace with actual database connection

        engine = sqlalchemy.create_engine('postgresql://postgres:1985@localhost:5433/postgres')

        # Read the data from sale table

        dfImported = pd.read_sql_query("SELECT * FROM sale", engine)

        #gets each unique category
        unique_categories = dfImported["category"].unique() 

        # Prints all the categories

        print("The following are all the categories that have been sold:")

        category_dict = {}
        
        #loops through each category to print it with the number next to it. 
        for i, category in enumerate(unique_categories, start=1):

            print(f"{i}. {category}")

            category_dict[i] = category


        # part 3:2 asks user for a category number to then pull data on

        category_number = int(input("Please enter the number of the category you want to see summarized: "))

        selected_category = category_dict.get(category_number, None)

        # shows information for the category decided by the user
        if selected_category:
            print(f"You selected the category: {selected_category}")

            # Filter dataframe for the selected category
            df_filtered = dfImported.query(f"category == '{selected_category}'")

            # Calculate summary statistics
            total_sales_sum = df_filtered["total_price"].sum()

            total_sales_avg = df_filtered["total_price"].mean()

            total_units_sold = df_filtered["quantity_sold"].sum()

            # Display summary statistics, rounds to 2 digits for the sum and average
            print(f"Summary for category '{selected_category}':")

            print(f"Total Sales: {total_sales_sum.round(2)}")

            print(f"Average Sale Amount: {total_sales_avg.round(2)}")

            print(f"Total Units Sold: {total_units_sold}")

            # Group by product and calculate the sum of total sales for each product
            
            product_sales = df_filtered.groupby('product')['total_price'].sum().reset_index()

            # Plotting the bar chart, puts product as the x label, total sales as the y, and gives it a unique title for each category. 
            plt.figure(figsize=(10, 6))
            
            plt.bar(product_sales['product'], product_sales['total_price'], color='skyblue')
            
            plt.xlabel('Products')
            
            plt.ylabel('Total Sales')
            
            plt.title(f'Total Sales by Product for Category: {selected_category}')
            
            plt.xticks(rotation=45, ha='right')
            
            plt.tight_layout()
            
            plt.show()

        # in case the user doesn't put in a correct category number
        else:
            print("Invalid category number")

#exception in case of any error
    except Exception as e:

        print(f"An error occurred: {e}")


#ends the program once the user is done, or if the something other than 1 or 2 is input
print("Closing the program.")