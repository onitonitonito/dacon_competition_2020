"""
# XGBM_CV 모델 - by SongDo_StudyGroup Code 참조
"""
print(__doc__)


import random  
import numpy as np                          # 계산 라이브러리
import pandas as pd                         # 데이터 분석 라이브러리
import xgboost as xgb

from tqdm import tqdm                       # 진행바
from sklearn.metrics import roc_auc_score   # AUC 스코어 계산
from sklearn.model_selection import KFold   # K-fold CV
from bayes_opt import BayesianOptimization  # 베이지안 최적화 라이브러리
from functools import partial               # 함수 변수 고정
from keras.utils import to_categorical      # 카테고리 범주바꾸는 라이브러리

import warnings                             
warnings.filterwarnings("ignore")           # 경고 문구 미표시

def main():
    pass

"""
# XGBClassifier
# 반드시 튜닝해야할 파라미터는 max_depth / gamma
"""

def XGB_cv( max_depth, 
            learning_rate, 
            subsample, 
            colsample_bytree, 
            reg_alpha, 
            reg_lambda, 
            gamma, 
            max_delta_step, 
            x_data=None, 
            y_data=None, 
            n_splits=5, 
            output='score'
        ):
    """ Extreme Gradient Boost Method 를 빌드."""
    
    score = 0
    kf = KFold(n_splits = n_splits)
    models = []
    for train_index, valid_index in kf.split(x_data):
        x_train, y_train = x_data.iloc[train_index], y_data[train_index]
        x_valid, y_valid = x_data.iloc[valid_index], y_data[valid_index]

        model = xgb.XGBClassifier(
            # booster = 'dart',
            max_depth = int(max_depth),
            # n_estimators = int(n_estimators),
            learning_rate = learning_rate,
            subsample = np.clip(subsample, 0, 1),
            # colsample_bynode = np.clip(colsample_bynode, 0, 1),
            colsample_bytree = np.clip(colsample_bytree, 0, 1),
            reg_alpha = reg_alpha,
            reg_lambda = reg_lambda,
            gamma = gamma,
            max_delta_step = max_delta_step,
        )

        model.fit(x_train, y_train)
        models.append(model)

        pred = model.predict_proba(x_valid)[:, 1]
        true = y_valid
        score += roc_auc_score(true, pred) / n_splits

    if output == 'score':
        return score
    
    if output == 'model':
        return models












    
    
if __name__ is '__main__':
    main()