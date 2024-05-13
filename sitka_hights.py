import csv
import datetime
import pathlib
import matplotlib.pyplot as plt

path = pathlib.Path("resource/death_valley_2018_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
head_row = next(reader)

dates, highs, lows = [], [], []
for line in reader:
    highs.append(int(line[6]))
    lows.append(int(line[7]))
    dates.append(datetime.datetime.strptime(line[2], "%Y-%m-%d"))

plt.style.use("Solarize_Light2")
fig, ax, = plt.subplots()
ax.plot(dates, highs, color="red")
ax.plot(dates, lows, color="green")

ax.set_title("Death Valley 2018", fontsize=24)
ax.set_xlabel("Date", fontsize=16)
ax.set_ylabel("")
fig.autofmt_xdate()
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)


plt.show()
