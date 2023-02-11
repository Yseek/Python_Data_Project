import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("자료/Data.xlsx", engine="openpyxl")
# print(df)

plt.rcParams['font.family'] = 'Malgun Gothic'

plt.subplot(2,2,1)
plt.plot(df['월별'], df['강수량'])
plt.xticks("")
plt.xticks(rotation=45)
plt.title("강수량")

plt.subplot(2,2,2)
plt.plot(df['월별'], df['평균기온'])
plt.xticks("")
plt.xticks(rotation=45)
plt.title("평균기온")

plt.subplot(2,2,3)
plt.plot(df['월별'], df['평균상대습도'])
plt.xticks(rotation=45)
plt.title("평균상대습도")

plt.subplot(2,2,4)
plt.plot(df['월별'], df['합정역'])
plt.xticks(rotation=45)
plt.title("합정역 따릉이 평균이용")

plt.suptitle("2019~2021 3개년 월별평균")

plt.show()