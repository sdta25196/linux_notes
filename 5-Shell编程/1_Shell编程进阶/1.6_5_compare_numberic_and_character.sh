#!/bin/bash
## 时间: 2016-04-04 22:35 Mon
## 目的: 测试数字和字符的比较方法
## 理论止的测试结果: 数字应该使用-eq，而字符使用==比较合适
## 测试结果: 字符比较只能使用==， 而数字比较使用==也是没有问题的，不确定是否把num作为字符来比较的嫌疑

read -p "Please input a numberic: " num
#if [ $num == 888 ]; then 
if [ $num -eq 888 ]; then 
    echo "I know your input number is 888"
else
    echo "I don't know your input number."
fi

read -p "Please input some character: " ch
#if [ "$ch" == hello ]; then
if [ "$ch" == "hello" ]; then
    echo "Your input characters is hello"
else
    echo "I don't know your input characters."
fi
