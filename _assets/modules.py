"""
# OS 화일 및 DF 정보조회를 위한 탐색 모듈
"""
print(__doc__)

import os
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    pass


# DEFINE FUNCTIONS
def show_ls(dir_target=os.getcwd()):
    """OS MODULE NEEDED before HAND"""
    print(os.getcwd() == dir_target)
    print(f"DIR_TARGET={os.getcwd()}")
    print(dir_target)
    os.chdir(dir_target)
    files_list = os.listdir('.')
    files_list.sort()
    
    print("--"*20)    
    for i, item in enumerate(files_list,1):
        print(f"  {i:02}. {item}")
    
def show_infoDF_from(df_target):
    """SHOW ESSENTIAL DF INFO TO OVER-VIEW"""
    print('*** DATA SHAPE = [ {:,} x {:,} ]'.format(*df_target.shape), end='\n\n')
    print(df_target.info(), end='\n\n')
    print(df_target.describe(), end='\n\n')
    df_target.head()       

    
def get_unique_through_check_duplicated_column(df_columns, echo=True, show_unique=True):
    """
    # get_unique_through_check_duplicated_column(df_columns, show_unique=True):
    # check! duplicated columns & return unique columns
    # - 중복되는 칼럼이 있는지 알려주소, 유니크 컬럼을 반납!
    """
    _array = []             # unique cols are gethered here!
    _repeat_dict = {}       # repeated cols are gethered & counted here!
    for col in df_columns:
        if col in _array:
            if col in _repeat_dict.keys():
                _repeat_dict[col] += 1
                if echo:
                    print(f"*** FOUND '{col}' is DUPLICATED! '{_repeat_dict[col]}' times!")
            else:
                _repeat_dict[col] = 1
                if echo:
                    print(f"*** FOUND '{col}' is DUPLICATED!")
        else:
            _array.append(col)
    if show_unique:        
        print(f"\n*** CHOSEN UNIQUE COLUMNS ARE ...\n {_array}")   
    if len(_repeat_dict):
        print(f"\n*** REPEAT COLUMS ARE BELOW! ***\n {_repeat_dict}")
    return _array


def save_df_to_csv(df,filename=False):
    """
    # save_df_to_csv(df,filename=False):
    # filename 이 있으면 save,True / 없으면 '스킵에코',False
    """
    if filename:
        df1.to_csv(dir_base + remake + filename)
        print(f"*** RESULTS ARE RECORDED! at ... '{filename}'")
        return True
    else:
        print(f"*** SKIPPED! SAVE FILE! ***")
        return False
   
    
def histit(axes, series, i, j ,color='Blue', title=' '):
    # hist_it = lambda series,i,j, color: axs[i,j].hist(
    #           series, alpha=0.3, density=True, color=color)
    row, col = (i-1, j-1)
    axes[row,col].hist(series, alpha=0.3, density=True, color=color)
    axes[row,col].set_title(title)
    axes[row,col].grid()    


def hist_it(
        serieses, i=1, j=1, figsize=(10,5), alpha=0.6, overlap=True,
        title='this is the example'):
    """plt 적층구조로 만든다 - 먼저pyplot 임포트가 필요하다
    # 히스토그램은 array 플롯 명령이 가능(병렬비교時), 이때는 알파사용 불가
    # 히스토그램 개별 사용때는 알파사용 가능 (오버랩 중첩)
    """
    plt.subplots(i, j, figsize=figsize)
    if overlap:
        for series in serieses:
            plt.hist(series, alpha=alpha)       # 중첩시, 알파 가능!
            plt.title(f"{title} ... (Over-lapped Comparrison)")
    else:
        plt.hist(serieses)                        # 비교시, 알파 불가능!
        plt.title(f"{title} ... (Solely Comparrison)")
    plt.grid()

def plot_it(
        serieses, i=1, j=1, figsize=(10,5), alpha=0.6, overlap=True,
        title='this is the example'):
    """plt 적층구조로 만든다 - 먼저pyplot 임포트가 필요하다"""
    plt.subplots(i, j, figsize=figsize)
    if overlap:
        for series in serieses:
            plt.plot(series, alpha=alpha)       # 중첩시, 알파 가능!
            plt.title(f"{title} ... (Over-lapped Comparrison)")
    else:
        plt.plot(serieses)                        # 비교시, 알파 불가능!
        plt.title(f"{title} ... (Solely Comparrison)")
    plt.grid()   

def get_random_n_array(repeat_array=5, rand_start=1, rand_end=10, repeat_rand=20):
    """ 원하는 갯수만큼 PD-Series 를 만든다 """
    return [pd.Series(np.array(
        [random.randint(rand_start, rand_end)for i in range(repeat_rand)]))
        for i in range(repeat_array)]

def get_basic_df(dict, key_name='Right_Click'):
    """이벤트 분류용 counts dict에서 기본 key df 를 만들고 컬럼 제정렬 한다."""
    df = pd.DataFrame(dict[key_name])
    df['details'] = df.index.copy()
    df.index = np.arange(len(df['details']))
    df = df[['details', 'event_contents']]              # re-order column position 

    # df.columns = ['details', 'counts']                # rename ... not shows result
    df.rename(columns={'event_contents' : 'counts'})    # rename ... shows result [추천]
    return df

def get_counts_dict_fromDF(df):
    """
    # 이벤트 분류를 위한 counts_dict 를 만든다.
    # CPU times: user 75.4 ms, sys: 2.81 ms, total: 78.2 ms
    # Wall time: 77.6 ms
    """
    counts = {
            'Camera'            : df['event_contents'][df['event'] == 'Camera'].value_counts(),
            'Right Click'       : df['event_contents'][df['event'] == 'Right Click'].value_counts(),
            'GetControlGroup'   : df['event_contents'][df['event'] == 'GetControlGroup'].value_counts(),
            'Selection'         : df['event_contents'][df['event'] == 'Selection'].value_counts(),
            'Ability'           : df['event_contents'][df['event'] == 'Ability'].value_counts(),
            'SetControlGroup'   : df['event_contents'][df['event'] == 'SetControlGroup'].value_counts(),
            'AddToControlGroup' : df['event_contents'][df['event'] == 'AddToControlGroup'].value_counts(),
            'ControlGroup'      : df['event_contents'][df['event'] == 'ControlGroup'].value_counts(),
        }
    return counts

    
if __name__ is '__main__':
    main() 