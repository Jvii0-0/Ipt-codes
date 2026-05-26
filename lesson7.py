from flask import Flask
import matplotlib.pyplot as plt
import pandas as pd

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# if __name__ == '__main__':
#     app.run(debug=True)

# df = pd.read_csv("calories_data.csv")

# Duration  = df["Duration"]
# Date  = str(df["Date"])
# Pulse = df["Pulse"]
# MaxPulse = df["Maxpulse"]
# Calories = df["Calories"]

# products = ["Laptop", "Mouse", "Keyboard"]
# sales = [50, 120, 80]

# plt.bar(Duration, Calories, color='green')
# plt.title("Bar Chart Example")
# plt.show()

# x = [1, 2, 3, 4]
# y = [10, 15, 7, 20]

# plt.plot(x, y, color = 'blue', marker = 'o', linestyle = '--')
# plt.title("Line Chart Sample")
# plt.xlabel("X Axis", color="purple")
# plt.ylabel("Y Axis", color="pink")
# plt.show()

# sizes = [40, 30, 20, 10]
# labels = ["A", "B", "C", "D"]

# explode = [0.1, 0, 0, 0]
# plt.pie(sizes, labels=labels, explode=explode, autopct = '%1.1f%%')
# plt.title("Pie Chart Sample")
# plt.show()

# data = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 5]
# plt.hist(data, bins=5, color="purple", edgecolor="black")
# plt.title("Sample Histogram", fontsize=14, color="pink")
# plt.show()

# data = [1, 8, 3, 6, 5]
# data1 = [9, 7, 8, 9, 10]
# data2 = [11, 9, 13, 7, 15]
# plt.plot(data, label="Expected")
# plt.plot(data1, label="Reality")
# plt.plot(data2, label="Projected")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.show()

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Saved Chard")

plt.savefig("chart.png", dpi = 300, bbox_inches='tight')
plt.show()