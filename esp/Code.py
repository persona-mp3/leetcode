#All sales by model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#used to valiate menu options in main menu
menu_options = [1, 2, 3, 4]

def main_menu():
    print("############## Versere Cars Sales ##############")
    print('Please select an option')
    #initiate while loop for validation
    flag = True
    while flag:
        print('Please select an option')
        print('1. Total Sales Analysis')
        print('2. Trends overtime for new and used cars')
        print('3. Trends and patterns ovetime for different sales people')
        print('4. Exit')
        user_input = input('Enter here: ')

        #check if input is int
        try:
            user_input = int(user_input)
            if user_input not in menu_options:
                print('Invalid range')
                print('Please select between 1 and 3')
                #call loop again to ask for input
                flag = True
            else:
                print('Choice accepted')
                #converts to index based match
                user_choice = menu_options[user_input -1]
                print(f'You chose option {user_choice}')
                #break loop
                flag = False
                return user_choice
        #runs if input isn not a number
        except ValueError:
            print('Invalid entry')
            print('Must be a number')
            flag = True



#for total sales meu option
def total_menu():
    print('Total Sales Menu')
    print("########### Please select an option #############")
    print("### 1. All sales by model")   
    print("### 2. Custom selection")

    flag = True
    while flag:
        user_input = input('Enter Here: ')

        try:
            user_input = int(user_input)
            if user_input < 1 or user_input > 2:
                print('INVALID RANGE')
                print('Please select between 1 and 2')
                flag = True
            else:
                print('Choice accepted')
                user_choice = user_input
                print(f'You choose option {user_choice}')
                flag = False
                return user_choice
        except ValueError:
            print('INVALID ENTRY')
            print('Must be a number')
            flag = True




#total for specified car model
def extract_model(user_choice):
    df = pd.read_csv('Task4a_data.csv')
   

    #extract data based on user choice
    extract = df[df['Car Model'] == user_choice]

    #step1. group data by date and car model
    extract_group = extract.groupby(['Car Model', 'Date'])['Value'].sum().reset_index()
    #step2. convert date column to datetime obj
    extract_group['Date'] = pd.to_datetime(extract_group['Date'], format='%d/%m/%Y')
    #step3. filter extract by removing car model column
    filtered_df = extract_group.drop(columns=['Car Model'])
    #step4. sort data by date for consistency
    sorted_df = filtered_df.sort_values('Date', ascending=True)
    print(sorted_df)
    #step5. plot graph using np
    x = np.array(sorted_df['Date'])
    y = np.array(sorted_df['Value'])
    plt.title(f'Total sales for {user_choice} over time')
    plt.xlabel('Date')
    plt.ylabel('Value (£)')
    plt.tight_layout()
    plt.grid()
    plt.plot(x, y, marker='o')
    plt.show()

    #additional info
    #sort the filtered dataframe by value to get the highest sold
    #gets the highest value using integer location
    sorted_by_value = filtered_df.sort_values('Value', ascending=False).iloc[0]['Value']
    #gets the date atv which it was sold
    sold_date =  filtered_df.sort_values('Value', ascending=False).iloc[0]['Date']
    print('\n',f'{user_choice} had a peak sale of £{sorted_by_value} at {sold_date}')

#calc aggregate for sub menu 1 and 2
    
def get_total_data(sub_menu):
    #import data file using pandas
    df = pd.read_csv('Task4a_data.csv')
    #runs based on selection from sub menu
    if sub_menu == 1:
        print('TOTAL SALES FOR CAR MODELS')
        

        #step 1. group dataframe by model
        model_group = df.groupby('Car Model')['Value'].sum().reset_index()
        #step2. sort dataframe
        sorted_models = model_group.sort_values('Value', ascending = False).reset_index(drop=True)
        highest_model = sorted_models.iloc[0]['Car Model']
        highest_val = sorted_models.iloc[0]['Value']
        print(sorted_models)
        print(f'Highest car model sold is {highest_model} at a value of £{highest_val}')
    else:
        print('CUSTOM SELECTION')
        flag = True
        while flag:
            #create a list of all model cars using uique method
            model_list = df['Car Model'].unique()
            #use a for loop to iteratye through the list and print
            for i in enumerate(model_list, 1):
                print(*i)
            print('Select an option')
            user_input = input('Enter here: ')
            #try block for validation and parsing
            try:
                user_input = int(user_input)
                if user_input not in[1, 2, 3, 4, 5]:
                    print('INVALID INPUT')
                    print('Input must be between 1 and 5')
                    flag = True
                #runs if input is valid
                else:
                    print('CHOICE ACCEPTED', '\n')
                    #access choice from model_list by using python matchng index
                    user_choice = model_list[user_input - 1]
                    print(f'You choose to see the data for {user_choice}')
                    #return value so it can be used to vget extrcat in another function
                    extract_model(user_choice)
                    flag = False
                
                    
            except ValueError:
                print('INVALID ENTRY')
                print('INPUT MUST BE A NUMBER', '\n')
                flag = True
                





def new_used_trends():
    #import the csv file
    df = pd.read_csv('Task4a_data.csv')
    

    #step1. find the total value of new and old cars using groupby
    new_used_value = df.groupby(['New/Used', 'Date'])['Value'].sum().reset_index()
       

    #step1.1. concert date column to date object
    new_used_value['Date'] = pd.to_datetime(new_used_value['Date'], format='%d/%m/%Y')
    

    #step2. seperate the new and used data into seperate dataframes
    new_df = new_used_value[new_used_value['New/Used'] == 'New'].reset_index(drop=True)
    used_df = new_used_value[new_used_value['New/Used'] == 'Used'].reset_index(drop=True)

    #step 3. sort and filter by date and drop new/used_column
    #(sort in dates to make the values consistent for graph plotting, in ascending order)
    
    #step3.1. sort for the new_df
    sorted_new = new_df.sort_values('Date', ascending=True).drop(columns=['New/Used']).reset_index(drop=True)
    print('Below is the table showing the periodic sales for the NEW cars over time')
    print(sorted_new)

    #step3.2. sort for the used df
    sorted_used = used_df.sort_values('Date', ascending=True).drop(columns=['New/Used']).reset_index(drop=True)
    print('\n')
    print('Below is the table showing periodic sales for Used Cars over time')
    print(sorted_used)

    #step 4. Plot graphs for both sorted df using numpy and matplotlib
    #step4.1, create x and y values for the sorted_new
    x = np.array(sorted_new['Date'])
    y = np.array(sorted_new['Value'])
    plt.plot(x,y, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Total Values (£)')
    plt.title('Trends and patterns over time for New Cars Sold')
    
    plt.show()

    #repeat step4.1 for the sorted used df but using a and b 
    a = np.array(sorted_used['Date'])
    b = np.array(sorted_used['Value'])
    plt.plot(a,b, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Total Values (£)')
    plt.title('Trends and patterns over time for Used Cars Sold')
    plt.show()


def sales_person_trend():
    df = pd.read_csv('Task4a_data.csv')
    

    #step1. groupby date and slaesperson,
    date_sales_person_group =df.groupby(['Salesperson', 'Date'])['Value'].sum().reset_index()
    

    #step1.1, convert date column to date time obj
    date_sales_person_group['Date'] = pd.to_datetime(date_sales_person_group['Date'], format = '%d/%m/%Y')
    

    #step2, creat a unique list for all sales person
    sales_person_list = date_sales_person_group['Salesperson'].unique()
    print('Here is a list of all Salespesons at Versere Cars')
    #formats and prints out the sales person list
    for i in enumerate(sales_person_list,1):
        print(*i)

    #step 3. use a for loop to iterate through and plot for each salesperson]
    for salesperson in sales_person_list:
    #step3.1 create an extrcat based on current sales person
        extract = date_sales_person_group[date_sales_person_group['Salesperson'] == salesperson].reset_index(drop=True)
        

        #step 3.2, sort the extrcat by date for consistency
        sorted_extract = extract.sort_values('Date', ascending=True).reset_index(drop=True)
        #print(f'Here is the table for {salesperson}')
        #print(sorted_extract, '\n')
        #step3.3 remove the salesperson column to make data appear neater from sorted_extrcat
        filtered_extract = sorted_extract.drop(columns=['Salesperson'])
        print(f'Here is the table for {salesperson}')
        print(filtered_extract, '\n')

        #step4. plot the graph of date against values for each salesperson
        #define x and y values using numpy
        x = np.array(sorted_extract['Date'])
        y = np.array(sorted_extract['Value'])
        plt.plot(x, y, marker='o')
        plt.title(f'Trends and patterns over time for the salesperson {salesperson}')
        plt.xlabel('Date')
        plt.ylabel('Values (£)')
        plt.grid()
        plt.show()

        #additional_info
        #sort filtered_extract by valuen to determine what each person sold the most
        sorted_by_vals = filtered_extract.sort_values('Value', ascending=False)
        highest_val =  sorted_by_vals.iloc[0]['Value']
        date_sold_at = sorted_by_vals.iloc[0]['Date']
        print(f'{salesperson} sold their highest at £{highest_val} on {date_sold_at}')
        
        

    

    

##call sttack for all functions

menu_choice = main_menu()
if menu_choice == 1:
    sub_menu = total_menu()
    total_data= get_total_data(sub_menu)
    
    
    
elif menu_choice == 2:
    new_used_sales = new_used_trends()
elif menu_choice == 3:
    sales_person_trend()
    
else:
    #calls data fpr different sales people
    print('Thank you for visiting Verse Cars')
    quit()
    
    
