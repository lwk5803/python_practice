
#* 머신러닝의 기본 흐름
#* 1. 데이터 준비 -> 2. 데이터 전처리 (정제 / 가공) -> 3. 학습/테스트 데이터 분리 -> 4. 모델 선택 및 학습 -> 5. 예측 -> 6. 평가

#* 핵심개념
#* 피쳐(feature)와 레이블(label)

# 피쳐 (X) : 입력값, 모델이 학습하는 데이터
# 레이블 (y) : 정답값, 모델이 맞춰야 하는 값

# 예시: 이용자 데이터
# 피쳐(X): 나이, 출석횟수, 참여율
# 레이블(y): 요관리 여부 (0: 정상, 1: 요관리)

#? 의사결정나무(decision tree)

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier     # 의사결정나무
from sklearn.ensemble import RandomForestClassifier # 랜덤포레스트
from sklearn.neighbors import KNeighborsClassifier  # K-최근접이웃
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

# 1. 데이터 준비
data = {
    "나이":     [72, 65, 80, 58, 75, 68, 70, 63, 77, 60],
    "출석횟수": [18, 12, 5, 20, 8, 15, 16, 19, 3, 11],
    "참여율":   [90, 60, 25, 100, 40, 75, 80, 95, 15, 55],
    "요관리":   [0, 0, 1, 0, 1, 0, 0, 0, 1, 1] # 0: 정상, 1: 요관리
}

df = pd.DataFrame(data)

# 2. 피처(X)와 레이블(y) 분리

X = df[["나이", "출석횟수", "참여율"]] # 입력값
y = df['요관리'] # 정답값

# 3. 학습 / 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state=42
)

# 4. 모델 선택 및 학습
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train) # 모델 학습!

# 5. 예측
df_pred = dt_model.predict(X_test)
print("예측값:", df_pred)
print("실제값:", y_test.values)

# 6. 평가
accuracy = accuracy_score(y_test, df_pred)
print(f"정확도: {accuracy * 100:.1f}%")

# 새 이용자: 나이 70세, 출석횟수 4회, 참여율 20%
new_user = np.array([[70, 4, 20]])
print(dt_model.predict(new_user))

# 데이터를 5등분해서 번갈아가며 학습 / 테스트
scores = cross_val_score(dt_model, X, y, cv=5)
print(f"교차검증 정확도: {scores.mean() * 100:.1f}%")

#? 랜덤 포레스트(RandomForestClassifier)

# 모델 선택 및 학습
RF_model = RandomForestClassifier()
RF_model.fit(X_train, y_train)

# 모델 예측
rf_pred = RF_model.predict(X_test)
print("예측값:", rf_pred)
print("실제값:", y_test.values)

# 모델 평가

accuracy = accuracy_score(y_test, rf_pred)
print(f"정확도: {accuracy * 100:.1f}%")

# 새 이용자: 나이 70세, 출석횟수 4회, 참여율 20%
new_user = np.array([[70, 4, 20]])
print(RF_model.predict(new_user))

dt_accuracy = accuracy_score(y_test, df_pred)
rf_accuracy = accuracy_score(y_test, rf_pred)

print(f"의사결정나무 정확도: {dt_accuracy * 100:.1f}%")
print(f"랜덤포레스트 정확도: {rf_accuracy * 100:.1f}%")

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

# SVM은 피처 스케일링이 중요해요!
# 나이(58~80)와 참여율(15~100)의 범위가 다르면
# 범위가 큰 피처가 더 큰 영향을 줌

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 1. 선형 SVM
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train_scaled, y_train)

# 2. RBF 커널 SVM
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_rbf.fit(X_train_scaled, y_train)

# 예측 및 평가
pred_linear = svm_linear.predict(X_test_scaled)
pred_rbf = svm_rbf.predict(X_test_scaled)

print(f"선형 SVM 정확도: {accuracy_score(y_test, pred_linear)*100:.1f}%")
print(f"RBF SVM 정확도: {accuracy_score(y_test, pred_rbf)*100:.1f}%")

# 서포트 벡터 확인
print(f"서포트 벡터 수: {len(svm_linear.support_vectors_)}")

import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    "나이":     [72, 65, 80, 58, 75, 68, 70, 63, 77, 60],
    "출석횟수": [18, 12, 5, 20, 8, 15, 16, 19, 3, 11],
    "참여율":   [90, 60, 25, 100, 40, 75, 80, 95, 15, 55],
    "요관리":   [0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
}

df = pd.DataFrame(data)

# 피쳐 / 레이블 분리
X = df[['나이', '출석횟수', '참여율']]
y = df['요관리']

# 학습 / 테스트 데이터 분리
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 피처 스케일링
scaler = StandardScaler()

x_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

# 선형 SVM과 RBF SVM 두 모델을 학습
svm_model = SVC(kernel='linear', C=1.0)
rbf_model = SVC(kernel='rbf', C=1.0, gamma='scale')

svm_model.fit(x_scaled, y_train)
rbf_model.fit(x_scaled, y_train)

dt_model = DecisionTreeClassifier()
dt_model.fit(x_train, y_train)  # 스케일링 불필요
dt_pred = dt_model.predict(x_test)

rf_model = RandomForestClassifier()
rf_model.fit(x_train, y_train)  # 스케일링 불필요
rf_pred = rf_model.predict(x_test)

# 두 모델의 정확도
pred_svm = svm_model.predict(x_test_scaled)
pred_rbf = rbf_model.predict(x_test_scaled)

print(f"선형 SVM 정확도: {accuracy_score(y_test, pred_svm)*100:.1f}%")
print(f"rbf SVM 정확도: {accuracy_score(y_test, pred_rbf)*100:.1f}%")

# 모든 모델의 정확도

print(f"의사결정나무 정확도: {accuracy_score(y_test, dt_pred)*100:.1f}%")
print(f"랜덤포레스트 정확도: {accuracy_score(y_test, rf_pred)*100:.1f}%")
print(f"선형 SVM 정확도: {accuracy_score(y_test, pred_svm)*100:.1f}%")
print(f"rbf SVM 정확도: {accuracy_score(y_test, pred_rbf)*100:.1f}%")