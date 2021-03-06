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

| NUM |  TRAIN.CSV  | TEST.CSV       | IS_SAME |
|:---:|-------------|----------------|:-------:|
|1 | game_id        | game_id        | True    |
|2 | winner         | time           | False   |
|3 | time           | player         | False   |
|4 | player         | species        | False   |
|5 | species        | event          | False   |
|6 | event          | event_contents | False   |
|7 | event_contents | -              | False   |



## DATA DETAILS

| 컬럼명         | 값                | type   | 설명                           | 비고              |
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

| NUM | SEED | RANDOM | ITERATION | n_ESTIMATION | num_LEAF | TIME_SPEND| PREDICTION |
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



## XGBM Iteration

| Iter. | Target | Colsample | Gamma | Learn_Rate | Max_Delta | Max_Depth | Reg_Alpha | Reg_Lambda | SubSample |
|--|--|--|--|--|--|--|--|--|--|
|  1        |  0.637    |  0.7742   |  14.71    |  0.2321   |  17.25    |  363.9    |  19.62    |  12.76    |  0.8955   |
|  2        |  0.6306   |  0.6162   |  19.42    |  0.3904   |  7.261    |  256.4    |  10.37    |  42.0     |  0.5312   |
|  3        |  0.6417   |  0.9804   |  6.588    |  0.1989   |  23.69    |  251.4    |  8.492    |  40.21    |  0.5392   |
|  4        |  0.6408   |  0.9462   |  9.748    |  0.1332   |  1.833    |  308.2    |  10.7     |  42.71    |  0.5824   |
|  5        |  0.6359   |  0.9861   |  16.6     |  0.4328   |  1.746    |  344.5    |  12.81    |  24.37    |  0.678    |
|  6        |  0.6385   |  0.6523   |  11.56    |  0.3019   |  13.17    |  272.7    |  12.36    |  27.17    |  0.6759   |
|  7        |  0.6333   |  0.5475   |  14.89    |  0.4889   |  8.224    |  453.4    |  19.26    |  10.5     |  0.7891   |
|  8        |  0.6421   |  0.9586   |  8.6      |  0.215    |  16.62    |  16.49    |  8.444    |  35.57    |  0.5633   |
|  9        |  0.6409   |  0.6151   |  9.27     |  0.1605   |  3.964    |  224.3    |  14.69    |  10.75    |  0.6354   |
|  10       |  0.6422   |  0.6098   |  7.758    |  0.425    |  21.5     |  193.8    |  10.29    |  42.67    |  0.8968   |
|  11       |  0.6353   |  0.9438   |  18.59    |  0.2033   |  13.22    |  10.8     |  19.54    |  15.68    |  0.6975   |
|  12       |  0.6431   |  0.9847   |  6.438    |  0.1648   |  9.992    |  171.0    |  8.58     |  46.7     |  0.5244   |
|  13       |  0.6344   |  0.682    |  18.43    |  0.2585   |  10.11    |  415.0    |  15.61    |  47.38    |  0.6662   |
|  14       |  0.6406   |  0.7198   |  8.694    |  0.3409   |  14.11    |  352.0    |  11.72    |  49.44    |  0.7835   |
|  15       |  0.6381   |  0.9125   |  10.76    |  0.3368   |  19.18    |  191.0    |  19.37    |  27.02    |  0.5894   |
|  16       |  0.6363   |  0.8853   |  17.32    |  0.3217   |  12.2     |  177.1    |  16.59    |  39.75    |  0.7485   |
|  17       |  0.6369   |  0.9016   |  14.5     |  0.171    |  4.717    |  360.9    |  14.99    |  9.614    |  0.5328   |
|  18       |  0.6376   |  0.8326   |  16.37    |  0.406    |  16.16    |  190.9    |  8.965    |  9.143    |  0.8536   |
|  19       |  0.6411   |  0.7981   |  9.339    |  0.2919   |  24.05    |  261.0    |  11.92    |  49.65    |  0.6929   |
|  20       |  0.6318   |  0.6301   |  15.85    |  0.4815   |  5.284    |  356.4    |  16.48    |  25.2     |  0.5646   |