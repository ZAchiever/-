#!/usr/bin/python
# -- coding: utf-8 --**

from get_info import get_path_list
import raw_data as data
from car_choose import car_task
# from email import interaction
from data_read_and_change import change_data


def main():

    all_full_car_task = []
    all_not_full_car_task = []
    path_info = get_path_list()  # 获取需要段路
    car_task_list = car_task(path_info)  # 获取以车为单位的任务
    for i in car_task_list:
        if i['full']:
            all_full_car_task.append(i)
        else:
            all_not_full_car_task.append(i)
    for i in all_full_car_task:
        change_data(i)


if __name__ == '__main__':
    main()
