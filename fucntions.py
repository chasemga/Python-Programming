def main() :
    print("Enter a time as Hours then Minutes")
    print("Hour value must be between 0 and 23")
    print("Minute value must be between 0 and 59")

    hours = int(input("hours"))
    minutes = int(input("minutes"))
    hours, minutes = read(hours, minutes)
    print(f'Your time is {hours} hours and {minutes} minutes')

def read(hr, mins) :
    HOURS = 24
    MINUTES = 59
    value = 0
    while hr > HOURS :
        print("Invalid value (out of range)")
        hr = int(input(f'Hour value must be between 0 and {HOURS} '))
    while mins > MINUTES :
        print("Invalid value (out of range)")
        mins = int(input(f'Minute value must be between 0 and {MINUTES} '))
    return hr, mins

main()
