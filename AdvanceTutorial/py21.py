# stats of file

import os
from datetime import *
stats = os.stat('Readme.md')
print('file size : ', stats.st_size)
print('last access time : ', datetime.fromtimestamp(stats.st_atime))
print('last modified time : ', datetime.fromtimestamp(stats.st_mtime))
# print('file size : ', stats.st_size)

# print(os.stat('Readme.md'))


#
# os.stat_result(
#     st_mode=33206,   protection bits
#     st_ino=5910974510924680,   i note number
#     st_dev=16923431263272621985, 
#     st_nlink=1,  no of hot links
#     st_uid=0,   user id
#     st_gid=0,   group user id
#     st_size=6178,   size of file (bytes)
#     st_atime=1706586697,  last access time (ms)
#     st_mtime=1706585914,  last modified time (ms)
#     st_ctime=1706508959   last time when metadat changed (ms)
#     )


# time stated to calculate for computer : 1st Jan 1970 12:00 AM
# for computer standard time : Epoche standard time