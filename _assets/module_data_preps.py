"""
# 학습용 Data-set 추출 from Raw data (Baseline offer)
"""
print(__doc__)

import os
import re
import pandas as pd                         # 데이터 분석 라이브러리
import numpy as np                          # 계산 라이브러리
import matplotlib.pyplot as plt             # * 그래프 이미지

from tqdm import tqdm                       # 진행바


def main():
    pass

def read_data_file(filename):
    train = pd.read_csv(filename)
    return train

def data_processing(train_data, answer=False):
    """
    # data preps to 1,600 features
    #  IF answer=True, return winner = train_data
    """
    x_data, y_data = [], []

    if answer:
        winners = train_data.groupby(['game_id']).winner.max()

    game_ids = train_data['game_id'].unique()
    speciesdata = pd.DataFrame(train_data.groupby(['game_id', 'player']).species.max())
    speciesdata.species.replace(['T', 'P', 'Z'], [0, 1, 2], inplace=True)

    events = train_data.event.unique()

    # Ability 분석
    print('Ability Data 구축')
    p1 = re.compile('\([^)]*\)\ \-\ ')              # "( xxx ) - "형식의 문자열
    p2 = re.compile('; Location:[^\)]*\)')          # "; Location: ..."  형식의 문자열
    p3 = re.compile('; Target:\ [\w]*', re.DOTALL)  # "; Target: ..." 형식의 문자열
    p4 = re.compile('\ \[[\w]*\]')                  # " [xxxx]" 형식의 문자열
    p5 = re.compile('\([\w]*\)')                    # "(xxxx)" 형식의 문자열

    abilitydata = pd.DataFrame(train_data[train_data.event.isin(['Ability'])])
    abilitydata.event_contents.fillna('', inplace=True)
    abilitydata['event_contents'] = [p5.sub('', p4.sub('', p3.sub('', p2.sub(
        '', p1.sub('', str(v)))))) for v in tqdm(abilitydata.event_contents)]
    unique_ability = abilitydata.event_contents.unique()
    abilitycountdata = pd.DataFrame(abilitydata.groupby(
        ['game_id', 'player']).event_contents.value_counts())
    #display( data.loc[0,0,'TrainSCV'].event_contents )
    #display( data.loc[0,0,'BuildSupplyDepot'].event_contents )

    # Right Click 분석
    print('Right Click Data 구축')
    p1 = re.compile(':\ \([^)]*\)')     # ": ..."  형식의 문자열
    p2 = re.compile('\ \[[^)]*\]')      # " [03BC0001]"형식의 문자열
    pend = re.compile('[\:\;\ ]*')      # ":", ";", " "

    rightclickdata = pd.DataFrame(
        train_data[train_data.event.isin(['Right Click'])])
    rightclickdata.event_contents.fillna('', inplace=True)
    rightclickdata['event_contents'] = [pend.sub('', p2.sub(
        '', p1.sub('', str(v)))) for v in tqdm(rightclickdata.event_contents)]
    unique_rightclick = rightclickdata.event_contents.unique()
    rightclickcountdata = pd.DataFrame(rightclickdata.groupby(
        ['game_id', 'player']).event_contents.value_counts())

    #display( data2.loc[0,0,'TargetNoneLocation'].event_contents )
    #display( data2.loc[0,0,'TargetMedivacLocation'].event_contents )

    # game_id, player별 event별 count값
    print('Event별 Count Data 구축')
    event_count = pd.DataFrame(train_data.groupby(
        ['game_id', 'player']).event.value_counts())

    print('Game별 학습 Data 구축')
    for game_id in tqdm(game_ids):

        # game_id에 대한 player의 종족
        player별종족 = pd.DataFrame(
            [
                [
                    speciesdata.loc[game_id, 0].species,
                    speciesdata.loc[game_id, 1].species
                ]
            ], columns=['P0_species', 'P1_species']
        )

        # event별 발생 count 집계
        df_P0_event, df_P1_event, df_delta_event = {}, {}, {}

        for event in events:
            try:
                df_P0_event['P0_event_' +
                            event] = event_count.loc[game_id, 0, event][0]
            except KeyError:
                df_P0_event['P0_event_' + event] = 0
            try:
                df_P1_event['P1_event_' +
                            event] = event_count.loc[game_id, 1, event][0]
            except KeyError:
                df_P1_event['P1_event_' + event] = 0

        for event in events:
            df_delta_event['event_delta_' + event] = df_P0_event['P0_event_' +
                                                                 event] - df_P1_event['P1_event_' + event]

        df_P0_event = pd.DataFrame(pd.Series(df_P0_event)).T
        df_P1_event = pd.DataFrame(pd.Series(df_P1_event)).T
        df_delta_event = pd.DataFrame(pd.Series(df_delta_event)).T

        # ability에 따른 count 차이를 계산
        df_ability_0, df_ability_1, df_ability_delta = {}, {}, {}
        for ability in unique_ability:
            try:
                df_ability_0['Ability0_' + ability] = abilitycountdata.loc[game_id,
                                                                           0, ability].event_contents
            except KeyError:
                df_ability_0['Ability0_' + ability] = 0
            try:
                df_ability_1['Ability1_' + ability] = abilitycountdata.loc[game_id,
                                                                           1, ability].event_contents
            except KeyError:
                df_ability_1['Ability1_' + ability] = 0

        for ability in unique_ability:
            df_ability_delta['Ability_delta_' + ability] = df_ability_0['Ability0_' +
                                                                        ability] - df_ability_1['Ability1_' + ability]

        df_ability_0 = pd.DataFrame(pd.Series(df_ability_0)).T
        df_ability_1 = pd.DataFrame(pd.Series(df_ability_1)).T
        df_ability_delta = pd.DataFrame(pd.Series(df_ability_delta)).T

        # right click 에 따른 count 차이를 계산
        df_rc_0, df_rc_1, df_rc_delta = {}, {}, {}
        for rc in unique_rightclick:
            try:
                df_rc_0['rc0_' + rc] = rightclickcountdata.loc[game_id,
                                                               0, rc].event_contents
            except KeyError:
                df_rc_0['rc0_' + rc] = 0
            try:
                df_rc_1['rc1_' + rc] = rightclickcountdata.loc[game_id,
                                                               1, rc].event_contents
            except KeyError:
                df_rc_1['rc1_' + rc] = 0
        for rc in unique_rightclick:
            df_rc_delta['rc_delta_' + rc] = df_rc_0['rc0_' + rc] - \
                df_rc_1['rc1_' + rc]
        df_rc_0 = pd.DataFrame(pd.Series(df_rc_0)).T
        df_rc_1 = pd.DataFrame(pd.Series(df_rc_1)).T
        df_rc_delta = pd.DataFrame(pd.Series(df_rc_delta)).T

        out = pd.concat([player별종족, df_P0_event, df_ability_0, df_rc_0, df_P1_event,
                         df_ability_1, df_rc_1, df_delta_event, df_ability_delta, df_rc_delta], axis=1)
        out.index = [game_id]
        out.index.name = 'game_id'

        x_data.append(out)
        if answer:
            y_data.append(winners[game_id])

    x_data = pd.concat(x_data)  # game별 player별 종족, event별 count
    x_data = x_data.fillna(0)
    y_data = np.array(y_data)  # 승리자 list

    return x_data, y_data

def species_converter(string):
    if string == 'T':
        return 0
    elif string == 'P':
        return 1
    elif string == 'Z':
        return 2
    else:
        raise ValueError

def data_preparation(df, answer=False):
    """ Dacon Baseline data-preparation code
    # x, y = data_preparation(df, answer=True)
    # x = <class 'pandas.core.frame.DataFrame'>
    # y = <class 'numpy.ndarray'>
    """
    game_ids = df['game_id'].unique()

    # 8개의 이벤트 액티비티가 존재!
    events = ['Ability',           # 생산,공격 등 선수 주요행동
              'AddToControlGroup', # 부대에 추가
              'Camera',            # 시점 선택
              'ControlGroup',      # 부대 행동
              'GetControlGroup',   # 부대 불러오기
              'Right Click',       # 마우스 우클릭
              'Selection',         # 객체 선택
              'SetControlGroup',   # 부대 지정
            ]

    # 플레이어별 이벤트 발생횟수를 카운트하는 DICT를 생성.저장
    # P0 8-Events Counts={ 'P0_Ability' : 234, 'P0_Camera': 123 ...}
    # P1 8-Events Counts={ 'P0_Ability' : 230, 'P0_Camera': 127 ...}
    # P0-P1의 갭 (delta)={ 'delta_Ability' : 4,'P0_Camera': -4 ...}

    unique_event_0, unique_event_1, delta_event = {}, {}, {}
    for event in events:
        unique_event_0['P0_' + event] = 0       # P0 유니크 이벤트 카운트=0
        unique_event_1['P1_' + event] = 0       # P1 유니크 이벤트 카운트=0
        delta_event['delta_' + event] = 0       # P0-P1의 갭 (delta)

    species = df.groupby(['game_id', 'player']).species.unique()

    event_count = df.groupby(['game_id', 'player']).event.value_counts()
    if answer:
        winners = df.groupby(['game_id']).winner.max()

    x_data, y_data = [], []
    for game_id in tqdm(game_ids):
        df_event_count = event_count[game_id].unstack(level=-1)
        df = pd.DataFrame(species[game_id])
        df = pd.concat([df, df_event_count], axis=1)
        df = df.fillna(0)

        df_P0_species = pd.DataFrame(
                [species_converter(
                        df.loc[0]['species'][0]
                        )
                    ],
                columns=['P0_species'],
            )

        df_P1_species = pd.DataFrame(
                [species_converter(
                        df.loc[1]['species'][0])
                    ],
                columns=['P1_species'],
            )

        df = df.drop(['species'], axis=1)

        df_P0_event = unique_event_0.copy()

        for column in df.columns:
            df_P0_event['P0_' + column] = df.loc[0][column]
        df_P0_event = pd.DataFrame(pd.Series(df_P0_event)).T

        df_P1_event = unique_event_1.copy()
        for column in df.columns:
            df_P1_event['P1_' + column] = df.loc[1][column]
        df_P1_event = pd.DataFrame(pd.Series(df_P1_event)).T

        df_delta_event = delta_event.copy()
        for column in df.columns:
            df_delta_event['delta_' + column] = df_P0_event['P0_' + column][0] - df_P1_event['P1_' + column][0]
        df_delta_event = pd.DataFrame(pd.Series(df_delta_event)).T

        out = pd.concat([df_P0_species, df_P0_event, df_P1_species, df_P1_event, df_delta_event], axis=1)
        out.index = [game_id]
        out.index.name = 'game_id'

        x_data.append(out)
        if answer:
            y_data.append(winners[game_id])

    x_data = pd.concat(x_data)
    y_data = np.array(y_data)

    return x_data, y_data


if __name__ is '__main__':
    main()
