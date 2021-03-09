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
        city = input('Would you like to see data for Chicago, New York City or Washington? ').lower()
        if city in CITY_DATA:
            break
        else:
            print('That\'s not a valid input, please choose one of the three cities Chicago, New York City or Washington?')
        
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:      
        month = input('Please choose a month: january, february, march, april, may, june or all? ').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june','all']:
            break
        else:
            print('That\'s not a valid input')
        
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:      
        day = input('Please choose a day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all? ').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' , 'all']:
            break
        else:
            print('That\'s not a valid input')

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
    df = pd.read_csv(CITY_DATA[city])
    
     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = pd.to_datetime(df['Start Time']).dt.hour
    
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

        
         # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month =  df['month'].mode()[0] - 1
    print('Most Popular Month: ', months[popular_month])

    # TO DO: display the most common day of week
    popular_week =  df['day_of_week'].mode()[0]
    print('Most Popular Start Week: ',popular_week)

    # TO DO: display the most common start hour
    popular_hour =  df['hour'].mode()[0]
    print('Most Popular Start Hour: ',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station =  df['Start Station'].mode()[0]
    print('Most Popular Start station: ',start_station)

    # TO DO: display most commonly used end station
    end_station =  df['End Station'].mode()[0]
    print('Most Popular End station: ', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station'] =   df['Start Station'] + '/' + df['End Station'] 
    print('Most Popular Combination: ',df['combination_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TOTAL_travel = df["Trip Duration"].sum()
    print('Total travel time',TOTAL_travel)
    # TO DO: display mean travel time
    TOTAL_mean = df["Trip Duration"].mean()
    print('Total travel mean',TOTAL_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user types \n ', user_types)
 

    # TO DO: Display counts of gender
    if city == 'chicago' or  city == 'new york city':
        gender = df['Gender'].value_counts()
        print('count of user gender',gender)       
    # TO DO: Display earliest, most recent, and most common year of birth
        
        early =  df['Birth Year'].min()
        print('Earliest birthyear: ',early)
        recent =  df['Birth Year'].max()
        print('Most Recent Birth year: ',recent)
        common =  df['Birth Year'].mode()[0]
        print('Most Popular birth year: ',common)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_rows(df):
    i=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','ye','yep','yea','y'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        user_input = input('would you like to display 5 more rows of data? ').lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_rows(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
