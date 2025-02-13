# ตัวอย่างที่ 4 Spearman’s Rank Correlation
# นักวิจัยต้องการวิเคราะห์ว่ามีความสัมพันธ์ระหว่างระดับความเครียดของพนักงาน (Stress Level) 
# กับระดับความพึงพอใจในงาน (Job Satisfaction) หรือไม่ โดยเก็บข้อมูลจากพนักงาน 10 คน:
# ระดับความเครียด (Stress Level): [7, 8, 6, 9, 5, 4, 6, 7, 8, 5]
# ระดับความพึงพอใจในงาน (Job Satisfaction): [3, 2, 4, 2, 5, 6, 5, 3, 2, 6]
# ใช้ Spearman’s Rank Correlation เพื่อตรวจสอบว่ามีความสัมพันธ์กันหรือไม่ที่ระดับนัยสำคัญ 0.05
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# --- ข้อ 3: Spearman’s Rank Correlation ---
# ข้อมูลระดับความเครียดและระดับความพึงพอใจในงาน
stress_level = np.array([7, 8, 6, 9, 5, 4, 6, 7, 8, 5])
job_satisfaction = np.array([3, 2, 4, 2, 5, 6, 5, 3, 2, 6])

# ทำ Spearman’s Rank Correlation
spearman_corr, spearman_p = stats.spearmanr(stress_level, job_satisfaction)
print("Spearman’s Rank Correlation:")
print(f"Correlation: {spearman_corr}, P-Value: {spearman_p}\n")

# กราฟแสดงผลลัพธ์
plt.figure(figsize=(8, 5))
sns.scatterplot(x=stress_level, y=job_satisfaction, color="blue")
plt.xlabel("Stress Level")
plt.ylabel("Job Satisfaction")
plt.title("Spearman’s Rank Correlation: Stress vs. Job Satisfaction")
plt.show()