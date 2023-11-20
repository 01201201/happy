import pandas as pd

# 비교연산

folder = "data/"
target = folder + "fktemp.csv"
df = pd.read_csv(target)

""" temp = df[df.postcode > 70000]
print(temp)
print("\n-------------------\n")

temp1 = df[df.postcode > 70000][["name", "postcode"]]
temp2 = df[df.postcode > df.postcode.mean()][["name", "postcode"]]

print(temp1)
print("\n-------------------\n")
print(temp2) """

# 결측 확인

""" # temp = df.company.isnull()
# temp = df[df.company.isnull()]
temp = df[df.company.isnull()][["name", "postcode"]]
print(temp)
temp = df.company.isnull()
for el in temp :
    if el in temp :
        if el == True:
            print(el) """

# 비트 연산 - Nor 

""" # temp = df[(df.color == "Beige")].postcode.mean()
temp = df[df.postcode > df.postcode.mean()][["name", "postcode"]]
temp1 = df[~(df.color == "Beige")].postcode.mean()
print(temp.count())
print("\n-------------------\n")
print(temp1)
print("\n-------------------\n") """


# and 연산

""" temp = df[(df.color == "Beige") & (df.postcode > 70000)]
print(temp) 
 """
# or 연산

""" temp = df[(df.color == "Beige") | (df.postcode > 70000)][["name"]]
print(temp) """

# 정렬

""" temp = df.sort_values("postcode")
temp1 = df.sort_values("name", ascending=False)
temp1 = df.sort_values("name", ascending=True)
print(temp)
print("\n-------------------\n")
print(temp1) """

#데이터재배열

import pandas as pd

col = ['Machine','Country','Price','Brand']
data = [['TV','Korea',1000,'A'],
        ['TV','Japan',1300,'B'],
        ['TV','China',300,'C'],
        ['PC','Korea',2000,'A'],
        ['PC','Japan',3000,'E'],
        ['PC','China',450,'F']]
df = pd.DataFrame(data=data, columns=col)

print(df)
print("\n-------------------\n")
print(df.pivot(index='Machine',columns='Country',values='Price'))