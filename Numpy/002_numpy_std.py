import math
vals =[i+1 for i in range(10)]

mean = sum(vals) / len(vals)
print('평균1:',mean)
vsum = 0
for cal in vals:
  vsum += (cal - mean) **2
vari = vsum / len(vals)
print('분산1:', vari)

std = math.sqrt(vari)
print('표준편차: ', std)

import numpy as np

p_mean = np.mean(vals)
print('평균2:', p_mean)
p_var = np.var(vals)
print('분산2:',p_var)
p_std = np.std(vals)
print('표준편차2:',p_std)

np.random.seed(0)

import seaborn as sns
import matplotlib.pyplot as plt

# 21개 랜덤 값
x = np.random.normal(size=40)
bins = np.linspace(-4, 4, 17)
# rug => 아래 작은 그래프 추가
sns.displot(x, rug=True, kde=True, bins=bins)
plt.title('histogram data_graph')
plt.xlabel('x')
plt.show()

print('평균값:',np.mean(x))
print('중앙값:',np.median(x))

ns, _ = np.histogram(x, bins=bins)
m_bin = np.argmax(ns)


print(f'최빈구간:{bins[m_bin]}~{bins[m_bin+1]}')

from sklearn.datasets import load_iris
import pandas as pd
import scipy as sp

x = load_iris()
x = x['data']
sepal_length = x[:,0]
sepal_width = x[:,1]
petal_length = x[:,2]
petal_width = x[:,3]



df = pd.DataFrame(data=x['data'])

df['target'] = pd.DataFrame(data=x['target'])

df.columns = ['sepal_length','sepal_width','petal_length','petal_width','target']

df

# 공분산: 2개의 변수가 선형적으로 상관성이 있는지 정량화한 수
print(np.cov(df.iloc[:,0],df.iloc[:,1]))

df.corr()

# 상관계수 (-1 ~ 1 사이의 )
# 피어슨 상관계수
print(sp.stats.pearsonr(sepal_length,sepal_width))

