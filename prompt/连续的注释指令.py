# 打印当前的购物车列表shopping_cart.
# 购物车内有多个商品，商品的属性为：\
# 'name' , 'quantity',\
# 'price'.
# 让客户输入需要删除的商品名字.
# 从购物车列表删除该项目.
# 如果用户输入的商品名字不在购物车列表中，打印出错误信息.
# 打印更新的购物车列表.

def main():
    shopping_cart = [
        {'name': 'apple', 'quantity': 3, 'price': 5},
        {'name': 'banana', 'quantity': 2, 'price': 3},
        {'name': 'pear', 'quantity': 1, 'price': 6}
    ]
    print(shopping_cart)
    name = input('请输入需要删除的商品名字：')
    for item in shopping_cart:
        if item['name'] == name:
            shopping_cart.remove(item)
            break
    else:
        print('商品名字不在购物车列表中')
    print(shopping_cart)

main()    
