from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')       # 得到3d坐标的图

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)     # 曲面，x,y,z坐标，横向步长，纵向步长，颜色，线宽，是否渐变

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))         # 设置z轴标度
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))         # 设置z轴精度

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)          # shrink颜色条伸缩比例0-1, aspect颜色条宽度（反比例，数值越大宽度越窄）

plt.show()
