import os

for i in range(1, 101):
    if not os.path.exists(f'Day {i}'):
        os.mkdir(f'Day {i}')
