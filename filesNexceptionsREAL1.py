total = 0
counter = 0

try:
    print(f'Opening file "numbers.txt"')
    infile = open('numbers.txt', 'r')
    for line in infile:
        number = int(line)
        total = total + number
        counter = counter + 1

    infile.close()

    average = total/counter

    print(f'The average of your numbers: {average}')
    print(f'The combined total of your numbers: {total}')
                           
except OSError:
    print(f'There was an error trying to read your file. File must be in same directory as this program.')
except ValueError:
    print(f'The file is required to have numeric data only')
except:
    print(f'There was an unexpected error.')
