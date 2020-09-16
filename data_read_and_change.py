import pandas as pd
from get_route import get_path
from raw_data import get_distance
from raw_data import get_cost
# 未完成找最近的汽车


def change_data(full_car_task):
    car = pd.read_excel('car.xlsx', sheet_name=0, index_col=0)
    driver = pd.read_excel('driver.xlsx', sheet_name=0, index_col=0)
    history = pd.read_excel('task_history.xlsx', sheet_name=0, index_col=0)
    all_car = list(car.index)
    all_driver = list(driver.index)
    all_history = list(history.index)
    cars = {}
    cars['A'] = []
    cars['B'] = []
    cars['C'] = []
    for i in all_car:
        if i[0] == 'A':
            cars['A'].append(i)
        elif i[0] == 'B':
            cars['B'].append(i)
        elif i[0] == 'C':
            cars['C'].append(i)
    driver = pd.read_excel('driver.xlsx', sheet_name=0, index_col=0)

    for i in full_car_task:
        print(i)
        print(22222222222222222222222222222222222222222222)
        for j in cars[i['car_type']]:
            a = 0
            start_time = i['earliest_time']
            # 按照时间推进找最近的合适的司机和汽车
            for t in range(i['earliest_time'], i['latest_time']-i['last_time_cost']):

                time_list = []  # 工作时间列表
                for k in range(start_time, start_time+i['last_time_cost']):
                    time_list.append(k)
                # work_time = list(map(int, list(car.loc[j, 'work_day'])))
                print(car.loc[j, 'work_day'])
                print(type(car.loc[j, 'work_day']))
                work_time = []
                if not car.loc[j, 'work_day'] == 'nan':
                    work_time = []
                else:
                    work_time = [int(x) for x in list(car.loc[j, 'work_day'])]
                if not set(time_list) & set(work_time):
                    print(j+'接单了' + str(car.loc[j, 'work_day']))
                    print(str(set(time_list) | set(work_time)))
                    car.loc[j, 'work_day'] = 1
                    car.loc[j, 'work_day'] = str(list(
                        set(time_list) | set(work_time)))
                    car.loc[j, 'total_distance'] = int(  # 汽车总里程加入运输的那一段的路程
                        car.loc[j, 'total_distance'])+i['last_distance']
                    path2 = get_path(car.loc[j, 'last_point'], i['from'])
                    distance_arrive = get_distance(path2)  # 到达点的路程
                    path = get_path(i['from'], i['to'])
                    distance_work = get_distance(path)  # 运输的路程长度

                    count = 0
                    dri = []
                    for d in all_driver:
                        driver_work_time = []
                        if driver.loc[d, 'work_day'] == 'nan':
                            driver_work_time = []
                        else:
                            driver_work_time = list(
                                map(int, list(driver.loc[d, 'work_day'])))
                        if not set(time_list) & set(driver_work_time):
                            driver.loc[d, 'work_day'] = list(  # 工作时间载入
                                set(time_list) | set(work_time))
                            driver.loc[d, 'total_distance'] = int(  # 司机总里程计入
                                driver.loc[d, 'total_distance'])+i['last_distance']
                            driver.loc[d, 'total_time'] = int(  # 司机总时间计入
                                driver.loc[d, 'total_time'])+i['last_time_cost']
                            count += 1
                            dri.append[d]
                            history.loc[id, 'driver'] = dri
                            if count == 2:  # 汽车和人都找好了,记录并保存
                                id = len(all_history)
                                # 历史计入汽车起点
                                history.loc[id,
                                            'car_point'] = car.loc[j, 'last_point']
                                # 历史计入汽车上货点
                                history.loc[id, 'do_task_point'] = i['from']
                                history.loc[id, 'empty_p_cost'] = get_cost(
                                    distance_arrive, i['car_type'], True)  # 到上货点的油耗
                                history.loc[id, 'total_p_cost'] = get_cost(
                                    distance_work, i['car_type'], False)  # 运输过程中的油耗
                                history.loc[id, 'all_p'] = history.loc[id,
                                                                       'total_p_cost']+history.loc[id, 'empty_p_cost']
                                car.loc[j, 'last_point'] = i['to']  # 记录汽车最后的位置
                                car.loc[j, 'total_distance'] = int(
                                    car.loc[j, 'total_distance'])+i['last_distance']  # 计入总里程（加如空载的那一段
                                a = 1
                                car.to_excel('car.xlsx')
                                driver.to_excel('driver.xlsx')
                                history.to_excel('history.xlsx')
                                break
                    if a == 1:
                        break
            if a == 1:
                break
