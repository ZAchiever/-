#!/usr/bin/python
# -- coding: utf-8 --**

from get_info import get_path_list
import raw_data as data
from car_choose import car_task
# from email import interaction
from data_save import change_data
from out_put_docs import out_put_doc
from input_info import input_info


def main():
    all_full_car_task = []
    all_not_full_car_task = []
    info, DICT = input_info()
    path_info = get_path_list(info)  # 获取需要段路
    car_task_list = car_task(path_info)  # 获取以车为单位的任务
    last_day = 0
    for i in car_task_list:
        last_day = change_data(i, last_day)

    out_put_doc(car_task_list)


if __name__ == '__main__':
    main()
