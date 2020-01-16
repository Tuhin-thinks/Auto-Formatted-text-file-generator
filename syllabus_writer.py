import os
import time

filename = input('Enter the file name:')  # give the file name, if not present it will create one


def main_operation():
    i = 5
    flag = 0
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            while i > 0:
                if flag == 0:
                    subject = input('Enter subject name:')
                    file.write('--' + subject + ':\n')
                    flag = 1
                if flag == 2:
                    break
                if flag == 1:
                    print('Enter syllabus:')
                line_input = input()  # syllabus line input
                j = 1
                if line_input != 'complete':
                    while j > 0:

                        if line_input.strip('\n') == 'next':
                            flag = 0
                            break
                        elif line_input.strip('\n') == 'complete':
                            flag = 2
                            break
                        else:
                            file.write('  ' + line_input + '\n')
                        line_input = input()
                else:
                    s = '{}'.format("                 " + "to be continued..." + "          x       " + 16 * '--')
                    file.write(s + '\n')
                    break
    else:
        print('Invalid File name entered... new file created!')  # if file name not present it will create a new one!
        f1 = open(filename, 'a')
        f1.close()
        main_operation()


if __name__ == '__main__':
    main_operation()

time.sleep(2.0)
# file.close()
