from get_route import get_path  # 获取路线的方法
from raw_data import all_point  # 所有的坐标点
from raw_data import all_raw_cargo  # 所有的原材料的set集合
from raw_data import all_finished_cargo  # 所有产成品的set集合
from raw_data import point
import datetime


def get_path_list(info, DICT):
    """获取外部输入信息并返回一个汽车每段的轨迹.
    由于从O到三个分支的时间一样因此分段
    Args:

    Returns:
        一个list,每个元素是一段路程字典包括,起点、终点、所需时间、使用的方式
        由于有些路段可以选择水路和铁路所以设置为999.
    """
    # info = input('请依次输入起点,终点,数量,种类,最早提货时间,最晚到货时间\n用空格隔开')
    info_list = info.split()
    print(info_list)
    if not(info_list[0] in all_point) or not(info_list[1] in all_point):
        print('地点信息不正确,请重新检查')
    elif not(info_list[2] in all_finished_cargo) and not(info_list[2] in all_raw_cargo):
        print('未知货物请检查')
    # time_limit = info_list[5]-info_list[4]
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

    typess = info_list[2]
    amount = int(DICT['##amount##'])
    route_list = get_path(info_list[0], info_list[1])  # 返回路径列表
    if len(route_list) == 0:
        print('找不到路径')
    else:
        total_length = []
        long = 0  # 统计长度
        temp_from = False
        temp_to = False
        for i in range(0, len(route_list)-1):
            if route_list[i] == 'D' or route_list[i+1] == 'D' or route_list[i] == 'E' or route_list[i+1] == 'E':
                if route_list[i+1] == 'D' and temp_to != 'D' and temp_from and temp_to:
                    # print('apush')
                    temp_dic = {
                        'many_way': False,  # 是否可以有多种方式
                        'from': temp_from,
                        'to': temp_to,
                        'distance': long,
                        'time_cost': 2,  # 说用的时间
                        'by': 'car',  # 使用的方式
                        'type': typess,
                        'amount': amount,
                        'earliest_time': earliest_time,
                        'latest_time': latest_time,
                    }
                    total_length.append(temp_dic)
                    # earliest_time += temp_dic['time_cost']
                # print('bpush')
                temp_dic = {
                    'many_way': True,  # 是否可以有多种方式
                    'from': route_list[i],
                    'to': route_list[i+1],
                    'distance': point[route_list[i]][route_list[i+1]],
                    'time_cost': 2 if time_limit < 6 else 3,  # 说用的时间
                    'by': 'car' if time_limit < 6 else 'train',  # 使用的方式
                    'type': typess,
                    'amount': amount,
                    'earliest_time': earliest_time,
                    'latest_time': latest_time,
                }
                total_length.append(temp_dic)
                # earliest_time += temp_dic['time_cost']
                temp_from = False
                temp_to = False
                long = 0

            elif (route_list[i] == 'A_O' or route_list[i] == 'B_O') and (i != 0 and i != len(route_list)-1) and (temp_from and temp_to):
                temp_dic = {
                    'many_way': False,  # 是否可以有多种方式
                    'from': temp_from,
                    'to': temp_to,
                    'distance': long,
                    'time_cost': 2,  # 说用的时间
                    'by': 'car',  # 使用的方式
                    'type': typess,
                    'amount': amount,
                    'earliest_time': earliest_time,
                    'latest_time': latest_time,
                }
                total_length.append(temp_dic)
                # earliest_time += temp_dic['time_cost']
                temp_from = route_list[i]
                temp_to = route_list[i+1]
                long = point[route_list[i]][route_list[i+1]]

            else:
                if not temp_from:
                    temp_from = route_list[i]
                temp_to = route_list[i+1]
                long += point[route_list[i]][route_list[i+1]]
        if temp_from and temp_to:
            # print('dpush')

            temp_dic = {
                'many_way': False,  # 是否可以有多种方式
                'from': temp_from,
                'to': temp_to,
                'distance': long,
                'time_cost': 2,  # 说用的时间
                'by': 'car',  # 使用的方式
                'type': typess,
                'amount': amount,
                'earliest_time': earliest_time,
                'latest_time': latest_time,
            }
            total_length.append(temp_dic)
            # earliest_time += temp_dic['time_cost']
        # for i in total_length:
            # print(i)
        return total_length, typess
# get_path_list()

# 时间不统一,所有的公司时间流逝不同
# 车的组合问题
#
