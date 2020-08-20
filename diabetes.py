import matplotlib.pylab as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# 당뇨병 데이터 세트를 적재한다.
diabetes = datasets.load_diabetes()

# 데이터 세트의 형태를 출력
print(diabetes.data.shape)

# 데이터 세트의 특징(변수)들의 이름을 출력
print(diabetes.feature_names)

# 보통 데이터 중 80%는 학습하는 데 사용하고 20%는 테스트에 사용한다
from sklearn.model_selection import train_test_split

# 학습 데이터와 테스트 데이터를 분리한다.
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.2, random_state=0)
print(type(diabetes))

# 선형 회귀 모델로 학습을 수행한다
model = LinearRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측해보자
y_pred = model.predict(X_test)

# 실제 데이터와 예측 데이터를 비교해보자
# 1번 인자 = x 축, 2번 인자 = y축, 3번 인자 = 마킹 방법
plt.plot(y_test, y_pred, '.')

# 직선을 그리기 위하여 완벽한 선형 데이터를 생성한다
x = np.linspace(0, 330, 100)
y = x
plt.plot(x, y)
plt.show()