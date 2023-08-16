# -*- coding: utf-8 -*-
"""
Created on 2023/8/9
@author : runyangwu
@file : api.py
@description : 接口
"""
from flask import Flask, request
import dice

app = Flask(__name__)


@app.route("/GetDiceResultV1", methods=["POST"])
def get_dice_result_v1():
    cmd = request.form.get('cmd')
    if cmd:
        return str(dice.roll_dice_v1(cmd))
    else:
        return str(dice.roll_dice_v1())


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
