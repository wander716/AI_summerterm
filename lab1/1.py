# -*- coding: utf-8 -*-
"""
实验二：变量、输入与数据类型
目标：掌握变量、数据类型及输入输出

任务：
1) 通过命令行输入两个数字
2) 计算并输出它们的和、差、积、商
"""

def main():
    # ===== 步骤 1：获取用户输入（已写好） =====
    a_str = input("请输入第一个数字：")
    b_str = input("请输入第二个数字：")

    # ===== 步骤 2：将字符串转换为浮点数（已写好，含异常处理） =====
    try:
        # TODO: 将读入的a b变量转成浮点数，赋值给a和b
        # a = ...
        # b = ...
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("输入无效：请确保输入的是数字。")
        return

    # ===== 步骤 3：进行四则运算 =====
    # 已写好示例：计算并输出“和”
    add = a + b
    print(f"和：{round(add, 2)}")   # 示例输出，保留 2 位小数

    # ======= 下面三项留给你完成（挖空+注释指引）=======
    # 1) 计算“差”：请创建变量 sub 保存 a - b 的结果
    #  
    # TODO：在此处编写计算差的代码
    # sub = ...
    sub = a - b

    # 2) 计算“积”：请创建变量 mul 保存 a * b 的结果
    # 
    # TODO：在此处编写计算积的代码
    # mul = ...
    mul = a * b

    # 3) 计算“商”：先判断 b 是否为 0
    #    - 若 b != 0，则 div = a / b
    #    - 若 b == 0，则 div = "除数不能为 0"
    # TODO：在此处完成对 div 的计算与判断
    # if b != 0:
    #     ...
    # else:
    #     div = "除数不能为 0"
    if b != 0:
        div = a / b
    else:
        div = None

    # ===== 步骤 4：格式化输出结果 =====
    # 已示例：上面已经输出了“和”
    # 请补充输出“差、积、商”。下面是参考格式（完成后取消注释并替换 ...）：
    # print(f"差：{round(sub, 2)}")
    # ...
    print(f"差：{round(sub, 2)}")
    print(f"积：{round(mul, 2)}")
    if div is not None:
        print(f"商：{round(div, 2)}")
    else:
        print("商：除数不能为 0")
    

if __name__ == "__main__":
    # 在命令行执行：python calculator.py
    main()
