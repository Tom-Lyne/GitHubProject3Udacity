import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#working - done
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    ny = ['new york', 'new_york', 'new york city', 'new_york_city', 'newyork', 'newyorkcity']
    # gets the user to enter the city that they want to see
    userinput = input('Would you like to see data for Chicago, New York, Or Washington?')
    #make userinput all lowercase to avoid any case sensitive errors
    userinput = userinput.casefold()
    #check to see if its a valid input if its not commence a while loop
    if userinput != 'chicago' and userinput not in ny and userinput != 'washington':
        gate = 0
        #while loop connected to gate string keeps the input coming up until valid input has been detected, this would of been easier with an enquiries package though
        while gate == 0:
            userinput = input('Sorry, but that isnt a valid option please input Chicago, New York or Washington')
            userinput = userinput.casefold()
            #check if the input is now valid if it is then change the gate variable to break the loop
            if userinput == 'chicago' or userinput in ny or userinput == 'washington':
                gate = 1
    #assign the city based on the input.
    if userinput in ny:
        userinput = 'new_york_city'
    city = userinput
    print(city)
    #make sure what we have ascertained is correct so the user can cancel out if needed
    print(f"We have detected that you want to view data relating to: {city}, If this is not correct please restart the program")
    userinput = input('please input the number of the month you want to view (i.e. January = 1) if you want to view all input 0:')
    monthlist = ["all", "january", "february", "march", "april", "june", "july", "august", "september", "october", "november", "december"]
    gate = 0
    testgate = 0
    #loop to make sure the input is an integer
    while gate == 0:
        if userinput.isnumeric() == False:
            #get the user to reinput as an integer
            userinput = input('invalid input - please input as a number of 0 or greater i.e January = 1 and December = 12:')
        if userinput.isnumeric() == True:
            userinput = int(userinput)
            #check if input is too high
            if int(userinput) >= 13:
                userinput = input('invalid input - number too high input as number between 0 and 12')
                gate = 0
                #all gravy, close the loop
            if int(userinput) < 13 and int(userinput) >= 0:
                gate = 1
    month = monthlist[userinput]
    print(f"we have detected you want data for the month: {month}, if this is not correct then please restart your program.")
    # get user input for the day
    userinput = input('Please input the number of the day you want to view (i.e. Friday = 5, Monday = 1, for all enter 0):')
    #define the day array
    daylist = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    #loop to make sure input is an integer
    gate = 0
    while gate == 0:
        if userinput.isnumeric() == False:
            #get the user to reinput as an integer
            userinput = input('Invalid input - please input as a number of 0 or greater i.e. Tuesday = 2, Saturday = 6:')
        if userinput.isnumeric() == True:
            #convert to integer
            userinput = int(userinput)
            #check if input is too high
            if int(userinput) > 7:
                userinput = input('Invalid input - number too high input as a number between 0 and 7')
                gate = 0
            #all gravy, close the loop
            if int(userinput) < 8 and int(userinput) >= 0:
                gate = 1
    day = daylist[userinput]
    print(f"we have detected you want data for the day: {day}, if this is not correct then please restart your program.")
    print('-'*40)
    return city, month, day
#working - done
def time_stats(city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    new_test = 0
    #read in the csv to a dataframe
    filedf = pd.read_csv(f"{city}.csv")
    monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    daysinweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    #convert the start time and end time to date format
    filedf['Start Time'] = pd.to_datetime(filedf['Start Time'])
    filedf['End Time'] = pd.to_datetime(filedf['End Time'])
    #decide on what filters we are using
    if month == 'all':
        #no need to filter the dataframe
        #create a duplicate df
        monthdf = filedf
        #add a month column to it
        monthdf['month'] = monthdf['Start Time'].dt.month
        #find the most common month 
        mcm = monthdf['month'].mode()[0]
        #convert to integer and remove one for list position
        mcm = int(mcm) - 1
        #grab the month name 
        mcm = str(monthsinyear[mcm])
        #get the count of the most common
        mcmcount = monthdf['month'].value_counts().max()
        #ToDo - Figure out how to get the 6 to disappear at the start of the mcmcount string
        print(f"As there was no filter on the month, the most common month travelled is {mcm} with a count of {mcmcount}")
    if month != 'all':
        #find which month we are looking for and return the value associated with it
        position = monthsinyear.index(month)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.month == position]
    if day == 'all':
        #no need to filter the dataframe
        #create a duplicate df
        daydf = filedf
        #create a day column in it
        daydf['day'] = daydf['Start Time'].dt.dayofweek
        #find the most common day
        mcd = daydf['day'].mode()[0]
        #convert to integer and remove one for list position
        mcd = int(mcd)-1
        #grab the day name
        mcd = str(daysinweek[mcd])
        #get the count of the most common
        mcdcount = daydf['day'].value_counts().max()

        print(f"As there was no filter on the day, the common day travelled is {mcd} with a count of {mcdcount}")
    if day != 'all':
        #find which day we are looking for and return the value associated with it
        position = daysinweek.index(day)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.dayofweek == position]
    #create an hour column
    filedf['hour'] = filedf['Start Time'].dt.hour
    #find the most common day
    mch = filedf['hour'].mode()[0]
    #get the count of the most common
    mchcount = filedf['hour'].value_counts().max()
    print(f"The most common starting hour is {mch} with a count of {mchcount}")
    #print out the time taken
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#working - done
def station_stats(city, month, day):
    """Displays statistics on the most popular stations and trip."""
    #print the output
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    filedf = pd.read_csv(f"{city}.csv")
    monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    daysinweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    filterint = 0
    filedf['Start Time'] = pd.to_datetime(filedf['Start Time'])
    filedf['End Time'] = pd.to_datetime(filedf['End Time'])
    #Apply filters to the dataframe
    if month != 'all':
        #find which month we are looking for and return the value associated with it
        position = monthsinyear.index(month)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        #test
        filedf = filedf[filedf['Start Time'].dt.month == position]
        filterint = 1
    if day != 'all':
        #find which day we are looking for and return the value associated with it
        position = daysinweek.index(day)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.dayofweek == position]
        filterint = 1
    #find the most common
    mcstart = filedf['Start Station'].mode()[0]
    #getthe count
    mcstartcount = filedf['Start Station'].value_counts().max()
    
    #find the most common
    mcend = filedf['End Station'].mode()[0]
    #find the count
    mcendcount = filedf['End Station'].value_counts().max()

    #make a column that combines multiple strings
    filedf['trip'] = filedf['Start Station'].str.cat(filedf['End Station'],sep='---->')
    #find the most common
    mccombo = filedf['trip'].mode()
    #find the count
    mccombocount = filedf['trip'].value_counts().max()
    
    #decide whether test is passed and which output to provide
    if filterint != 1:
        #display
        print(f"The most common starting station is {mcstart} with a count of {mcstartcount}")
        print(f"The most common trip is (stations seperated by '---->'): {mccombo} with a count of {mccombocount}")
        print(f"The most commonly used end station is {mcend} with a count of {mcendcount}")
    if filterint == 1:
        print("The below stats are based on your selected filters:")
        print(f"The most common starting station is {mcstart} with a count of {mcstartcount}")
        print(f"The most common trip is (stations seperated by '---->'): {mccombo} with a count of {mccombocount}")
        print(f"The most commonly used end station is {mcend} with a count of {mcendcount}")

    #print out the time taken
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#working - done
def trip_duration_stats(city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    #read in csv
    filedf = pd.read_csv(f"{city}.csv")
    monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    daysinweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    filterint = 0
    filedf['Start Time'] = pd.to_datetime(filedf['Start Time'])
    filedf['End Time'] = pd.to_datetime(filedf['End Time'])
    #Apply filters to the dataframe
    if month != 'all':
        #find which month we are looking for and return the value associated with it
        position = monthsinyear.index(month)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.month == position]
        filterint = 1
    if day != 'all':
        #find which day we are looking for and return the value associated with it
        position = daysinweek.index(day)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.dayofweek == position]
        filterint = 1

    # TO DO: display total travel time
    ttt = filedf['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    ttm = filedf['Trip Duration'].mean()
    ttmax = filedf['Trip Duration'].max()
    ttmin = filedf['Trip Duration'].min()

    if filterint == 1:
        print("The below stats are based on your selected filters:")
        print(f"The total travel time is {ttt}.")
        print(f"The mean travel time is {ttm}. With the highest travel time being {ttmax}. And the lowest being {ttmin}.")
        
    if filterint != 1: 
        print(f"The total travel time is {ttt}.")
        print(f"The mean travel time is {ttm}. With the highest travel time being {ttmax}. And the lowest being {ttmin}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
#working - done
def user_stats(city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #read in csv
    filedf = pd.read_csv(f"{city}.csv")
    monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    daysinweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    filterint = 0
    filedf['Start Time'] = pd.to_datetime(filedf['Start Time'])
    filedf['End Time'] = pd.to_datetime(filedf['End Time'])
    #Apply filters to the dataframe
    if month != 'all':
        #find which month we are looking for and return the value associated with it
        position = monthsinyear.index(month)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.month == position]
        filterint = 1
    if day != 'all':
        #find which day we are looking for and return the value associated with it
        position = daysinweek.index(day)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.dayofweek == position]
        filterint = 1
    old = 0
    young = 0
    mcy = 0
    listint = 0
    if filterint == 1:
        print("Based on your Month/Day filters and removing NaN values:")
    else:
        print("The following is with NaN values removed:")
    headerlist = filedf.columns.values
    a = 'Gender'
    if a in headerlist:
        #add all the user types into a list
        filelist = filedf['User Type']
        filelist = filelist.dropna(axis = 0)
        typelist = filelist.unique()
        #create a list of usertypes
            #loop until the entire list as been processed
        while listint != (len(typelist)):
            #if there are filters do something
            if filterint != 1:
                #get the string value that we are on
                typestr = str(typelist[listint])
                #run a process to return a 1 on each match
                a = filelist.str.count(typestr)
                #sum it together
                b = a.sum()
                #display
                print(f"The count of {typestr} is {b}")
                listint = listint +1
            #if there are no filters do something
            if filterint == 1:
                #get the string value that we are on
                typestr = typelist[listint]
                #run a process to return a 1 on each match
                a = filelist.str.count(typestr)
                #sum it together
                b = a.sum()
                #display
                print(f"Based on your Month/Day filters. The count of {typestr} is {b}.")
                listint = listint +1
        #add all the genders into a list
        filelist = filedf['Gender']
        filelist = filelist.dropna(axis = 0)
        genderlist = filedf['Gender'].unique()
        #reset the list int
        listint = 0
        #loop through until list processed
        while listint != (len(genderlist)):
            #if there are filters do something
            if filterint != 1:
                #get the string value that we are on
                genderstr = str(genderlist[listint])
                #run a process to return a 1 on each match
                a = filelist.str.count(genderstr)
                #sum it together
                b = a.sum()
                #display
                if genderstr != 'nan':
                    print(f"The count of {genderstr} travellers is {b}.")
                listint = listint +1
            #if there are no filters do something
            if filterint == 1:
                #get the string value that we are on
                genderstr = str(genderlist[listint])
                #run a process to return a 1 on each match
                a = filelist.str.count(genderstr)
                #sum it together
                b = a.sum()
                #display
                if genderstr != 'nan':
                    print(f"Based on your Month/Day filters. The count of {genderstr} travellers is {b}.")
                listint = listint +1
    else: 
        print("There is no Gender column in csv therefore cannot get data")

    # TO DO: Display earliest, most recent, and most common year of birth
    a = 'Birth Year'
    if a in headerlist:
        #find the most common YOB 
        mcy = filedf['Birth Year'].mode()[0]
        #find the lowest YOB
        old = filedf['Birth Year'].min()
        young = filedf['Birth Year'].max()

        old = int(old)
        young = int(young)
        mcy = int(mcy)

        print(f"The oldest traveller was born on {old}.")
        print(f"The youngest traveller was born on {young}.")
        print(f"The most common YOB for travellers was {mcy}.")
        
    else: 
        print(f"There is no Birth Year column in the csv therefore cannot get data")

    #Display results

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def raw_data(city, month, day):
    filedf = pd.read_csv(f"{city}.csv")
    monthsinyear = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    daysinweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    filterint = 0
    filedf['Start Time'] = pd.to_datetime(filedf['Start Time'])
    filedf['End Time'] = pd.to_datetime(filedf['End Time'])
    #Apply filters to the dataframe
    if month != 'all':
        #find which month we are looking for and return the value associated with it
        position = monthsinyear.index(month)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.month == position]
        filterint = 1
    if day != 'all':
        #find which day we are looking for and return the value associated with it
        position = daysinweek.index(day)
        #remove the 0 value
        position = position + 1
        #filter the dataframe
        filedf = filedf[filedf['Start Time'].dt.dayofweek == position]
        filterint = 1
    #get input as to whether user wants raw data
    userinput = input("Would you like to see 5 lines of raw data? (yes/no)")
    gate = 0
    #check to make sure input is correct
    while gate == 0:
        if userinput != 'yes' or userinput != 'no':
            print('Invalid input detected please input yes or no')
            gate = 0
        if userinput == 'yes' or userinput == 'no':
            gate = 1
    if userinput == 'yes':
        print('\nPulling in raw data...\n')
        if filterint == 1:
            print('The following is with your Month/Date filters selected:')
        start_time = time.time()
        a = 1
        while a < 6:
            print('First Person:')
            print(filedf.iloc[a])
            print('-'*10)
            a=a+1

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#doesnt need input
def main():
    while True:
        city, month, day = get_filters()
        df = (city, month, day)
        time_stats(city, month, day)
        station_stats(city, month, day)
        trip_duration_stats(city, month, day)
        user_stats(city, month, day)
        raw_data(city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
	main()
