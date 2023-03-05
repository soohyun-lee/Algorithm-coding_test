# 미세먼지 농도 - 좋음 : 30 이하 , 보통 31-80, 나쁨 81-150, 매우나쁨 151이상
# 초미세먼지 농도 - 좋음 : 15 이하 , 보통 16-35, 나쁨 36-75, 매우나쁨 76이상

# 민우는 매일 외출을 하는데 미세먼지나 초미세먼지의 농도가 어느 하나라도 나쁨 이상으로 올라가면 마스크를 착용합니다. 새 마스크를 착용한 후 이틀 후 까지는 재사용을 합니다. 미세먼지/초미세먼지의 농도가 둘다 매우나쁨 인 경우 사용하던 마스크는 그날까지만 쓰고 폐기합니다.

# 미세먼지/초미세먼지 농도에 대한 예보를 담고 있는 2차원 정수 배열 atmos가 매게변수로 주어집니다. 이때 민우에게 필요한 마스크의 갯수를 return 하는 함수를 작성해주세요.

# atmos의 길이는 1이상 1000이하입니다. atmos에는 예보 첫날부터 마지막날까지의 미세먼지/초미세먼지 농도가 차례대로 담겨있습니다. atmos의 원소들은 [a,b]의 형태입니다.a는 미세먼지의 농도, b는 초 미세먼지의 농도입니다. 


def count_masks(atmos):
    mask_count = 0
    mask_expire = 0  # 마스크 만료일
    for a, b in atmos:
        if a >= 151 and b >= 76:  # 미세먼지나 초미세먼지 농도가 매우나쁨 이상인 경우
            mask_count += 1
            # mask_expire = 2  # 새 마스크를 착용한 후 이틀간 재사용 가능
        elif mask_expire > 0:  # 마스크를 사용 중이며 아직 만료일이 지나지 않은 경우
            mask_expire -= 1
        elif a >= 81 or b >= 36:  # 미세먼지나 초미세먼지 농도가 나쁨 이상인 경우
            mask_count += 1
            mask_expire = 2  # 새 마스크를 착용한 후 이틀간 재사용 가능
    return mask_count
    
    
print(count_masks([[80,35],[70,38],[100,41],[75,30],[160,80],[77,29],[181,68],[151,76]]))
print(count_masks([[30,15],[80,35]]))




# def solution(atmos):
#     masks = 0
#     mask_duration = 0

#     for i in range(len(atmos)):
#         fine_dust_level = get_fine_dust_level(atmos[i][0])
#         strong_fine_dust = get_strong_fine_dust_level(atmos[i][1])

#         if fine_dust_level == 3 or strong_fine_dust == 3:
#             masks += 1
#             mask_duration = 2
            
#         elif mask_duration > 0:
#             mask_duration -= 1

#     return masks

# def get_fine_dust_level(dust):
#     if dust <= 30:
#         return 0

#     elif dust <= 80:
#         return 1

#     elif dust <= 150:
#         return 2

#     else:
#         return 3
    
# def get_strong_fine_dust_level(dust):
#     if dust <= 15:
#         return 0

#     elif dust <= 35:
#         return 1

#     elif dust <= 75:
#         return 2

#     else:
#         return 3
def solution(atmos):
    masks = 0
    mask_duration = 0

    for i in range(len(atmos)):

        if mask_duration > 0:
            if atmos[i][0] >= 151 and atmos[i][1] >= 76:
                mask_duration == 0
            else:
                mask_duration -= 1
    
        elif mask_duration == 0:
            if atmos[i][0] >= 151 and atmos[i][1] >= 76:
                masks += 1

            elif atmos[i][0] >= 81 or atmos[i][1] >= 36:
                masks += 1
                mask_duration += 2


    return masks