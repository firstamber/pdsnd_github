import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Would you like to see data for Chicago, New York or Washington?\n').title()
        if city not in ['Chicago','New York','Washington']:
            city = input('Please enter a valid city name.\n')
            #continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)   
   # x=input("Would you like to filter the data by month,day,both or not at all?Type None for no time filter.\n")
    while True:
            #if x=='month':
        month = input('Which Month? All,January,February,March,April,May or June?\n').lower()
        if month not in ['all','january','february','march','april','may','june']:
            month = input ('Please enter a valid month')
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        #elif x=='day':
         day = input ('Which day? All,Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday?\n').lower()
         if day not in ['all','monday','tuesday','wendesday','thursday','friday','saturday','sunday']:
             day = input('please enter a valid day')
             continue
         else:
             break#print ('Please enter a valid day')
                
        #elif x == "both":
            #month = input('Which Month? January,February,March,April,May or June?\n').lower()
            #day = input ('Which day? Please type your response as an integer.\n').lower()
         

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    CITY_DATA={'Chicago':'chicago.csv','New York City':'new_york_city.csv','Washington':'washington.csv'}
   
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    
    if month !='all':
        months = ['january','february','march','april','may','june']
        month = months.index(month)+1
        df=df[df['month']==month]
                                 
    if day!='all':
        df=df[df['day_of_week']==day.title()]   
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print ("the most common month is {} ,Count: {}".format(popular_month,df['month'].value_counts().max()))
           
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print ("the most common day is {} ,Count: {}".format(popular_day,df['day_of_week'].value_counts().max()))
    # TO DO: display the most common start hour
    popular_start_hour = df['Start Time'].mode()[0]
    print ("the most common hour is {} ,Count: {}".format(popular_start_hour,df['Start Time'].value_counts().max()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ("the most commonly used start station is {} ,Count: {}".format(popular_start_station,df['Start Station'].value_counts().max()))
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ("the most commonly used end station is {} ,Count: {}".format(popular_end_station,df['End Station'].value_counts().max()))
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station']+ df['End Station']).mode()[0]
    print ("the most frequent combination trip is {} ".format(popular_trip))
    #,df['Start Station']+df['End Station'].value_counts().max()))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ("total travel time",total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ("mean travel time ",mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
    # TO DO: Display counts of user types
        print("counts of user types",df['User Type'].value_counts())

    # TO DO: Display counts of gender
        print("counts of gender",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print("earliest year of birth {}, most recent year of birth {}, and most common year of birth {}". format (df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0]))
    except KeyError as e :
        print ('Washington does not have Gender and Birth Year data')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """prompt the user if they want to see 5 lines of raw data,
       Display that data if the answer is 'yes',
       Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
       Stop the program when the user says 'no' or there is no more raw data to display."""
    view_data = input('\nWould you like to view 5 rows of individual trip data? enter yes or no\n')
    start_loc = 0
    while view_data.lower()=='yes':
        print (df.iloc[start_loc:start_loc+5])
        start_loc+=5
        view_data = input("Do you wish to continue?:  ").lower()
    return 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
