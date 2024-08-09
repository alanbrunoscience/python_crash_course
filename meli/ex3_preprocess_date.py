import os

def preprocessDate(dates):
    months_map = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    
    new_dates = []
    for date in dates:
        parts = date.split()
        day = parts[0][:-2]
        month = months_map[parts[1]]
        year = parts[2]

        day = day.zfill(2)  # Ensure day has two digits
        
        formatted_date = f"{year}-{month}-{day}"
        new_dates.append(formatted_date)
    
    return new_dates

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dates_count = int(input().strip())
    dates = []

    for _ in range(dates_count):
        dates_item = input().strip()
        dates.append(dates_item)

    result = preprocessDate(dates)

    fptr.write('\n'.join(result) + '\n')  # Write all dates at once
    
    fptr.close()



