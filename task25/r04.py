from fnmatch import fnmatch

for i in range(2023, 10**10, 2023):
    if fnmatch(str(i), '1?2139*4'):
        print(i, i // 2023)