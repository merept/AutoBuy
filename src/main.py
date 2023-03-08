from autobuy.jd import JingDong
from autobuy.tb import TaoBao

time_to_buy = '2023-03-07 18:30:00.00000000'

if __name__ == '__main__':
    with open('time.txt', 'r') as file:
        time_to_buy = file.readline()
    print(f'预定的购买时间为 {time_to_buy}')
    print('选择要购买的网站:\n1.淘宝\n2.京东\n>', end=' ')
    select = input()
    TaoBao(time_to_buy).buy() if select == '1' else JingDong(time_to_buy).buy()
