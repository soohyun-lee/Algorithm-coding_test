# def solution(progresses, speeds):
#     success = int(100)
#     remain_progress = []
#     cnt = []
#     day = []
#     for i in progresses:
#         remain_progress.append(success - int(i))
#     for j in range(len(remain_progress)):
#         for y in range(len(speeds)):
#             if remain_progress[j] % speeds[y]:
#                 day.append(remain_progress[j] // speeds[y] + 1)
#             else:
#                 day.append(remain_progress[j] // speeds[y])


progresses = [93, 30, 55]
speeds = [2, 30, 10]
success = int(100)
remain_progress = []
day = []
for i in progresses:
    remain_progress.append(success - int(i))
for j in range(len(remain_progress)):
    # for y in range(len(speeds)):
    if remain_progress[j] % speeds[j] != 0:
        day.append(remain_progress[j] // speeds[j] + 1)
    else:
        day.append(remain_progress[j] // speeds[j])

print(day)