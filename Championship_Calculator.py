import sys
import time
import csv


def create_file():
    driver_points_file = open('points.csv', 'w', newline='')

    driver_points = {'HAM': 0,          # Mercedes
                     'BOT': 0,

                     'VER': 0,          # RedBull
                     'ALB': 0,

                     'VET': 0,          # Ferrari
                     'LEC': 0,

                     'NOR': 0,          # McLaren
                     'SAI': 0,

                     'RIC': 0,          # Renault
                     'GHI': 0,

                     'GAS': 0,          # AlphaTauri
                     'TRU': 0,

                     'RAI': 0,          # Sauber/Alpha Romeo
                     'GIO': 0,

                     'PER': 0,          # RacingPoint
                     'STR': 0,

                     'GRO': 0,          # Haas
                     'MAG': 0,

                     'RUS': 0,          # Williams
                     'LAT': 0}

    writer = csv.writer(driver_points_file)

    for key, value in driver_points.items():
        writer.writerow([key, value])

    driver_points_file.close()


def read_from_file():
    driver_points_file = open('points.csv', 'r')
    dictionary = {}
    for line in driver_points_file:
        line = line.strip('\n')
        (key, val) = line.split(",")
        dictionary[key] = int(val)
    return dictionary


def modify_file():
    driver = get_input_driver()
    points = get_input_points()
    dictionary = read_from_file()
    if driver in dictionary:
        dictionary[driver] = int(dictionary[driver]) + points
    return dictionary


def overwrite_file():
    dictionary = modify_file()
    driver_points_file = open('points.csv', 'w', newline='')
    writer = csv.writer(driver_points_file)
    for key, value in dictionary.items():
        writer.writerow([key, value])
    driver_points_file.close()


def get_input_points():
    while True:
        inp = input('Enter the amount of points: \n').casefold()
        if inp == '':
            print('Wrong input, please try again.')
            continue
        elif inp == 'quit':
            print('See you next weekend!')
            time.sleep(0.5)
            sys.exit()
        else:
            return int(inp)


def get_input_driver():
    while True:
        inp = input('Enter your desired driver\'s abreviation: \n').upper()
        if inp == '':
            print('Wrong input, please try again.')
            continue
        elif inp.casefold() == 'quit':
            print('See you next weekend!')
            time.sleep(0.5)
            sys.exit()
        else:
            return inp


def view_points():
    dictionary = read_from_file()
    dictionary_with_ints = dict((k, int(v)) for k, v in dictionary.items())
    sort_dictionary = sorted(dictionary_with_ints.items(), key=lambda x: x[1], reverse=True)
    number = 0
    for driver in sort_dictionary:
        number += 1
        print(str(number)+'.', driver[0], driver[1])


def win_condition():
    dictionary = read_from_file()
    dictionary_with_ints = dict((k, int(v)) for k, v in dictionary.items())
    winner = max(dictionary_with_ints, key=dictionary_with_ints.get)
    print('Crofty: The season has ended...')
    time.sleep(1.5)
    print('Crofty: And what a great one it has been!')
    time.sleep(1.5)
    print('Crofty: With that out of the way, let\'s take a look at our driver standings!')
    time.sleep(5.0)
    print('Crofty: ' + winner + ' is champion of the world with', dictionary_with_ints[winner], 'points!')
    time.sleep(10.0)
    print('Crofty: Thank you for joining us ladies and gentlemen. We\'ll see you next time in winter!')


def main():
    print('Welcome to the Formula 1 Virtual GP calculator!\n')
    time.sleep(0.5)
    print('1. Check actual driver standings.')
    print('2. Edit driver standings.')
    print('3. Declare Winner')
    print('4. Quit')
    while True:
        operation = input('Please choose your desired operation: ')
        if operation == '1':
            view_points()
            continue
        elif operation == '2':
            while True:
                text = str(input('Do you wish to edit a driver\'s points? (YES / NO / QUIT): ')).upper()
                if text == 'YES':
                    overwrite_file()
                    continue
                elif text == 'NO':
                    break
                elif text == 'QUIT':
                    sys.exit()
                else:
                    print('Invalid input!')
                    break
        elif operation == '3':
            win_condition()
            continue
        elif operation == '4':
            print('See you next weekend!')
            time.sleep(1)
            sys.exit()
        else:
            print('Wrong input!')
            continue


main()
