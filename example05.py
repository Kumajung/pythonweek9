# ตัวอย่างที่ 6 Friedman Test
# โจทย์ ทดสอบว่ามีความแตกต่างระหว่างกลุ่มข้อมูลที่เก็บจากหลายช่วงเวลาหรือไม่ จาก Data => friedman_data.csv
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
friedman_data = pd.read_csv('/kaggle/input/example-week-09-data/friedman_data.csv')

# ทำ Friedman Test
friedman_stat, friedman_p = stats.friedmanchisquare(*[friedman_data[col] for col in friedman_data.columns])
print("Friedman Test:")
print(f"Statistic: {friedman_stat}, P-Value: {friedman_p}\n")

# กราฟ scatterplot
plt.figure(figsize=(8,5))
sns.scatterplot(data=friedman_data)
plt.title("Friedman Test Data Distribution")
plt.show()