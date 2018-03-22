# encoding:utf-8
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
# import seaborn as sns

# mpl.style.use('seaborn-whitegrid')

def sta001(k,nyear,xd):
    d2 = np.fv(k,nyear,-xd,-xd) # 复利公式
    d2 = round(d2) # 取近似值
    return d2
# 本金总和
d40=1.4*40
print ("d40,40 * 1.4 =",d40)
# 银行5%利率
d=sta001(0.05,40-1,1.4) # 40-1 第一年不计算收益
print ("01 保守投资模式,",d,round(d/d40))
# 股票20%利率
d2=sta001(0.20,40-1,4)
print ("02 激进投资模式,",d2,round(d2/d40))
# 计算倍数
dk=round(d2/d)
print ("dk,两者差别(xx倍):",dk)

dx05=[sta001(0.05,x,1.4) for x in range(0,40)]
dx10=[sta001(0.10,x,1.4) for x in range(0,40)]
dx15=[sta001(0.15,x,1.4) for x in range(0,40)]
dx20=[sta001(0.20,x,1.4) for x in range(0,40)]

#print (dx05) print (dx20)

df=pd.DataFrame(columns=['dx05','dx10','dx15','dx20'])
df['dx05']=dx05;df['dx10']=dx10
df['dx15']=dx15;df['dx20']=dx20

print ("")
print (df.tail())
# df.plot()
# df.plot(colormap='hot')
df.plot(colormap='brg')

# 制图
def dr_xtyp(_dat):
    i=0
    for xss in plt.style.available:
        #_dat.plot( colormap=xss ) # 颜色表
        plt.figure()
        plt.style.use(xss)
        _dat.plot()
        fss="k101_"+xss+".png"
        plt.savefig(fss)
        i+=1
        print (i,xss,",",fss)
        plt.show()

dr_xtyp(df)