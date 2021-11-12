import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
 

#Input Parameter
x_bmi=i = np.arange(0, 30, 1)
x_ipk = np.arange(0, 5, 1)
x_trafik  = np.arange(0, 10, 1)

# Generate fuzzy membership functions

bmi_under = fuzz.trapmf(x_bmi,[0, 1, 18, 18])
bmi_normal = fuzz.trapmf(x_bmi,[18, 18, 25, 25])
bmi_over = fuzz.trapmf(x_bmi,[25, 25, 27, 27])
bmi_obesity=fuzz.trapmf(x_bmi,[27, 27,30, 30])


ipk_rendah = fuzz.trapmf(x_ipk,[0, 0, 1, 2])
ipk_sedang = fuzz.trapmf(x_ipk,[1, 2, 3, 4])
ipk_tinggi = fuzz.trapmf(x_ipk,[3, 4, 4, 4])


trafik_lancar = fuzz.trapmf(x_trafik,[0, 0, 1, 4])
trafik_sedang = fuzz.trapmf(x_trafik,[4, 4, 8,8])
trafik_macet = fuzz.trapmf(x_trafik,[8, 8, 10, 10])

R = 20
S = 50
T = 100

# Visualize these universes and membership functions//membuat visualisasi grafik
fig, (bmi, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 10))


bmi.plot(x_bmi, bmi_under, 'b', linewidth=1.5, label='Underweight')
bmi.plot(x_bmi, bmi_normal, 'g', linewidth=1.5, label='Normal')
bmi.plot(x_bmi, bmi_over, 'r', linewidth=1.5, label='Overweight')
bmi.plot(x_bmi, bmi_obesity, 'y', linewidth=1.5, label='Obesity')

bmi.set_title('Index BMI')
bmi.legend()


ax1.plot(x_ipk, ipk_rendah, 'b', linewidth=1.5, label='Rendah')
ax1.plot(x_ipk, ipk_sedang, 'g', linewidth=1.5, label='Sedang')
ax1.plot(x_ipk, ipk_tinggi, 'r', linewidth=1.5, label='Tinggi')
ax1.set_title('Index Prestasi Mahasiswa')
ax1.legend()

ax2.plot(x_trafik, trafik_lancar, 'b', linewidth=1.5, label='Lancar')
ax2.plot(x_trafik, trafik_sedang, 'g', linewidth=1.5, label='Sedang')
ax2.plot(x_trafik, trafik_macet, 'r', linewidth=1.5, label='Macet')
ax2.set_title('Trafik')
ax2.legend()



for ax in (bmi, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
plt.show()
