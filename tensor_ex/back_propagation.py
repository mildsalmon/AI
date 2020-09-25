import numpy as np

# 학습률
learning_rate = 0.3

# 반복 횟수
spoke = 1000

# 시그모이드
def sigmoid(x):
    return 1/(1+np.exp(-x))

# 시그모이드 미분
def sigmoid_deriv(x):
    return x*(1-x)

# 평균 제곱 오차
def mse(targets, values):
    try:
        result = (1/len(targets))*(targets - values)**2

        return result.sum()
    except Exception as e:
        print("error : {0}".format(e))

# 두 번째 layer의 weight들의 업데이트
def update_second_layer_weight(targetY, y, prevY, update_weight):
    v1 = -(targetY - y) + 0
    v2 = y * (1 - y)
    fun = v1 * v2 * prevY

    return update_weight - learning_rate * fun

# 첫 번째 layer의 weight들의 업데이트
def update_first_layer_weight(t1, t2, y1, y2, w1, w2, a, update_weight, input_x):
    e1 = -(t1 - y1) * y1 * (1 - y1) * w1
    e2 = -(t2 - y2) * y2 * (1 - y2) * w2
    v1 = a * (1 - a)
    v2 = input_x
    fun = (e1 + e2) * v1 * v2
    # print("{0} + {1}) * {2} * {3}".format(e1, e2, v1, v2))
    return update_weight - learning_rate * fun

# def run():
#     i = 0
#
#     for i in spoke:
#         z10 = x1 * w0[0][0]

if __name__ == "__main__":
    # 인풋 초기화
    input_x1 = 0.2
    input_x2 = 0.5

    X = np.array([input_x1, input_x2])

    # X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
    # 아웃풋 초기화
    out_t1 = 0.2
    out_t2 = 0.7

    targets = np.array([out_t1, out_t2])

    # targets = np.array([0], [1], [1], [0])
    # Wights 초기화
    w0 = np.array([[0.1, 0.2],
                   [0.3, 0.1]])

    w1 = np.array([[0.4, 0.5],
                   [0.1, 0.3]])

    # 학습률
    learning_rate = 0.3

    # 반복 횟수
    spoke = 1000


    for i in range(spoke):
        # Forward propagation
        z10 = X[:1] * w0[:1, :1] + X[1:2] * w0[1:2, :1]
        a10 = sigmoid(x=z10)
        z11 = X[:1] * w0[:1, 1:2] + X[1:2] * w0[1:2, 1:2]
        a11 = sigmoid(z11)

        z20 = a10 * w1[:1, :1] + a11 * w1[1:2, :1]
        a20 = sigmoid(z20)
        z21 = a10 * w1[:1, 1:2] + a11 * w1[1:2, 1:2]
        a21 = sigmoid(z21)

        values = np.array([a20, a21])

        e_t = mse(targets=targets, values=values)

        print("{0} | y1 = {1}, y2 = {2}, E => {3}".format(i, a20, a21, e_t))

        # Back propagation
        newW0 = np.array([[update_first_layer_weight(t1=targets[:1], t2=targets[1:2], y1=a20, y2=a21,
                                                     w1=w1[:1, :1], w2=w1[:1, 1:2], a=a10, update_weight=w0[:1, :1], input_x=X[:1]),
                           update_first_layer_weight(t1=targets[:1], t2=targets[1:2], y1=a20, y2=a21,
                                                     w1=w1[1:2, :1], w2=w1[1:2, 1:2], a=a11, update_weight=w0[:1, 1:2], input_x=X[:1])],
                          [update_first_layer_weight(t1=targets[:1], t2=targets[1:2], y1=a20, y2=a21,
                                                     w1=w1[:1, :1], w2=w1[:1, 1:2], a=a10, update_weight=w0[1:2, :1], input_x=X[1:2]),
                           update_first_layer_weight(t1=targets[:1], t2=targets[1:2], y1=a20, y2=a21,
                                                     w1=w1[1:2, :1], w2=w1[1:2, 1:2], a=a11, update_weight=w0[1:2, 1:2], input_x=X[1:2])]
                          ])

        newW1 = np.array([[update_second_layer_weight(targetY=targets[:1], y=a20, prevY=a10, update_weight=w1[:1, :1]),
                           update_second_layer_weight(targetY=targets[1:2], y=a21, prevY=a10, update_weight=w1[:1, 1:2])],
                          [update_second_layer_weight(targetY=targets[:1], y=a20, prevY=a11, update_weight=w1[1:2, :1]),
                           update_second_layer_weight(targetY=targets[1:2], y=a21, prevY=a11, update_weight=w1[1:2, 1:2])]
                          ])

        for j, v in enumerate(newW0):
            for ii, vv in enumerate(v):
                w0[j][ii] = vv

        for j, v in enumerate(newW1):
            for ii, vv in enumerate(v):
                w1[j][ii] = vv

        # print(w0[:1, :1])

    print("t1 = {0}, t2 = {1}".format(targets[:1], targets[1:2]))