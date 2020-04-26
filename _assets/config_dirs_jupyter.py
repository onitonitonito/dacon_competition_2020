"""
# FOR Jupyter Notebook - 화일분석에 필요한 공동폴더를 등록합니다.
# - echo = True : SYS.PATH INSERT 상황 보여줌
"""

echo=False

print(__doc__)

import os
import sys

HOME= 'dacon_competition_2020'                  # HOME FOLDER!
dir_base = "".join(os.getcwd().partition(HOME)[:2]) + "\\"

assets = dir_base + '_assets/'
statics= dir_base + '_statics/'
images = statics + 'images/'

raw    = 'c03_starcraft_prediction/data_raw/'
remake = 'c03_starcraft_prediction/data_remake/'
submit = 'c03_starcraft_prediction/data_submit/'


if not dir_base in sys.path:
    sys.path.insert(0, dir_base)
    if echo:
        print(f"***'{dir_base}' has set in SYS.PATH! ***\n")

        for i, item in enumerate(sys.path,1):
            print(f"{i:02}.{item}")
