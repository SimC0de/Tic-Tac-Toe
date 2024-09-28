from ascii_arts import *

block_1 = []
block_2 = []
block_3 = []
block_4 = []
block_5 = []
block_6 = []
block_7 = []
block_8 = []
block_9 = []

start_range = 0

i = 0
while (i < 11):
    stop_range = start_range + 20
    block_1.append(range(start_range, stop_range))
    block_2.append(range(start_range + 25, stop_range + 25))
    block_3.append(range(start_range + 50, stop_range + 50))
    block_4.append(range(start_range + 781, stop_range + 781))
    block_5.append(range(start_range + 806, stop_range + 806))
    block_6.append(range(start_range + 831, stop_range + 831))
    block_7.append(range(start_range + 1562, stop_range + 1562))
    block_8.append(range(start_range + 1587, stop_range + 1587))
    block_9.append(range(start_range + 1612, stop_range + 1612))
    start_range += 71
    i += 1

horizontal_win_conditions = [
    [block_1, block_2, block_3], 
    [block_4, block_5, block_6],
    [block_7, block_8, block_9]
]

vertical_win_conditions = [
    [block_1, block_4, block_7], 
    [block_2, block_5, block_8],
    [block_3, block_6, block_9]
]

diagonal_win_conditions = [
    [block_1, block_5, block_9],
    [block_3, block_5, block_7]
]