import csv
import time
import random


x_data = 0
Team_1 = 115
Team_2 = 122

fieldnames = ['x_data', 'Team_1', 'Team_2']
with open('live_data.csv', 'w') as live_data:
    csv_writer = csv.DictWriter(live_data, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('live_data.csv', 'a') as live_data:
        csv_writer = csv.DictWriter(live_data, fieldnames=fieldnames)

        data = {
            'x_data': x_data,
            'Team_1': Team_1,
            'Team_2': Team_2
        }

        csv_writer.writerow(data)
        print(data)

        x_data += 1
        Team_1 += random.randint(-3, 4)
        Team_2 += random.randint(-4, 3)
    time.sleep(1)