# -*- coding: utf-8 -*-
"""
Created on 2023/8/7
@author : runyangwu
@file : dndlib.py
@description : DND小工具
"""
import random
import logging
import re

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %A %H:%M:%S")


def _replace_func(match):
    captured_string = match.group(1)  # 获取捕获到的字符串
    logging.debug(f"捕获到的字符串为{captured_string}")
    # 根据捕获到的字符串进行替换
    count, dx = [int(i) for i in captured_string.split("d")]
    logging.debug(f"count={count}, dx={dx}")
    roll_list = [random.randint(1, dx) for _ in range(count)]
    logging.debug(f"{count}个{dx}面骰子的投掷结果具体为：{roll_list}")
    return str(sum(roll_list))

def roll_dice(cmd: str = "1d6"):
    """
    投掷骰子
    :param cmd: 投掷骰子的命令标准格式如下：3 * (3d4 + 1) + 1，默认投掷1个最常见的6面骰子
    :return: `int` 本次投掷获得的点数
    """
    # 格式化输入的投掷命令
    cmd = cmd.lower()
    logging.info(f"投掷命令为：{cmd}")
    pattern = r"(\d+d\d+)"
    new_cmd = re.sub(pattern, _replace_func, cmd)
    logging.info(f"解析后的投掷命令为：{new_cmd}")
    res = eval(new_cmd)
    logging.info(f"投掷结果为：{res}")
    return res


if __name__ == '__main__':
    roll_dice()
