import os
import platform
import matplotlib.pyplot as plt
import numpy as np

# fix error DPI-1047: Cannot locate a 64-bit Oracle Client library
LOCATION = r"C:\instantclient_19_9"
print("ARCH:", platform.architecture())
# print("FILES AT LOCATION:")
# for name in os.listdir(LOCATION):
# print(name)
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"]

import cx_Oracle

connection = cx_Oracle.connect("hogan", "sfsselect", "SFIS.WORLD")
cursor = connection.cursor()

cursor.execute("""select work_section, mo_number, model_name, pass_qty, fail_qty, first_fail_qty from sfism4.r102 where mo_number = '2153004262' and work_date = '20201212' and group_name = 'FT' and rownum =1 order by work_section""")

for work_section, mo_number, model_name, pass_qty, fail_qty, first_fail_qty in cursor:
    y = np.array([pass_qty, fail_qty, first_fail_qty])
    mylabels = ["Pass_qty", "Fail_qty", "first_fail_qty"]
connection.close()
plt.pie(y, labels=mylabels)
plt.legend(title="San Luong:")
plt.show()
