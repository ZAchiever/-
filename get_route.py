from raw_data import point as route
result = []
done = False


def path_finder(from_point, to_point, last_point):
    global result
    global done
    # result.insert(0,'Aa')
    for i in route[from_point]:
        if i == last_point or i == from_point:
            continue
        # print(i+'   from : '+from_point+'   '+str(done))
        if i == to_point:
            done = True
            return result.insert(0, i)
        else:
            path_finder(i, to_point, from_point)
            if done:
                return result.insert(0, i)


def get_path(from_point, to_point):
    global result, done
    result = []
    done = False
    path_finder(from_point, to_point, 'null')
    result.insert(0, from_point)
    print(result)
    return result


# point_A=input('请输入A的坐标');
# point_B=input('请输入B的坐标');
# point_A = 'A_DF1'
# point_B = 'A_XB3'
# get_path(point_A, point_B)
