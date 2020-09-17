#!/usr/bin/python
# -- coding: utf-8 --**

from get_info import get_path_list
import raw_data as data
from car_choose import car_task
# from email import interaction
from data_save import change_data
# from out_put_docs import out_put_doc
from input_info import input_info

DICT = {}
DICT = {
    "##托运公司##": '##bug##',
    '##地址##': '##bug##',
    '##货物1##': '##bug##',
    '##货物2##': '##bug##',
    '##货物3##': '##bug##',
    '##1的数量##': '##bug##',
    '##2的数量##': '##bug##',
    '##3的数量##': '##bug##',
    '##from##': '##bug##',
    '##to##': '##bug##',
    '##取货时间##': '##bug##',
    '##收货人##': '##bug##',
    '##到货时间##': '##bug##',
    '##总价格##': '##bug##',
    '##y##': '##bug##',
    '##m##': '##bug##',
    '##d##': '##bug##',
    '##大写总价格##': '##bug##',
}


def main():
    global DICT
    all_full_car_task = []
    all_not_full_car_task = []
    info, DICT = input_info(DICT)
    print('传入的info')
    print(info)
    path_info = get_path_list(info)  # 获取需要段路
    print('获取的路段')
    for i in path_info:
        print(i)
    car_task_list = car_task(path_info)  # 获取以车为单位的任务
    print('获取的任务')
    for i in car_task_list:
        print(i)
    last_day = 0
    for i in car_task_list:
        last_day = change_data(i, last_day)

    # out_put_doc(car_task_list)


if __name__ == '__main__':
    main()
