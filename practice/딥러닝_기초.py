
#* 딥러닝이란?
#* 머신러닝의 한 분야로, 사람의 뇌 신경만 구조를 흉내낸 알고리즘
#* 머신러닝: 사람이 직접 피처를 설계 -> 모델이 학습
#* 딥러닝: 모델이 피처까지 스스로 학습

#* 신경망의 기본 구조
#* 뉴런
#* 생물학적 뉴런: 수상돌기(입력) -> 세포체(처리) -> 축삭(출력)
#* 인공 뉴런: 입력값(x) -> 가중합 + 활성화함수 -> 출력값

#* 활성화 함수
#* ReLU (Rectified Linear Unit) - 가장 많이 사용
#* Sigmoid - 이진분류 할때 주로 사용(출력값이 항상 0 ~ 1 사이) -> 확률로 해석 가능
#* softmax - 다중분류 할때 사용 / 여러 클래스의 확률이 합이 1이 되도록 반환

#* 순전파 (Forward Propagation)
#* 입력층 -> 출력층 까지 계산되는 과정
#* 입력층 -> 은닉층1(활성화함수: ReLu) -> 은닉층2(활성화함수:Relu) -> 출력층(sigmoid)

# 실제 숫자로 직접 계산해보기
import numpy as np

np.random.seed(42)
W1 = np.random.randn(3, 4)
b1 = np.zeros(4)
W2 = np.random.randn(4, 1)
b2 = np.zeros(1)

# 스케일링 추가 (0~1 사이로 정규화)
x = np.array([72, 18, 90])
x_scaled = x / np.array([100, 20, 100])  # 나이/100, 출석/20, 참여율/100
print(f"스케일링 전: {x}")
print(f"스케일링 후: {x_scaled}")

print("\n=== 순전파 단계별 계산 ===")
z1 = np.dot(x_scaled, W1) + b1
print(f"은닉층 선형계산 z1: {z1}")

a1 = np.maximum(0, z1)
print(f"ReLU 적용 a1: {a1}")

z2 = np.dot(a1, W2) + b2
print(f"출력층 선형계산 z2: {z2}")

output = 1 / (1 + np.exp(-z2))
print(f"Sigmoid 적용 output: {output}")

# output[0][0] → output[0] 또는 output.flatten()[0]으로 수정
prob = output.flatten()[0]  # 어떤 shape이든 안전하게 꺼내는 방법
print(f"\n요관리 확률: {prob*100:.1f}%")
print(f"예측: {'요관리' if prob >= 0.5 else '정상'}")