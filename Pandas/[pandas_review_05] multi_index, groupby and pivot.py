# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
import numpy as np
import pandas as pd

# 버전 문제로 생기는 warning 안뜨게 하는 법
import warnings
warnings.filterwarnings(action='ignore')

# 시간, 날짜 control 위한 패키지 설치
from datetime        import date, datetime, timedelta
from dateutil.parser import parse

import json
import urllib

# titanic dataset
import seaborn as sns

# 비정형 데이터 처리를 위한 라이브러리
from bs4 import BeautifulSoup
import requests
import re

print('numpy version - ', np.__version__)
print('pandas version - ', pd.__version__)
# -

# # 다중 인덱스
# - 여러개의 계층을 갖는 인덱스
# - DataFrame 만들 때 columns = [[1], [2]] 이런 구조로 하게 되는데, [1] 에서 상위(그룹) 인덱스 정의
# - 하위 인덱스[2]와 개수를 맞춰서 하게 되면 해당 하위 인덱스들이 그룹[1]으로 묶이게 됨
# - 사용의 편리성을 위해 열 인덱스의 이름을 부여해서 사용할 수 있음

# ### 다중 인덱스 (열)

multi_col_frm = pd.DataFrame( np.round(np.random.randn(6, 4), 2),
                              columns = [
                                  ['Grp01', 'Grp01', 'Grp02', 'Grp02'] , # 그룹으로 관리하는 index(상위 인덱스) - 하위 인덱스와 개수 맞춰서
                                  ['col02', 'col04', 'col03', 'col01']
                              ])

# 인덱스 별로 각각의 이름을 부여해서 사용 가능
multi_col_frm.columns.names = ['GrpIdx', 'ColIdx']

multi_col_frm.columns.names

# ### 다중 인덱스 (행)

multi_idx_frm = pd.DataFrame( np.round(np.random.randn(6, 4), 2),
                              columns = [
                                  ['Grp01', 'Grp01', 'Grp02', 'Grp02'] , # 그룹으로 관리하는 index(상위 인덱스) - 하위 인덱스와 개수 맞춰서
                                  ['col02', 'col04', 'col03', 'col01']
                              ],
                              index = [
                                  ['M', 'M', 'M', 'F', 'F', 'F'] ,              # 그룹이 되는 인덱스
                                  [ 'id_' + str(idx) for idx in range(6)]      # 우리가 아는 인덱스
                              ])
multi_idx_frm.columns.names = ['GrpIdx', 'ColIdx']  # 열 인덱스 이름 부여
multi_idx_frm.index.names = ['GenderIdx', 'RowIdx'] # 행 인덱스 이름 부여
multi_idx_frm

# ### 다중 인덱스 함수
# - stack() : 열 인덱스 > 행 인덱스로 바꿔줌
#   - DataFrame 이 반시계 방향으로 90도 회전한 모습
# - unstack() : 행 인덱스 > 열 인덱스로 바꿔줌
#   - DataFrame 이 시계 방향으로 90도 회전한 모습
#
# > 둘다 열<->행이 transpose 된게 아니라 열 인덱스가 행 인덱스의 가장 하위 인덱스로 위치하게 되고(stack), 행 인덱스가 열 인덱스의 가장 하위 인덱스로 위치하게 되는 형태(unstack)

multi_idx_frm.stack()

multi_idx_frm.unstack()










