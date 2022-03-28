def submain():
    top = '1'
    top_center = top.center(20, " ")
    print(top_center,end='')
    for i in range(10):
        star = '1' * (2*i)
        center_star = star.center(20, " ")
        print(center_star)
    print('        ||||')
    print('        ||||')
