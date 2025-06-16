# %% [code]
# city와 f4를 기준으로 f5의 평균값을 구한 다음, f5를 기준으로 상위 7개 값을 모두 더해 출력하시오 (소수점 둘째자리까지 출력)
# - 데이터셋 : basic1.csv 
# - 오른쪽 상단 copy&edit 클릭 -> 예상문제 풀이 시작
# - File -> Editor Type -> Script


import pandas as pd

df = pd.read_csv("../input/bigdatacertificationkr/basic1.csv")
df.head()

# 2개의 기준을 적용해 그룹화 
df = df.groupby(['city', 'f4'])[['f5']].mean()
print(df)

# 내림차순으로 정렬한다. 7개만 추출하여 df에 저장 
df=df.sort_values(['f5'],ascending=False).head(7)
print(df)

# 7개의 합계를 구한 후, 소수점 둘째자리까지 출력
result=df['f5'].sum()
print(f'{result:.2f}')