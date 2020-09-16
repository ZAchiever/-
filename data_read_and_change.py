import pandas as pd


def change_data(full_car_task):
    import pandas as pd
    car = pd.read_excel('car.xlsx', sheet_name=0, index_col=0)
    all_car = list(car.index)
    A_car = []
    B_car = []
    C_car = []
    for i in all_car:
        if i[0] == 'A':
            A_car.append(i)
        elif i[0] == 'B':
            B_car.append(i)
        elif i[0] == 'C':
            C_car.append(i)
    driver = pd.read_excel('driver.xlsx', sheet_name=0, index_col=0)
    for i in full_car_task:
        if i['car_type'] == 'A':
            for j in A_car:
                start_time = i['earliest_time']
                for t in range(i['earliest_time'], i['latest_time']-i['last_time_cost']):
                    time_list = []  # 工作时间列表
                    for k in range(start_time, start_time+i['last_time_cost']):
                        time_list.append(k)
                    work_time = list(map(int, list(car.loc[j, 'work_day'])))
                    if not set(time_list) & set(work_time):
                        car.loc[j, 'work_day'] = list(
                            set(time_list) | set(work_time))
                        car.loc[j, 'total_distance'] = int(
                            car.loc[j, 'total_distance'])+i['last_distance']

                        car.loc[j, 'last_point'] = i['to']
                        return
