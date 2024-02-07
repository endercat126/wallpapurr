#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#                            /l、      
#     _ || _  _  _     _ _  (ﾟ､ 。 7   
# \)/(_||||_)(_||_)|_|| |    l  ~ヽ  　
#         |     |            じしf_,)ノ
# 
# Simple wallpaper changer for many different platforms
#
# By Ender~chan
# This software is licensed under the MIT license

import os
import sys
import flet
import time
import tomllib

config = {}

def load_config() -> dict:
    try:
        with open("config.toml", "rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        with open("$XDG_CONFIG_HOME/wallpapurr/config.toml", "rb") as f:
            return tomllib.load(f)

def gui(page: flet.Page):
    page.title = "Wallpapurr"
    page.vertical_alignment = flet.MainAxisAlignment.START
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.window_width = 500
    page.window_height = 400
    page.window_resizable = True

    page.theme = flet.Theme(
        color_scheme_seed="gray",
    )

    page.add(flet.Text("Choose a wallpaper"))

    page.update()


def main():
    global config
    config = load_config()

    if config["general"]["force_x11"] == True:
        os.environ["GDK_BACKEND"] = "x11"

    flet.app(target=gui)


if __name__ == "__main__":
    main()