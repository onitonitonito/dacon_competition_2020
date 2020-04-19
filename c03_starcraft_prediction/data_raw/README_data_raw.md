## DATA LIST


| NUM  | FILE NAME    | DESCRIPTION           |        ROW | COLUMN | REMARK                     |
| :--: | ------------ | --------------------- | ---------: | :----: | -------------------------- |
|  1   | train.csv    | original raw data     | 67,091,776 |   7    | label = winner             |
|  2   | test.csv     | original raw data     | 28,714,849 |   6    |                            |
|  3   | X1_train.csv | train.csv (80%)  + Y  |     31,097 | 26 + 1 | sklearn.train_test_split() |
|  4   | X1_test.csv  | train.csv (20%)  + Y  |      7,775 | 26 + 1 | sklearn.train_test_split() |
|  5   | X2_train.csv | train.csv (100%) + Y  |     38,872 | 26 + 1 | preps_data                 |
|  6   | X2_test.csv  | test.csv (100%), No-Y |     16,787 |   26   | preps_data                 |



## COLUMN COMPARISON : TRAIN & TEST

| NUM |  TRAIN.CSV  | TEST.CSV       |   IS_SAME |
| :-: | ------------ | ------------ | :-------: |
|1 | game_id                 | game_id                 | True  |
|2 | winner                  | time                    | False |
|  3   | time                    | player                  | False |
|4 | player                  | species                 | False |
|5 | species                 | event                   | False |
|6 | event                   | event_contents          | False |
|7 | event_contents          | -                       | False |



## DATA DETAILS

| 컬럼명            | 값                | type   | 설명                           | 비고              |
| -------------- | ----------------- | ------ | ------------------------------ | ----------------- |
| game_id        | 33781             | int    | 경기 구분 기호                 | unique (multiple) |
| winner         | 0.6523            | float  | player-1 승리확률              | 0.6287            |
| time           | 2.24              | float  | 경기시간 (60분법 구분)         | 2분24초           |
| player         | 0                 | int    | player 0 - 첫번째 선수         |                   |
|                | 1                 | int    | player 1 - 두번째 선수         |                   |
| species        | T                 | Object | 테란 (Terran)                  |                   |
|                | P                 | Object | 프로토스 (Protos)              |                   |
|                | Z                 | Object | 저그 (Zerg)                    |                   |
| event          | Ability           | Object | 생산, 공격 등 선수의 주요 행동 |                   |
|                | AddToControlGroup | Object | 부대에 추가                    |                   |
|                | Camera            | Object | 시점 선택                      |                   |
|                | ControlGroup      | Object | 부대 행동                      |                   |
|                | GetControlGroup   | Object | 부대 불러오기                  |                   |
|                | Right             | Object | Click : 마우스 우클릭          |                   |
|                | Selection         | Object | 객체 선택                      |                   |
|                | SetControlGroup   | Object | 부대 지정                      |                   |
| event_contents | @(좌표, 등)       | object | 이벤트에 관한 상세설명         |                   |





# LGBM Parametric Study

| NUM | SEEd | RANDOM | ITERATION | n_ESTIMATION | num_LEAF | TIME_SPEND| PREDICTION |
|:---:|-----:|---:|---:|-----:|-----:|----------:|:--------:|
| 1   | 50000| 20 | 50 | 1024 | 1024 | 47.28 min | 60.369 % |
| 2   |  4321| 20 | 50 |  500 |  500 | 20.37 min | 60.617 % |
| 3   |  4321| 20 | 50 |  250 |  250 |  8.00 min | 60.758 % |
| 4   |  4321| 20 | 50 |  125 |  125 |  3.29 min | 60.694 % |
| 5   |  4321| 20 | 50 |   62 |   62 |  1.55 min | 60.694 % |
|  -  |
| 1   | 50000| 15 | 75 | 1024 | 1024 | 52.20 min | 60.681 % |
| 2   |  4321| 15 | 75 |  500 |  500 | 24.15 min | 60.553 % |
| 3   |  4321| 15 | 75 |  250 |  250 |  9.48 min | 60.591 % |
| 4   |  4321| 15 | 75 |  125 |  125 |  5.06 min | 60.501 % |
| 5   |  4321| 15 | 75 |   62 |   62 |  2.47 min | 60.360 % |