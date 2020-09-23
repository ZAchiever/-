import datetime
d0 = datetime.datetime.strptime('2018-1-1', '%Y-%m-%d')
d0.strftime('%Y-%m-%d')


def input_info(DICT):
    info = input('请依次输入起点,终点,种类(产成品为P1,原材料为M1),最早提货时间,最晚到货时间\n用空格隔开')
    ##托运公司##

    info_list = info.split()
    d0 = datetime.datetime.strptime('2018-1-1', '%Y-%m-%d')
    earliest_time = (datetime.datetime.strptime(
        info_list[3], '%Y-%m-%d')-d0).days
    latest_time = (datetime.datetime.strptime(
        info_list[4], '%Y-%m-%d')-d0).days
    time_limit = latest_time-earliest_time
    # import datetime

    # d1 = datetime.datetime.strptime('2012-03-05', '%Y-%m-%d')
    # d2 = datetime.datetime.strptime('2012-1-02', '%Y-%m-%d')
    # delta = d1 - d2
    # print (delta.days)
    # print(latest_time-earliest_time)

    type = info_list[2]
    # amount = int(info_list[2])
    amount = 0
    info2 = input('请依次输入你的公司名,你想要发往的公司名,你所在的教室地址用空格隔开\n')
    temp_type = 'qaq'
    temp_int = 1
    print('请输入类型和数量用空格隔开,例如M1:500(注意大小写,统一为大写),q为退出')
    while(temp_type != 'q' and temp_type != ''):
        temp_type = input('请输入类型和数量用空格隔开')
        if temp_type:
            types = temp_type.split()[0]
            amounts = int(temp_type.split()[1])

            DICT['##货物'+str(temp_int)+'##'] = types
            amount += amounts
            DICT['##'+str(temp_int)+'的数量##'] = str(amounts)
            temp_int += 1
    DICT['##amount##'] = amount
    info_list2 = info2.split()
    DICT["##托运公司##"] = info_list2[0]
    DICT["##收货人##"] = info_list2[1]
    DICT['##地址##'] = info_list2[2]
    # DICT['##货物1##'] = type
    # DICT['##1的数量##'] = str(amount)
    DICT['##from##'] = info_list[0]
    DICT['##to##'] = info_list[1]
    DICT['##取货时间##'] = info_list[3]
    DICT['##到货时间##'] = info_list[4]
    DICT['##y##'] = str(datetime.datetime.strptime(
        info_list[4], '%Y-%m-%d').year)
    DICT['##m##'] = str(datetime.datetime.strptime(
        info_list[4], '%Y-%m-%d').month)
    DICT['##d##'] = str(datetime.datetime.strptime(
        info_list[4], '%Y-%m-%d').day)
    return info, DICT
