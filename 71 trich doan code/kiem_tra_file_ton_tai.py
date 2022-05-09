# leverage the os package 
import os
exits = os.path.isfile('D:\Xuan\Hoc Tap\Python\K team\Ma_tran_Vecto.py')
print(exits)

# brute force with a try-except block (Python 3+)
try:
	with open('D:\Xuan\Hoc Tap\Python\K team\Ma_tran_Vecto.py','r') as fh:
		print('file is exits')
except FileNotFoundError as e:
	pass
finally:
	pass

# wrap the path in an object for enhanced
from pathlib import Path
config=Path('D:\Xuan\Hoc Tap\Python\K team\Ma_tran_Vecto.py')
if config.is_file():
	print("file is exits")