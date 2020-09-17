import datetime
d0 = datetime.datetime.strptime('2018-1-1', '%Y-%m-%d')
d0.strftime('%Y-%m-%d')


def input_info(DICT):
    info = input('请依次输入起点,终点,数量,种类,最早提货时间,最晚到货时间\n用空格隔开')
    ##托运公司##
    info_list = info.split()
    d0 = datetime.datetime.strptime('2018-1-1', '%Y-%m-%d')
    earliest_time = (datetime.datetime.strptime(
        info_list[4], '%Y-%m-%d')-d0).days
    latest_time = (datetime.datetime.strptime(
        info_list[5], '%Y-%m-%d')-d0).days
    time_limit = latest_time-earliest_time
    # import datetime

    # d1 = datetime.datetime.strptime('2012-03-05', '%Y-%m-%d')
    # d2 = datetime.datetime.strptime('2012-1-02', '%Y-%m-%d')
    # delta = d1 - d2
    # print (delta.days)
    # print(latest_time-earliest_time)

    type = info_list[3]
    amount = int(info_list[2])

    return info, DICT
