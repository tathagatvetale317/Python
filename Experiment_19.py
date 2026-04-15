print("Tathagat", 251C025")
import pandas as pd
import matplotlib.pyplot as plt
data = {"Name": ["A", "B", "C"], "Marks": [85, 90, 78]}
df = pd.DataFrame(data)
print(df)
plt.bar(df["Name"], df["Marks"])
plt.title("Marks Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
