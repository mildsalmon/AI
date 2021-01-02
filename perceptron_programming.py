# 뉴런의 출력 계산 함수
def calculate(input):
    global weights
    global bias
    activation = bias
    # 입력신호 총합 계산
    for i in range(2):
        activation += weights[i]*input[i]
    # 스텝 활성화 함수
    if activation >= 0.0:
        return 1.0
    else:
        return 0.0

# 학습 알고리즘
def train_weights(X, y, l_rate, n_epoch):
    global weights
    global bias
    # 에포크 반복
    for epoch in range(n_epoch):
        sum_error = 0.0
        # 데이터 세트를 반복
        for row, target in zip(X, y):
            # 실제 출력 계산
            actual = calculate(row)
            error = target - actual
            bias = bias + l_rate * error
            # 오류의 제곱 계산 (참고값이다)
            sum_error += error**2
            # 가중치 변경
            for i in range(2):
                weights[i] = weights[i] + l_rate * error * row[i]

            print(weights, bias)
        print('에포크 번호={0}, 학습률={1:.3f}, 오류={2:.3f}'.format(epoch, l_rate, sum_error))
    return weights

# AND 연산 학습 데이터셋, 샘플과 레이블이다
X = [[170, 80], [175, 76], [180, 70], [160, 55], [163, 43], [165, 48]]
y = [0, 0, 0, 1, 1, 1]
# 가중치와 바이어스 초기값
weights = [0.0, 0.0]
bias = 0.0
# 학습률
l_rate = 0.1
# 에포크 횟수
n_epoch = 50
weights = train_weights(X, y, l_rate, n_epoch)
print(weights, bias)