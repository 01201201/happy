import matplotlib.pyplot as plt

# 마커 지정

                             	# c=cyan d=diamond
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "cd", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "gd", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "r<", label="PData(km)")
# plt.show()

# 마커 / 선 동시 설정

# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "bo--", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "m1-", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], "kv-.", label="PData(km)")
# plt.show()

# marker 파라메터 사용

# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="H", label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker=11, label="PData(km)")
# plt.plot([2,3,6,7,10], [1,4,5,8,9], marker="s", label="PData(km)")
# plt.show()

# 그래프 영역 채우기
""" xdata = [2, 3, 6, 7, 10]
ydata = [1, 4, 5, 8, 9]
y1data = [2, 4, 6, 8, 10]

plt.plot(xdata, y1data)
plt.xlabel("x_data")
plt.ylabel("y_data")
plt.ylabel("y1_data") """
# 세로축 채우기

# plt.fill_between(xdata[1:4], ydata[1:4], alpha=0.5)
# plt.fill_between(xdata[2:4], ydata[2:4], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.5)
# plt.fill_between(xdata[1:3], ydata[1:3], alpha=0.3)

# 가로축 채우기

# plt.fill_betweenx(ydata[1:3], xdata[1:3], alpha=0.3)
# plt.fill_betweenx(ydata[2:4], xdata[2:4], alpha=0.3)

# 두 선간의 영역 채우기

# plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
# plt.fill_between(xdata[1:4], ydata[1:4], y1data[1:4], alpha=0.5)
# plt.fill_between(xdata[:4], ydata[:4], y1data[:4], alpha=0.5)

# 범위 지정 영역 채우기

# plt.fill([2.9, 2.9, 7.1, 7.1], [2.5, 5.0, 8.5, 6.0], alpha=0.5)

# 배경 설정

# dic_val = {"x_data":[2,3,6,7,10], "y_data": [1, 4, 5, 8, 9]}
# dic1_val = {"x1_data": [1,3,5,7,8], "y1_data":[2,4,6,8,10]}

# plt.plot("x_data", "y_data", data=dic_val, label="PData(km)")
# plt.plot("x1_data", "y1_data", data=dic1_val, label="Value(m)")
# plt.xlabel("x_data")
# plt.ylabel("y_data")

# plt.grid()

# # x축 그리드
# plt.grid(axis="x")

# # y축 그리드
# plt.grid(axis="y")

# # 색상 설정
# plt.grid(axis="y", color="g")
# plt.grid(axis="y", color="b")

# # 투명도 설정
# plt.grid(axis="y", color="g", alpha=0.5)

# 선 종류 선택
# plt.grid(axis="y", color="g", alpha=0.5, linestyle="-")
# plt.grid(axis="y", color="g", alpha=0.5, linestyle="--")
# plt.grid(axis="y", color="g", alpha=0.5, linestyle="-.")

# 눈금 표시

# plt.xticks()
# plt.yticks()

# # 임의 데이터 지정
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])

# # 라벨 지정
# plt.xticks([1,2,3,4,5,6,7,8,9,10], labels=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"])
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11], labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# # 눈금 안쪽/바깥쪽 지
# plt.tick_params(axis="x", direction="in")

# 막대그래프 그리기

x_years = ['2020', '2021', '2022']
y_data = [100, 400, 900]
clr = ["r", "g", "b"]

""" plt.bar(x_years, y_data)
plt.show()

# 색 지정
plt.bar(x_years, y_data, color="g")
# 개별 색 지정
plt.bar(x_years, y_data, color=clr)
# 막대 너비 설정
plt.bar(x_years, y_data, color=clr, width=2)
# 막대 위치 선정
plt.bar(x_years, y_data, color=clr, align="edge", width=0.5)
# 막대 테두리 설정

# 라인 색 선택
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", width=0.5)

# 테두리 라인 설정
plt.bar(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, width=0.5)

# 축 지표

plt.xticks()
plt.yticks() """

# 수평 그래프 그리기
""" 
plt.barh(x_years, y_data)

# 그래프 설정
#   {x축 데이터}{y축 데이터}{색설정} {위치설정} {테두리색설정} {선두께} {그래프 두께}
plt.barh(x_years, y_data, color=clr, align="center", edgecolor="black", linewidth=3, height=0.3)
 """
# 산점도 그래프 그리기

plt.scatter(1, 1)

























plt.show()

