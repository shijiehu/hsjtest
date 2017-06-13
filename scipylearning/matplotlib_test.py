#coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
x=np.arange(-5 , 5,0.01)
y=x**3
#plt.axis([-6,6,-150,150])
plt.xlim(-6,6)
plt.ylim(-150,150)
plt.plot(x,y,'r',x,x**2,'b',x,x,'g')
plt.title(u'这里写的是中文')
plt.ylabel(u'我是y注释')
plt.xlabel(u'X坐标')
plt.grid(True)
plt.show()