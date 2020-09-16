import raw_data as data


def car_task(path_info):
    """返回一个以汽车为单位的任务的对象
    目前只写了不需要考虑铁路和水路的路段,即不到D的运输任务
    Args:
        path_info:点到点的任务,一个列表元素为字典
    Return:
        car_task_list:一个列表元素为字典
        元素例子:{
                    'full': full,#是否装满
                    'car_type': 'B',#汽车类型
                    'from': last_start_point,#任务的起点
                    'to': last_end_point,
                    'type': [path_info[0]['type']],#货物种类
                    'amount': temp_amount,#这个车上装的量
                    'earliest_time': path_info[0]['earliest_time'],#最早的提货时间
                    'latest_time': path_info[0]['latest_time'],#最晚的到货时间
                }

    """
    simple = True  # 是否会经过D点
    # print('aaaaa')
    for i in path_info:
        if i['many_way'] == True:
            simple = False
    if simple or True:
        a = 0
        b = 0
        c = 0
        if path_info[0]['type'] in ['P1', 'P2', 'P3', 'P4']:
            a = data.car_a['amount_finished']
            b = data.car_b['amount_finished']
            c = data.car_c['amount_finished']
        else:
            a = data.car_a['amount_raw']
            b = data.car_b['amount_raw']
            c = data.car_c['amount_raw']
        last_time_cost = 0
        last_distance = 0
        last_start_point = path_info[0]['from']
        last_end_point = path_info[len(path_info)-1]['to']
        for i in path_info:
            last_distance += i['distance']
            last_time_cost += i['time_cost']

        type = []
        amount = path_info[0]['amount']

        car_task_list = []
        while(amount != 0):
            # print('bbbb')
            if amount >= 2*a:
                amount -= a
                car_task_list.append({
                    'full': True,
                    'car_type': 'A',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': a,

                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                continue
            elif amount <= 2*a and amount > a+b:
                # 两a
                car_task_list.append({
                    'full': True,
                    'car_type': 'A',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': a,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                temp_amount = amount-a
                full = False
                if temp_amount == a:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'A',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': temp_amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= a+b and amount > 2*b:
                # 1a 1b
                car_task_list.append({
                    'full': True,
                    'car_type': 'A',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': a,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                temp_amount = amount-a
                full = False
                if temp_amount == b:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'B',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': temp_amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0

            elif amount <= 2*b and amount > b+c:
                # 两个个b车
                car_task_list.append({
                    'full': True,
                    'car_type': 'B',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': b,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                temp_amount = amount-b
                full = False
                if temp_amount == b:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'B',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': temp_amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= b+c and amount > 2*c:
                # 1b 1c
                car_task_list.append({
                    'full': True,
                    'car_type': 'B',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': b,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                temp_amount = amount-b
                full = False
                if temp_amount == c:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'C',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': temp_amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= 2*c and amount > a:
                car_task_list.append({
                    'full': True,
                    'car_type': 'C',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': c,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                temp_amount = amount-c
                full = False
                if temp_amount == c:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'C',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': temp_amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= a and amount > b:
                full = False
                if temp_amount == a:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'A',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= b and amount > c:
                full = False
                if temp_amount == b:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'B',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
            elif amount <= c:
                full = False
                if temp_amount == c:
                    full = True
                car_task_list.append({
                    'full': full,
                    'car_type': 'C',
                    'from': last_start_point,
                    'to': last_end_point,
                    'type': [path_info[0]['type']],
                    'amount': amount,
                    'earliest_time': path_info[0]['earliest_time'],
                    'latest_time': path_info[0]['latest_time'],
                    'last_time_cost': last_time_cost,
                    'last_distance': last_distance,
                })
                amount = 0
        for j in car_task_list:
            print(j)
        return car_task_list
