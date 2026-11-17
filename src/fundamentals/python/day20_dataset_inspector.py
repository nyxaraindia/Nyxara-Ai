import os
print(os.path.exists('Nyxara.txt'))
print(os.path.isfile('Nyxara.txt'))
print(os.path.isdir('python'))
os.makedirs('python',exist_ok=True)