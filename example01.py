# ตัวอย่างที่ 1
# นักวิจัยต้องการศึกษาว่ามีนัยสำคัญทางสถิติหรือไม่ระหว่างคะแนนสอบของนักเรียนสองห้องเรียน (A และ B) โดยมีข้อมูลดังนี้:

# ห้อง A: [85, 90, 88, 92, 75, 78, 80, 95, 85, 87]
# ห้อง B: [82, 76, 78, 80, 74, 70, 79, 85, 81, 77]

# ใช้ Mann-Whitney U Test เพื่อตรวจสอบว่าคะแนนสอบของนักเรียนในห้อง A และห้อง B มีความแตกต่างกันอย่างมีนัยสำคัญทางสถิติหรือไม่ที่ระดับนัยสำคัญ 0.05
# นำเข้าข้อมูลและไลบรารี

# เรานำเข้า numpy และ scipy.stats เพื่อใช้คำนวณทางสถิติ
# กำหนดข้อมูลของห้องเรียน A และ B ในรูปแบบ numpy array
# คำนวณ Mann-Whitney U Test

# ใช้ stats.mannwhitneyu() ซึ่งรับค่าเป็นสองกลุ่มข้อมูลที่ต้องการทดสอบ
# กำหนด alternative='two-sided' เพื่อใช้การทดสอบแบบสองด้าน
# แสดงผลลัพธ์

# ค่า U-Statistic เป็นค่าที่ใช้เปรียบเทียบอันดับของข้อมูลในสองกลุ่ม
# ค่า P-Value ใช้เพื่อตัดสินใจทางสถิติ
# สรุปผลลัพธ์โดยเปรียบเทียบกับระดับนัยสำคัญ (alpha = 0.05)

# หาก p_value < 0.05 → มีความแตกต่างกันอย่างมีนัยสำคัญ
# หาก p_value ≥ 0.05 → ไม่มีความแตกต่างกันอย่างมีนัยสำคัญ

import numpy as np
import scipy.stats as stats

# ข้อมูลคะแนนสอบของทั้งสองกลุ่ม
group_A = np.array([85, 90, 88, 92, 75, 78, 80, 95, 85, 87])
group_B = np.array([82, 76, 78, 80, 74, 70, 79, 85, 81, 77])

# ทำ Mann-Whitney U Test
u_statistic, p_value = stats.mannwhitneyu(group_A, group_B, alternative='two-sided')

# แสดงผลลัพธ์
print(f"U-Statistic: {u_statistic}")
print(f"P-Value: {p_value}")

# ตรวจสอบระดับนัยสำคัญ
alpha = 0.05
if p_value < alpha:
    print("ผลการทดสอบ: มีความแตกต่างกันอย่างมีนัยสำคัญทางสถิติระหว่างคะแนนสอบของห้อง A และ B")
else:
    print("ผลการทดสอบ: ไม่มีความแตกต่างกันอย่างมีนัยสำคัญทางสถิติระหว่างคะแนนสอบของห้อง A และ B")

# สร้าง scatter plot ใหม่โดยใช้ภาษาอังกฤษ
plt.figure(figsize=(8, 5))
plt.scatter(["A"] * len(group_A), group_A, color='blue', label="Class A")
plt.scatter(["B"] * len(group_B), group_B, color='red', label="Class B")

# ปรับข้อความเป็นภาษาอังกฤษ
plt.xlabel("Class")
plt.ylabel("Exam Scores")
plt.title("Scatter Plot of Exam Scores for Class A and B")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

# แสดงกราฟที่อัปเดต
plt.show()
