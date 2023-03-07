def confirm():
    print('请勾选需要购买的商品\n勾选好后输入 y 并回车等待程序购买\n>', end=' ')
    select = ''
    while select != 'y':
        select = input()
