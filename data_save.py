from raw_data import get_cost
from raw_data import get_distance
from get_route import get_path
import datetime
import pandas as pd
# history = pd.read_excel('history.xlsx', sheet_name=0, index_col=0)
# history.to_excel('storage\\car_2.xlsx')


def change_data(full_car_task, last_day):
    history = pd.read_excel('storage\\history.xlsx', sheet_name=0, index_col=0)
    all_history = list(history.index)
    if full_car_task['car_type'] == 'train':
        last_day += 3

        history.loc[len(
            all_history), 'do_task_point'] = full_car_task['from']

        history.loc[len(
            all_history), 'last_ponit'] = full_car_task['to']
        history.loc[len(
            all_history), 'by'] = 'train'
        history.to_excel('storage\\history.xlsx')

    else:
        car = pd.read_excel('storage\\car.xlsx', sheet_name=0, index_col=0)
        driver = pd.read_excel('storage\\driver.xlsx',
                               sheet_name=0, index_col=0)

        earliest_time = full_car_task['earliest_time']  # 最早的时间
        latest_time = full_car_task['latest_time']  # 最晚的时间
        last_time_cost = full_car_task['last_time_cost']  # 这个运输任务需要的总时间
        all_car = list(car.index)
        all_driver = list(driver.index)

        car_type = full_car_task['car_type']
        cars = []  # 所有对应种类的车型
        for i in all_car:
            if i[0] == car_type:
                cars.append(i)
        close_car = sorted(cars, key=lambda i: get_distance(
            get_path(car.loc[i, 'last_point'], full_car_task['from'])))  # 按距离排序
        for i in close_car:  # 按距离遍历寻找最优可以接单的car
            empty_car_distance = get_path(
                car.loc[i, 'last_point'], full_car_task['from'])
            empty_car_distance = get_distance(empty_car_distance)
            empty_car_need_time = 0  # 赶到上货地需要的时间#再加一段铁路运输的
            if empty_car_distance >= 270:
                empty_car_need_time = 2
            elif empty_car_distance >= 470:
                empty_car_need_time = 4
            elif empty_car_distance >= 820:
                empty_car_need_time = 6
            for t in range(earliest_time+empty_car_need_time, latest_time-last_time_cost):
                time_list = []  # 工作的时间列表
                for k in range(t, t+last_time_cost):
                    time_list.append(str(k))
                raw_info = str(car.loc[i, 'work_day'])
                car_unable = raw_info.split(',')
                if not set(time_list) & set(car_unable):  # 时间不相交可以选司机了
                    time_add = set(time_list) | set(car_unable)
                    # time_add.remove('nan')
                    new_time_unable = ''
                    for k in time_add:

                        if new_time_unable:
                            if str(k) != 'nan':
                                new_time_unable = new_time_unable+','+k
                        else:
                            new_time_unable = k
                    driver_alive = []
                    for d in all_driver:
                        driver_raw_info = str(driver.loc[d, 'work_day'])
                        driver_unable_time = driver_raw_info.split(',')

                        if not set(time_list) & set(driver_unable_time):  # 抓走合适的司机
                            driver_time_add = set(time_list) | set(
                                driver_unable_time)
                            # driver_time_add.remove('nan')
                            new_driver_time_unable = ''
                            for k in time_add:
                                if new_driver_time_unable:
                                    if str(k) != 'nan':
                                        new_driver_time_unable = new_time_unable+','+k
                                else:
                                    new_driver_time_unable = k
                            driver_total_time = int(
                                driver.loc[d, 'total_time'])
                            if driver_total_time < 250000:
                                driver_alive.append(d)
                                if len(driver_alive) == 2:  # 司机和汽车准备好了,开始填制表单
                                    print('开始载入信息')
                                    # 数据备份
                                    car.to_excel('storage\\car_0.xlsx')
                                    driver.to_excel('storage\\driver_0.xlsx')
                                    history.to_excel('storage\\history_0.xlsx')
                                    # 重写excel
                                    history.loc[len(
                                        all_history), 'car_point'] = car.loc[i, 'last_point']
                                    history.loc[len(
                                        all_history), 'do_task_point'] = full_car_task['from']
                                    history.loc[len(all_history), 'empty_p_cost'] = get_cost(
                                        empty_car_distance, car_type, True)
                                    history.loc[len(
                                        all_history), 'last_ponit'] = full_car_task['to']
                                    history.loc[len(
                                        all_history), 'total_distance'] = empty_car_distance+full_car_task['last_distance']
                                    history.loc[len(all_history), 'total_p_cost'] = get_cost(
                                        full_car_task['last_distance'], car_type, False)

                                    history.loc[len(
                                        all_history), 'driver'] = str(driver_alive[0])+','+str(driver_alive[1])
                                    history.loc[len(all_history), 'date'] = str(
                                        datetime.datetime(2018, 1, 1)+datetime.timedelta(days=t))
                                    history.loc[len(all_history), 'all_p'] = history.loc[len(
                                        all_history), 'empty_p_cost']+get_cost(full_car_task['last_distance'], car_type, False)
                                    history.loc[len(all_history),
                                                'by'] = i
                                    car.loc[i, 'work_day'] = new_time_unable
                                    car.loc[i, 'last_point'] = full_car_task['to']
                                    car.loc[i, 'total_distance'] = car.loc[i, 'total_distance'] + \
                                        empty_car_distance + \
                                        full_car_task['last_distance']
                                    for people in driver_alive:
                                        driver.loc[people, 'total_time'] = int(
                                            driver.loc[people, 'total_time'])+empty_car_need_time+last_time_cost
                                        driver.loc[people,
                                                   'work_day'] = new_driver_time_unable
                                        driver.loc[people, 'total_distance'] = int(
                                            driver.loc[people, 'total_distance'])+empty_car_distance+full_car_task['last_distance']
                                    car.to_excel('storage\\car.xlsx')
                                    driver.to_excel('storage\\driver.xlsx')
                                    history.to_excel('storage\\history.xlsx')
                                    return
    return last_day
