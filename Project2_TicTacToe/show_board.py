def show_board(my_list):
    N = 3
    print('=' * 10)
    print('\n'.join([' |'.join(i) for i in zip(*[iter(my_list)] * N)]))
    print('=' * 10)