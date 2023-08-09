# -*- coding: utf-8 -*-
"""
Created on 2023/8/9
@author : runyangwu
@file : api.py
@description : 接口
"""
from flask import Flask, request
import dndlib

app = Flask(__name__)


@app.route("/GetDiceResult", methods=["POST"])
def get_dice_result():
    cmd = request.form.get('cmd')
    if cmd:
        return str(dndlib.roll_dice(cmd))
    else:
        return str(dndlib.roll_dice())


if __name__ == '__main__':
    app.run()
