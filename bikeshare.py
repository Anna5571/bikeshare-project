import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n")
      if city not in ('New York City', 'Chicago', 'Washington'):
        print("Invalid input, please try again.\n")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")
      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):
        print("Invalid input, please try again.\n")
        continue
      else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nWhich day would you like to filter by? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all of them?\n")
      if day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all'):
        print("Invalid input, please try again.\n")
        continue
      else:
        break

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
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
    popular_month = df['month'].mode()[0]
    print('Most common month: ', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day: ', popular_day)



    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station: ', start_station)


    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('Most commonly used end station: ', end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' - ' + df['End Station']
    combination = df['combination'].mode()[0]
    print("The most frequent combination of start station and end station: ", combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time, " sec")


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time, " sec")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    #print(user_types)
    print('User types:\n', user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('\nGender Types:\n', gender_types)
    except KeyError:
      print("\nGender Types:\nThere are no data available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth


    try:
      earliest_year = df['Birth Year'].min()
      print('\nEarliest Year: ', earliest_year)
    except KeyError:
      print("\nEarliest year:\nThere are no data available for this city.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('Most Recent Year: ', most_recent_year)
    except KeyError:
      print("\nMost recent year:\nThere are no data available for this city.")

    try:
      most_common_year = df['Birth Year'].mode()[0]
      print('Most common year: ', most_common_year)
    except KeyError:
      print("Most Common Year:\nThere are no data available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df, current_line):

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    view_data = view_data.lower()
    if view_data == 'yes' or view_data == 'y':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_data(df, current_line)
    if view_data == 'no' or view_data == 'n':
        return
    else:
        print("\nInavlid input. Please enter yes or no")
        return display_data(df, current_line)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df,0)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
