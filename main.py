#!/usr/bin/python
# -- coding: utf-8 --**

from get_info import get_path_list
import raw_data as data
from car_choose import car_task
# from email import interaction
from data_save import change_data
from out_put_docs import out_put_doc
from input_info import input_info
import pandas as pd


DICT = {}
DICT = {
    '##托运公司##': '##bug##',
    '##地址##': '##bug##',
    '##货物1##': '##bug##',
    '##货物2##': '',
    '##货物3##': '',
    '##货物4##': '',
    '##1的数量##': '##bug##',
    '##2的数量##': '',
    '##3的数量##': '',
    '##4的数量##': '',
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
    '##NO##': '',
    'total_p': 0,
    '##amount##': 0,
}


def main():
    global DICT
    all_full_car_task = []
    all_not_full_car_task = []
    info, DICT = input_info(DICT)
    task_list = pd.read_excel(
        'storage\\task_list.xlsx', sheet_name=0, index_col=0)
    DICT['##NO##'] = str(len(task_list.index)+20000)
    print('传入的info')
    print(info)
    path_info, typess = get_path_list(info, DICT)  # 获取需要段路
    print('获取的路段')
    for i in path_info:
        print(i)
    car_task_list = car_task(path_info)  # 获取以车为单位的任务
    print('获取的任务')

    total_money = 0
    cargo_type = ''
    if typess in ['P1', 'P2', 'P3', 'P4']:
        cargo_type = 'finish'
    else:
        cargo_type = 'raw'

    for i in car_task_list:
        if i['car_type'] in ['A', 'B', 'C']:
            total_money += data.price_map['A'][cargo_type][i['car_type']
                                                           ]*i['last_distance']
        else:
            total_money += data.price_map['B'][cargo_type][i['car_type']
                                                           ]*i['last_distance']*i['amount']
        print(i)

    DICT['##大写总价格##'] = data.digital_to_chinese(total_money)
    DICT['##总价格##'] = str(round(total_money*1.2, 3)) + \
        '(税后价'+str(round(total_money*1.09*1.2, 3))+')'
    last_day = 0
    for i in car_task_list:
        last_day, DICT = change_data(i, last_day, DICT)

    out_put_doc(DICT)
    task_list.loc[DICT['##NO##'], '托运公司'] = DICT['##托运公司##']
    task_list.loc[DICT['##NO##'], '起点'] = DICT['##from##']
    task_list.loc[DICT['##NO##'], '终点'] = DICT['##to##']
    task_list.loc[DICT['##NO##'], '类型'] = cargo_type
    task_list.loc[DICT['##NO##'], '起运时间'] = DICT['##取货时间##']
    task_list.loc[DICT['##NO##'], '到达时间'] = DICT['##到货时间##']

    task_list.loc[DICT['##NO##'], '总量'] = DICT['##amount##']
    task_list.loc[DICT['##NO##'], '总油耗'] = str(DICT['total_p'])
    task_list.to_excel('storage\\task_list.xlsx')


if __name__ == '__main__':
    main()
