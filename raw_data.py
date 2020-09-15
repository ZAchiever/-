point = {
    'D': {
        'A_O': 350,
        'B_O': 350,
        'E': 3000,
    },
    'E': {
        'D': 3000,
    },
    'A_O': {
        'D': 350,
        'A_XB1': 120,
        'A_XN1': 200,
        'A_DF1': 150,
    },
    'A_XB1': {
        'A_O': 120,
        'A_XB2': 70,
    },
    'A_XB2': {
        'A_XB1': 70,
        'A_XB3': 50,
    },
    'A_XB3': {
        'A_XB2': 50,
    },
    'A_XN1': {
        'A_O': 200,
        'A_XN2': 50,
    },
    'A_XN2': {
        'A_XN1': 50,
    },
    'A_DF1': {
        'A_O': 150,
        'A_DF2': 50,
    },
    'A_DF3': {
        'A_DF2': 50,
    },
    'A_DF2': {
        'A_DF1': 50,
        'A_DF3': 50,
    },
    'B_O': {
        'D': 350,
        'B_XB1': 120,
        'B_XN1': 200,
        'B_DF1': 150,
    },
    'B_XB1': {
        'B_O': 120,
        'B_XB2': 70,
    },
    'B_XB2': {
        'B_XB1': 70,
        'B_XB3': 50,
    },
    'B_XB3': {
        'B_XB2': 50,
    },
    'B_XN1': {
        'B_O': 200,
        'B_XN2': 50,
    },
    'B_XN2': {
        'B_XN1': 50,
    },
    'B_DF1': {
        'B_O': 150,
        'B_DF2': 50,
    },
    'B_DF3': {
        'B_DF2': 50,
    },
    'B_DF2': {
        'B_DF1': 50,
        'B_DF3': 50,
    }
}
all_point = set(point.keys())
all_finished_cargo = set(['P1', 'P2', 'P3', 'p4'])
all_raw_cargo = set([])

car_a = {
    'weight': 10,
    'amount_finished': 550,
    'amount_raw': 720,
    'empty_cost': 25,
    'full_cost': 30,
}
car_b = {
    'weight': 8,
    'amount_finished': 450,
    'amount_raw': 600,
    'empty_cost': 20,
    'full_cost': 25,
}
car_c = {
    'weight': 5,
    'amount_finished': 300,
    'amount_raw': 400,
    'empty_cost': 20,
    'full_cost': 15,
}





