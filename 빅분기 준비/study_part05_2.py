# 교재 내용 jupyter notebook 으로 진행
# 최종 제출 코드 작성은 pycharm 으로 진행

# data load
import pandas as pd
X_train = pd.read_csv('bigData-main/titanic_x_train.csv', encoding='cp949')
X_test  = pd.read_csv('bigData-main/titanic_x_test.csv',  encoding='cp949')
y_train = pd.read_csv('bigData-main/titanic_y_train.csv', encoding='utf-8')

# 데이터 탐색 과정은 진행하고 메모에 남기고 지우기 

# 데이터 전처리
X_test_passenger_id = X_test['PassengerId']
X_train = X_train.drop(columns = ['PassengerId'])
X_test = X_test.drop(columns = ['PassengerId'])
y_train = y_train.drop(columns = ['PassengerId'])
X_train = X_train.drop(columns = ['티켓번호', '객실번호', '승객이름', '나이'])
X_test = X_test.drop(columns = ['티켓번호', '객실번호', '승객이름', '나이'])

# 결측치 처리
X_train['선착장'] = X_train['선착장'].fillna('S')
X_test['선착장'] = X_test['선착장'].fillna('S')

# encoding
X_train['성별'] = X_train['성별'].replace('male',0).replace('female',1)
X_test['성별'] = X_test['성별'].replace('male',0).replace('female',1)

선착장_dummy = pd.get_dummies(X_train['선착장'], drop_first=True).rename(columns = {'Q':'선착장Q', 'S':'선착장S'})
X_train = pd.concat([X_train, 선착장_dummy], axis=1)
X_train = X_train.drop(columns = ['선착장'])

선착장_dummy = pd.get_dummies(X_test['선착장'], drop_first=True).rename(columns = {'Q':'선착장Q', 'S':'선착장S'})
X_test = pd.concat([X_test, 선착장_dummy], axis=1)
X_test = X_test.drop(columns = ['선착장'])

# 파생변수
X_train['가족수'] = X_train['형제자매배우자수'] + X_train['부모자식수']
X_train = X_train.drop(columns = ['형제자매배우자수', '부모자식수'])
X_test['가족수'] = X_test['형제자매배우자수'] + X_test['부모자식수']
X_test = X_test.drop(columns = ['형제자매배우자수', '부모자식수'])

# 데이터 분리
from sklearn.model_selection import train_test_split
X_TRAIN, X_VAL, Y_TRAIN, Y_VAL = train_test_split(X_train, y_train, test_size=.2, random_state=10)

# 모델 학습 및 평가
from xgboost import XGBClassifier
model2 = XGBClassifier(n_estimators=100, max_depth=5, eval_metric='error', random_state=10)
model2.fit(X_TRAIN, Y_TRAIN)

# 모델 두개만 만들어보고 (기본 vs 하이퍼 파라미터 튜닝) 비교해서 하나만 살리고 삭제
# Y_VAL_PRED2 = model2.predict(X_VAL)
# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(Y_VAL, Y_VAL_PRED2))

# 결과 제출
y_test_pred = pd.DataFrame(model2.predict(X_test), columns = ['Survived'])
final = pd.concat([X_test_passenger_id, y_test_pred], axis=1)
# print(final.head())
final.to_csv('data/12345.csv', index=False)