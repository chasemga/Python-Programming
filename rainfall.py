def main():

    
    month_rain = [0.0]*12
    month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    for i in range(len(month_rain)):
        month_rain[i] = float(input('Rainfall for ' + month_list[i] + ": "))

    total = sum(month_rain)
    average = total / 12.0
    highest = max(month_rain)
    lowest = min(month_rain)
    highest_month = month_list[month_rain.index(highest)]
    lowest_month = month_list[month_rain.index(lowest)]

    print(f'all numbers in inches')
    print(f"Total Rainfall: {total}")
    print(f"Average Rainfall: {average:.2f}")
    print(f"Highest rainfall: {highest} in {highest_month}")
    print(f"Lowest rainfall: {lowest} in {lowest_month}")

main()
