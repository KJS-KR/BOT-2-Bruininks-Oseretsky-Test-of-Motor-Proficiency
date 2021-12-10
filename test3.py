import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc


plt.rc('font', family='Malgun Gothic') 

x = np.arange(5)

category = ['미세운동 조절', '손 상지 협응', "신체 협응", "근력 및 민첩성", "총점"]
values = [50, 60, 70, 30, 50]

plt.bar(x, values, width=0.5)
plt.xticks(x, category)
plt.axis([-1, 5, 20, 80])
plt.grid(True, axis='y')
plt.ylabel("30(매우낮음) 40(낮음) 50(평균) 60(높음) 70(매우높음)")
plt.show()