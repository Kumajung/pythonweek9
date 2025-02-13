# ตัวอย่างที่ 8 เรามีข้อมูลเกี่ยวกับอายุ (age) และรายได้ (income) ของบุคคล 100 คน 
# เราต้องการสร้างแบบจำลอง Quantile Regression เพื่อศึกษาความสัมพันธ์ระหว่างอายุและรายได้ 
# โดยเฉพาะอย่างยิ่ง เราต้องการทราบว่ารายได้ของบุคคลที่มีอายุ 30 ปี 
# จะมีค่าเท่าใดใน quantile ที่ 0.5 (ค่าเฉลี่ย) และ quantile ที่ 0.9 (ค่าสูงสุด 10%)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import QuantileRegressor

# สร้างข้อมูล
np.random.seed(0)
data = {
    'age': np.random.randint(25, 50, 100),
    'income': np.random.randint(40000, 120000, 100)
}
df = pd.DataFrame(data)

# สร้างแบบจำลอง Quantile Regression
qr = QuantileRegressor(quantile=0.5, solver='highs')
qr.fit(df[['age']], df['income'])

# คาดการณ์ค่ารายได้สำหรับบุคคลที่มีอายุ 30 ปีใน quantile ที่ 0.5
income_pred_05 = qr.predict([[30]])

# สร้างแบบจำลอง Quantile Regression สำหรับ quantile ที่ 0.9
qr_09 = QuantileRegressor(quantile=0.9, solver='highs')
qr_09.fit(df[['age']], df['income'])

# คาดการณ์ค่ารายได้สำหรับบุคคลที่มีอายุ 30 ปีใน quantile ที่ 0.9
income_pred_09 = qr_09.predict([[30]])

# วาดกราฟแสดงความสัมพันธ์ระหว่างอายุและรายได้
plt.scatter(df['age'], df['income'])
plt.plot(df['age'], qr.predict(df[['age']]), label='Quantile 0.5')
plt.plot(df['age'], qr_09.predict(df[['age']]), label='Quantile 0.9')
plt.legend()
plt.xlabel('อายุ')
plt.ylabel('รายได้')
plt.show()

print(f'รายได้ของบุคคลที่มีอายุ 30 ปีใน quantile ที่ 0.5: {income_pred_05[0]:.2f}')
print(f'รายได้ของบุคคลที่มีอายุ 30 ปีใน quantile ที่ 0.9: {income_pred_09[0]:.2f}')