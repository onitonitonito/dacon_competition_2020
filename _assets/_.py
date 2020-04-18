# df_select_null_total 을 만든다.

cols = [ 'time_span', 'delta_rate_pool4', ]

p0_rates_pool4 = {
         0.4 :  10.76923077,
         1.1 :  12.88888889,
         1.5 :  5.286343612,
         2.2 :  8.641975309,
         2.6 :  7.631318137,
         3.3 :  5.546492659,
         4.0 :  6.330837304,
         4.4 :  3.209019948,
         5.1 :  1.980830671,
         5.5 :  2.459396752,
         6.6 :  2.971175166,
         7.3 :  2.118644068,
         8.0 :  4.469273743,
         8.4 :  6.127352823,
         9.1 :  3.374578178,
         9.5 :  1.671938545,
        10.2 :  0.308153577,
        10.6 :  3.000545554,
    }

p0_rates_pool2 = {
        0.2 : 23.91304348,
        0.4 : 3.571428571,
        0.6 : 7.692307692,
        1.1 : 24.63768116,
        1.3 : 6.12244898,
        1.5 : 4.651162791,
        2.0 : 7.142857143,
        2.2 : 9.248554913,
        2.4 : 6.465517241,
        2.6 : 8.623853211,
        3.1 : 6.557377049,
        3.3 : 5.11627907,
        3.5 : 6.608884074,
        4.0 : 5.860805861,
        4.2 : 1.570680628,
        4.4 : 4.827586207,
        4.6 : 3.049421661,
        5.1 : 0.325732899,
        5.3 : 1.323251418,
        5.5 : 3.55515041,
        6.0 : 6.534653465,
        6.2 : 2.831050228,
        6.4 : 1.500441306,
        6.6 : 4.456327986,
        7.1 : 3.363914373,
        7.3 : 1.458670989,
        7.5 : 5.606694561,
        8.0 : 2.18487395,
        8.2 : 4.632587859,
        8.4 : 7.630522088,
        8.6 : 2.795311091,
        9.1 : 4.334828102,
        9.3 : 2.451838879,
        9.5 : 0.840336134,
        10.0 : 0.145825738,
        10.2 : 2.028985507,
        10.4 : 3.762376238,
        10.6 : 2.065613609,
    }

P0_rates_pool1 = {
         0.1 : 100,
         0.2 : 20.45454545,
         0.3 : 5.376344086,
         0.4 : 1.333333333,
         0.5 : 6.52173913,
         0.6 : 9.375,
         1.0 : 42.85714286,
         1.1 : 22.58064516,
         1.2 : 6.796116505,
         1.3 : 5.376344086,
         1.4 : 4.761904762,
         1.5 : 4.545454545,
         1.6 : 4.615384615,
         2.0 : 40,
         2.1 : 11.26760563,
         2.2 : 7.843137255,
         2.3 : 6.140350877,
         2.4 : 6.779661017,
         2.5 : 11.43911439,
         2.6 : 5.839416058,
         3.0 : 4,
         3.1 : 6.744868035,
         3.2 : 6.965174129,
         3.3 : 3.493449782,
         3.4 : 8.636363636,
         3.5 : 4.761904762,
         3.6 : 5.737704918,
         4.0 : 6.896551724,
         4.1 : 2.120717781,
         4.2 : 0.938086304,
         4.3 : 0.716845878,
         4.4 : 8.637873754,
         4.5 : 5.2,
         4.6 : 0.66518847,
         5.0 : 3.03030303,
         5.1 : 0,
         5.2 : 0.578034682,
         5.3 : 2.040816327,
         5.4 : 1.270417423,
         5.5 : 5.860805861,
         5.6 : 6.113537118,
         6.0 : 10.63829787,
         6.1 : 4.301075269,
         6.2 : 1.303538175,
         6.3 : 0.512820513,
         6.4 : 2.554744526,
         6.5 : 2.272727273,
         6.6 : 7.114624506,
         7.0 : 3.333333333,
         7.1 : 3.367003367,
         7.2 : 0.651465798,
         7.3 : 2.258064516,
         7.4 : 4.04040404,
         7.5 : 7.154742097,
         7.6 : 1.492537313,
         8.0 : 8.474576271,
         8.1 : 7.073954984,
         8.2 : 2.222222222,
         8.3 : 8.116883117,
         8.4 : 7.154213037,
         8.5 : 1.867572156,
         8.6 : 3.846153846,
         9.0 : 10.34482759,
         9.1 : 3.764320786,
         9.2 : 1.196581197,
         9.3 : 3.770197487,
         9.4 : 1.615798923,
         9.5 : 0,
         9.6 : 0.036643459,
        10.0 : 21.42857143,
        10.1 : 1.747572816,
        10.2 : 2.307692308,
        10.3 : 2.702702703,
        10.4 : 4.87804878,
        10.5 : 3.8647343,
        10.6 : 0.244498778,
    }



""" SYS.PATH
# C:\Anaconda3
# C:\Anaconda3\Library\mingw-w64\bin
# C:\Anaconda3\Library\usr\bin
# C:\Anaconda3\Library\bin
# C:\Anaconda3\Scripts
# C:\Anaconda3\bin
# C:\Anaconda3\condabin
# C:\Anaconda3
# C\Anaconda3\Scripts
# C\Anaconda3\Library\bin
# C:\Program Files\ImageMagick-7.0.8-Q16-HDRI
# C:\Program Files\Java\jdk-9.0.1\bin
# C:\uncrustify
# C:\MinGW\bin
# C:\WINDOWS
# C:\WINDOWS\system32
# C:\WINDOWS\System32\Wbem
# C:\WINDOWS\System32\WindowsPowerShell\v1.0
# C:\WINDOWS\System32\OpenSSH
# C:\ProgramData\Oracle\Java\javapath
# C:\Program Files (x86)\Yarn\bin
# C:\Program Files (x86)\Graphviz2.38\bin
# C:\Program Files (x86)\Graphviz2.38\bin\dot.exe
# C:\Program Files\Git\cmd
# C:\Program Files\PuTTY
# C:\Program Files\nodejs
# C:\Program Files\Common Files\Intel\WirelessCommon
# C:\Program Files\Intel\WiFi\bin
# C:\Program Files\Microsoft VS Code\bin
# C:\Program Files\Intel\WiFi\bin
# C:\Program Files\Common Files\Intel\WirelessCommon
# C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL
# C:\Program Files\Intel\Intel(R) Management Engine Components\DAL
# C:\Program Files\Java\jdk-9.0.1\bin
# C:\Ruby25-x64\bin
# C:\Users\nitt0\AppData\Roaming\npm
# C:\Users\nitt0\AppData\Local\Yarn\bin
# C:\Users\nitt0\AppData\Local\atom\bin
# C:\Users\nitt0\AppData\Local\Microsoft\WindowsApps
# C:\Users\nitt0\AppData\Local\Microsoft\WindowsApps
"""
