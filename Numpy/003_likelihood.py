import numpy as np
import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

def likelihood_mu(mu):
  # norm.pdf(): 정규분포 확률밀도함수
  # pdf(x): x범위에 따른 정규확률밀도
  return sp.stats.norm(loc=mu).pdf(0)

mus = np.linspace(-5, 5, 1000)
like_mu = [likelihood_mu(m) for m in mus]
plt.subplot(211)
plt.plot(mus, like_mu)
plt.title('likelihood $L(\mu, \sigma^2=1; x=0)$')
plt.xlabel('$\mu$')

def likelihood_sigma2(sigma2):
  return sp.stats.norm(scale=np.sqrt(sigma2)).pdf(0)

sigma2s = np.linspace(0.1,10,1000)
like_sigma2 = [likelihood_sigma2(s) for s in sigma2s]
plt.subplot(212)
plt.plot(sigma2s,like_sigma2)
plt.title('likelihood $L(\mu=0, \sigma^2; x=0)$')
plt.xlabel('$\sigma^2$')

MU, SIGMA2 = np.meshgrid(mus, sigma2s)

like_sigma2 = [likelihood_sigma2(s) for s in sigma2s]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(MU, SIGMA2, like_sigma2, linewidth=0.1)
plt.xlabel('$\mu$')
plt.ylabel('$\sigma^2$')
plt.title('likelihood $L(\mu, \sigma^2)$')

MU, SIGMA2 = np.meshgrid(mus, sigma2s)
L = np.exp(-MU**2 / (2*SIGMA2)) / np.sqrt(2*np.pi*SIGMA2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(MU, SIGMA2, L, linewidth=0.1)
plt.xlabel('$\mu$')
plt.ylabel('$\sigma^2$')
plt.title('likelihood $L(\mu, \sigma^2)$')

import pandas as pd

# 중심 극한 정리
def central_limit_th(cnt):
  bag_of_mean = []
  for i in range(cnt):
    # 이항분포에서 랜덤 표본 추출(n=1이 p확률로 나오는 것)
    m=np.random.binomial(n=1,p=0.5, size=100).mean()
    bag_of_mean.append(m)
  
  df = pd.DataFrame(bag_of_mean)
  plt.hist(df)
  plt.title(f'data counting : {cnt}')
  plt.xlabel('$\sigma^2$')
  plt.ylabel('Frequency')
  plt.show()

central_limit_th(1000)

# 가우스 함수
mu, sigma = 0, 0.1
s = np.random.normal(loc=mu, scale=sigma, size=1000)
cnt, bins, g = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2 / (2*sigma**2)),linewidth=2,color='r')



import scipy.stats as stats
# 동일한 난수 생성
np.random.seed(1)
# 평균 178, 표준 편차 5
heights = [178+np.random.normal(0,5) for _ in range(20)]
heights
# t-검정
# 유의확률 >= 0.05 : 귀무가설 채택
# 유의확률 < 0.05 : 대립가설 채택
tTestRes = stats.ttest_1samp(heights,173)
tTestRes



