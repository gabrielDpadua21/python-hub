import csv
import pandas

TEMPERATURES = []


def open_file() -> None:
    with open('data.csv', newline='') as file:
        for line in file.readlines():
            print(line)


def open_csv() -> None:
    with open('data.csv', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if len(row) > 1 and row[1].isdigit():
                TEMPERATURES.append(row[1])
            print(row)


def open_pandas() -> None:
    df = pandas.read_csv('data.csv')
    TEMPERATURES = df['temp'].tolist()
    data_dict = df.to_dict()
    avarage_temp = sum(TEMPERATURES) / len(TEMPERATURES)
    print(avarage_temp)
    print(df['temp'].mean())
    print(f"Max Temp: {df['temp'].max()}")
    print(f"Min Temp: {df['temp'].min()}")
    print(f"Median: {df['temp'].median()}")
    max_temp_day = df[df.temp == df.temp.max()].day
    monday_temp_in_fire = (int(df[df.day == "Monday"].temp) * 9/5) + 32
    print(f"Day of week max temp: {max_temp_day}")
    print(f"Monday temp in fahrenheit: {monday_temp_in_fire}")

if __name__ == '__main__':
    open_pandas()