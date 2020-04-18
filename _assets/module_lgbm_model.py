"""
# LGBM_CV 모델 - Dacon Baseline 참조
"""
print(__doc__)

import os
import pandas as pd                         # 데이터 분석 라이브러리
import numpy as np                          # 계산 라이브러리
import matplotlib.pyplot as plt             # * 그래프 이미지

from tqdm import tqdm                       # 진행바

from sklearn.metrics import roc_auc_score   # AUC 스코어 계산
from sklearn.model_selection import KFold   # K-fold CV    
from bayes_opt import BayesianOptimization  # 베이지안 최적화 라이브러리  
from functools import partial               # 함수 변수 고정
import lightgbm as lgb                      # LightGBM 라이브러리
import warnings           
import random                       
warnings.filterwarnings("ignore")           # 경고 문구 미표시

def main():
    pass

def lgb_cv(
            num_leaves, 
            learning_rate, 
            n_estimators, 
            subsample, 
            colsample_bytree, 
            reg_alpha, 
            reg_lambda, 
            x_data=None, 
            y_data=None, 
            n_splits=5, 
            output='score',
        ):
    """ Light Gradient Boost Method 를 빌드."""
    kf = KFold(n_splits=n_splits)
    score = 0
    models = []
    kwargs = {
            'num_leaves'        : int(num_leaves), 
            'learning_rate'     : learning_rate, 
            'n_estimators'      : int(n_estimators), 
            'subsample'         : np.clip(subsample, 0, 1), 
            'colsample_bytree'  : np.clip(colsample_bytree, 0, 1), 
            'reg_alpha'         : reg_alpha, 
            'reg_lambda'        : reg_lambda,
        }  

    for train_index, valid_index in kf.split(x_data):
        x_train, y_train = x_data.iloc[train_index], y_data[train_index]
        x_valid, y_valid = x_data.iloc[valid_index], y_data[valid_index]
        
        model = lgb.LGBMClassifier(**kwargs)
        model.fit(x_train, y_train)
        models.append(model)
        
        pred = model.predict_proba(x_valid)[:, 1]
        true = y_valid
        score += roc_auc_score(true, pred)/n_splits
    
    if output == 'score':
        return score
    if output == 'model':
        return models
    
    
    
    
    
if __name__ is '__main__':
    main()