"""
學習目標:
1. 學習撰寫模組，在python，一個檔案或是一個資料夾都可被視為一個模組。
2. 用test_case來測試自己寫的東西對不對
核心概念:先畫靶再射箭，先設定好自己要的結果，再開始coding。
"""


def get_constellation(month, day) -> str:
    """
    根據生日回傳正確的星座
    牡羊座	3月21日～4月20日
    金牛座	4月21日～5月20日
    雙子座	5月21日～6月20日
    巨蟹座	6月21日～7月22日
    獅子座	7月23日～8月22日
    處女座	8月23日～9月22日
    天秤座	9月23日～10月22日
    天蠍座	10月23日～11月22日
    射手座	11月23日～12月22日
    魔羯座	12月23日～1月21日
    水瓶座	1月22日～2月19日
    雙魚座	2月20日～3月20日
    """
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    constellations = ("摩羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蝎座", "射手座", "魔羯座")
    if day < dates[month-1]:
        return constellations[month-1]
    else:
        return constellations[month]

import math
def get_each_number(number: int) -> []:
    """
    輸入一個正整數，然後將每一位數分開。
    ex get_each_number(1920) 
    return [1,9,2,0]
    """
    l = []
    while (number>0):
        l.append(number%10)
        number=math.floor(number/10)
    l=list(reversed(l))
    return l


def get_life_number(year=1900, month=1, day=1) -> int:
    """
    會回傳一個生命靈數，生命靈數的計算方式是出生年月日的每一個數字的總和，不斷加總至個位數。
    ex 1995 12 13 -> 1+9+9+5+1+2+1+3 = 31 -> 3+1 =4
    這樣生命靈數就是4
    """
    n1 = get_each_number(year)
    n2 = get_each_number(month)
    n3 = get_each_number(day)
    i = 0
    j = 0
    k = 0
    life_number_n1 = 0
    life_number_n2 = 0
    life_number_n3 = 0
    while i < len(n1):
        life_number_n1 += n1[i]
        i += 1
    while j < len(n2):
        life_number_n2 += n2[j]
        j += 1
    while k < len(n3):
        life_number_n3 += n3[k]
        k += 1
    m = 0
    n = 0
    o = 0
    life_number_n1_ = 0
    life_number_n2_ = 0
    life_number_n3_ = 0
    if life_number_n1>9:
        life_number_n1 = get_each_number(life_number_n1)
        while m < 2:
            life_number_n1_ += life_number_n1[m]
            m += 1
        life_number_n1 = life_number_n1_
    if life_number_n2 > 9:
        life_number_n2 = get_each_number(life_number_n2)
        while n < 2:
            life_number_n2_ += life_number_n2[n]
            n += 1
        life_number_n2 = life_number_n2_
    if life_number_n3 > 9:
        life_number_n3 = get_each_number(life_number_n3)
        while o < 2:
            life_number_n3_ += life_number_n3[o]
            o += 1
        life_number_n3 = life_number_n3_
        
    life_number_1 = life_number_n1 + life_number_n2 + life_number_n3
    p = 0
    life_number_1_ = 0
    if life_number_1 > 9:
        life_number_1 = get_each_number(life_number_1)
        while p < 2:
            life_number_1_ +=life_number_1[p]
            p+=1
        life_number_1 = life_number_1_
    life_number = life_number_1
    return life_numbr

