#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""简单测试脚本：演示打印功能、变量、循环和函数调用"""

# 1. 基础打印
print("=== 基础打印测试 ===")
print("Hello, World!")  # 打印字符串
print(123)             # 打印数字
print(3.14159)         # 打印浮点数
print(True)            # 打印布尔值
print(None)            # 打印空值


# 2. 变量打印
print("\n=== 变量打印测试 ===")
name = "测试脚本"
version = 1.0
is_debug = True

# 直接打印变量
print("名称:", name)
print("版本:", version)
print("调试模式:", is_debug)

# f-string 格式化打印（Python 3.6+）
print(f"格式化输出: {name} v{version} (调试: {is_debug})")


# 3. 循环打印
print("\n=== 循环打印测试 ===")
for i in range(5):  # 打印 0-4
    print(f"循环第 {i+1} 次: i = {i}")


# 4. 函数调用与打印
print("\n=== 函数打印测试 ===")
def add(a, b):
    """简单加法函数"""
    result = a + b
    print(f"函数 add({a}, {b}) = {result}")  # 函数内打印
    return result

# 调用函数并打印返回值
sum1 = add(2, 3)
sum2 = add(10, 20)
print("函数返回值累加:", sum1 + sum2)  # 打印函数返回值的计算结果


# 5. 结束提示
print("\n=== 所有测试完成 ===")
