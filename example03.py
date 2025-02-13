# ตัวอย่างที่ 5 Mann-Whitney U Test (จากไฟล์ CSV)
# โจทย์ ทดสอบว่าคะแนนสอบของกลุ่ม A และกลุ่ม B มีความแตกต่างกันอย่างมีนัยสำคัญหรือไม่ จาก Data => mann_whitney_data.csv
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
mann_whitney_data = pd.read_csv('/kaggle/input/example-week-09-data/mann_whitney_data.csv')

# แยกกลุ่ม A และ B
group_A = mann_whitney_data[mann_whitney_data['Group'] == 'A']['Score'].values
group_B = mann_whitney_data[mann_whitney_data['Group'] == 'B']['Score'].values

# ทำ Mann-Whitney U Test
mann_whitney_stat, mann_whitney_p = stats.mannwhitneyu(group_A, group_B)
print("Mann-Whitney U Test:")
print(f"Statistic: {mann_whitney_stat}, P-Value: {mann_whitney_p}\n")

# กราฟ scatterplot
plt.figure(figsize=(8,5))
sns.scatterplot(x=mann_whitney_data['Group'], y=mann_whitney_data['Score'], hue=mann_whitney_data['Group'], palette="deep")
plt.xlabel("Group")
plt.ylabel("Score")
plt.title("Mann-Whitney U Test: Score Comparison Between Group A and B")
plt.show()