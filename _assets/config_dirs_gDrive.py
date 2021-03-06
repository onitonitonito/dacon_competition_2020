"""
# FOR gDrive Colab - 화일분석에 필요한 공동폴더를 등록합니다.
# - echo = True : SYS.PATH INSERT 상황 보여줌
"""
echo=False

print(__doc__)

import os
import sys

dir_base = '/content/drive/My Drive/Colab Notebooks/'       # HOME

raw      = 'competition/c03_starcraft_prediction/data_raw/'
remake   = 'competition/c03_starcraft_prediction/data_remake/'
submit   = 'competition/c03_starcraft_prediction/data_submit/'

assets   = dir_base + '_assets/'
statics  = dir_base + '_statics/'
images   = statics + 'images/'


if not dir_base in sys.path:
    sys.path.insert(0, dir_base)
    if echo:
        print(f"***'{dir_base}' HAS SET! in SYS.PATH! ***\n")

        for i, item in enumerate(sys.path,1):
            print(f"{i:02}.{item}")
