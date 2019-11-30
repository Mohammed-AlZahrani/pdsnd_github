import pandas as pd

city_data = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

'''
Starting Bikeshare project with making some libraries
'''

cities = ['new york city', 'chicago', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'none']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'None']

print("\n          _______About To Explore Some Data For Bike Share_______\n")


def filtering():
    global month
    global day
    global city_1
    print(' ')

    """
        Asks user to Choose a city, month, and day to analyze.
        Returns:
            (str) city - name of the city to Filter by
            (str) month - name of the month to Filter by
            (str) day - name of the day of week to Filter by
        """
    while True:
        city = input(f'Enter the city name you would like to see or filter data for: {cities} \n>')
        city_1 = city.lower()
        if city_1[-1] == ' ':
            print('Make sure there is no space after the name!')
            continue
        else:
            pass
        if city_1 not in cities:
            print(f'Try Again And Make Sure Your Spelling Are Correct')
            continue
        else:
            print('-' * 40)
            break

# ------------ Filtering Questions ------------
    ask = input('Would you like to filter the data by month or day or both or (no) for no filter: ')
    if ask == 'month':
        day = 'none'
        while True:
            month = input(
                'Month which you want filter by  \n(january, february, march, april, may, june): \n>')
            if month[-1] == ' ':
                print('Make sure there is no space after the name!')
                continue
            else:
                pass
            if month.lower() not in months:
                print('Please Try Again!')
                continue
            else:
                print('-' * 40)
                break

    if ask == 'day':
        month = 'none'
        while True:
            day = input('''The name of day which you want filter by 
(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) \n>''')
            if day[-1] == ' ':
                print('Make sure there is no space after the name!')
                continue
            else:
                pass
            if day.title() not in days:
                print('Please Try Again:')
                continue
            else:
                print('-' * 40)
                break

    if ask == 'both':
        while True:
            month = input(
                'Month which you want filter by \n(january, february, march, april, may, june): \n>')
            if month[-1] == ' ':
                print('Make sure there is no space after the name!')
                continue
            else:
                pass
            if month.lower() not in months:
                print('Please Try Again!')
                continue
            else:
                print('-' * 40)
                break

        while True:
            day = input('''The name of day which you want filter by 
(Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday) \n>''')
            if day[-1] == ' ':
                print('Make sure there is no space after the name!')
                continue
            else:
                pass
            if day.title() not in days:
                print('Please Try Again:')
                continue
            else:
                print('-' * 40)
                break

    if ask.lower() == 'none' or ask.lower() == 'no':
        month = 'none'
        day = 'none'
    return city_1, month, day


def grap_data(city1, month1, day1):
    global df
    global month
    global day
    '''
    :param city1: Get the selected city from input
    :param month1: If applying filter by month it well get it from input
    :param day1: If applying filter by day it well get it from input
    :return: Filtering data as user required
    '''
    df = pd.read_csv(city_data[city1])

# ---------- Converting 'Start Time' column type to acquire month and day ---------
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.weekday_name

# --------- data filtering as required by the user ---------
    if month != 'none':
        month = months.index(month1) + 1
        df = df[df['month'] == month]
    else:
        pass

    if day != 'none':
        df = df[df['Day of Week'] == day1.title()]
    else:
        pass

    return df


def top_time(df):
    '''Shows The Most Popular Travel Times'''
    print('-' * 40)
    print('Calculating The Most Popular Times of Travel...\n')

    top_month = df['month'].mode()[0]
    print(f'Most Common Month: {top_month}')

    top_day = df['Day of Week'].mode()[0]
    print(f'Most Common day: {top_day}')

    df['hour'] = df['Start Time'].dt.hour
    top_hour = df['hour'].mode()[0]
    print(f'Most Common Hour: {top_hour}')


def top_station(df):
    '''Shows Top Start And End Stations'''
    print('-' * 40)
    print('Graping Top Start And End Stations...\n')

    start_station = df['Start Station'].value_counts().idxmax()
    print(f'Popular start station: {start_station}.')

    end_station = df['End Station'].value_counts().idxmax()
    print(f'Popular end station: {end_station}.')

    df['routes'] = df['Start Station']+ " " + df['End Station']
    a = df['routes'].value_counts().idxmax()
    print(f'Most Combined Stations: {a}.')


def t_trip(df):
    '''Shows total and Average time travel'''
    print('-' * 40)
    print('Calculating Total and Average Trip Duration...\n')

    t_travel = sum(df['Trip Duration'])
    print(f'Total travel Time: {t_travel}')

    average = df['Trip Duration'].mean()
    print(f'Average travel time: {average}')


def user_data(df, city_a):
    """Shows statistics on bikeshare users."""
    print('-' * 40)
    print('Calculating Users Type...\n')

    print('Counts of users type: ')
    print(df['User Type'].value_counts())
    print('')

# -------- Shows Users Sex For Chicago and New York Data --------

    if city_a.lower() != 'washington':
        print('-' * 40)
        print('Calculating counts of gender... \n')

        print('Counts of gender: ')
        gender = df['Gender'].value_counts()
        print(f'{gender}')

# -------- Shows earliest, most recent, and most common year of birth --------

        earliest = df['Birth Year'].min()
        earliest_a = int(earliest)
        print('-' * 40)
        print(f'The earliest birth year is: {earliest_a}')

        most_recent = df['Birth Year'].max()
        most_recent_a = int(most_recent)
        print(f'The latest birth year is: {most_recent_a}')

        most_common = df['Birth Year'].mode().values[0]
        most_common_a = int(most_common)
        print(f'The most common birth year is: {most_common_a}')


def raw_data(df):
    """
    Shows contents of the DATA file to display it as required by the user.
    """

    start = 0
    end = 5

    raw_show = input("\nWanna see the raw data? Enter yes or no").lower()

    if raw_show == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end, :])
            start += 5
            end += 5

            end_show = input("Wanna continue? Enter yes or no").lower()
            if end_show == 'no':
                break


def main():

    while True:
        city_a, month, day = filtering()
        df = grap_data(city_a, month, day)

        top_time(df)
        top_station(df)
        t_trip(df)
        user_data(df, city_a)
        raw_data(df)

        restart = input('\nWanna See The Data Again? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nShutting Down.. See You Again!')
            break


if __name__ == "__main__":
    main()
