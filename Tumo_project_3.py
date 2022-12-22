import re
import time

"""
Station Project 3 : Bonus project   

The Task

Create a program which will take a time from the user as a timer and start to countdown in the terminal. 
You can use any library and function you want for this mini project. Make sure your program - is written 
only using Python - each new countdown line appears after one second, not immediately
"""


def time_format_validation(time_format):
    """
    This function checks the received time format.
    """

    answer = []
    if re.search(r'\d{1,2}:\d{1,2}:\d{1,2}', time_format):
        h, m, s = time_format.split(':')
        if int(h) not in range(0, 24):
            answer.append('Hours should be in a range 0 - 23!')

        if int(m) not in range(0, 60):
            answer.append('Minutes should be in a range 0 - 59!')

        if int(s) not in range(0, 60):
            answer.append('Seconds should be in a range 0 - 59!')

    elif time_format.lower() in ['s', 'stop']:
        answer.append('stop')

    else:
        answer.append('Invalid time format!')

    return answer


def countdown():
    """
    This function asks for time(h:m:s) from the user and starts countdown from that time.
    """

    while True:
        time_format = input('Insert time to count down (h:m:s) or s/stop to quit the program: ')
        answers = time_format_validation(time_format)
        if answers:
            if len(answers) == 1 and answers[0] == 'stop':
                break
            for answer in answers:
                print(answer)

            continue

        time_format = [int(x) for x in time_format.split(':')]

        while True:
            h, m, s = time_format
            if s == 0:
                s = 60
                if m != 0:
                    m -= 1
                    if h != 0:
                        h -= 1

            s -= 1
            time_format[0], time_format[1], time_format[2] = h, m, s

            print(':'.join([str(x) if x > 9 else '0' + str(x) for x in time_format]), end='')
            time.sleep(1)
            print('', end='\r')

            if h == 0 and m == 0 and s == 0:
                print('THE TIME IS OVER!!')
                break


if __name__ == '__main__':
    countdown()

