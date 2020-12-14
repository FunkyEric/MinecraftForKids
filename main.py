from tkinter import Tk, Button
from superPlayer.mc_functions import *

name_lists = ['Eric']
player_lists = []
screen = Tk()
screen.geometry('400x800')
screen.title('MC plugins')
for name in name_lists:
    player_lists.append(Player(name))



def protect(players=player_lists):
    for player in players:
        player.protect()


def tower(players=player_lists):
    for player in players:
        player.tower()


def build_wall(players=player_lists):
    for player in players:
        player.build_wall()


def fast_leaves(players=player_lists):
    for player in players:
        player.fast_leaves()


def fall_water(players=player_lists):
    for player in players:
        player.fall_water()


def side_build(players=player_lists):
    for player in players:
        player.side_build()


def clear_wall(players=player_lists):
    for player in players:
        player.clear_wall()


def test(players=player_lists):
    for player in players:
        player.test()


def build_qrcode(players=player_lists):
    for player in players:
        player.build_qrcode()


def build_qrcode(players=player_lists):
    for player in players:
        player.build_qrcode()


def prison(players=player_lists):
    for player in players:
        player.prison()

button_name = [{'保护':protect,'高塔':tower,'造墙':build_wall,'速搭':fast_leaves},
               {'落地水':fall_water,'侧搭':side_build,'清理':clear_wall,'二维码':build_qrcode},
               {'监狱':prison,'测试':test},
               ]

buttons = []
for i, row in enumerate(button_name):
    j = 0
    for k, v in row.items():
        button = Button(screen, text=k, command=v)
        button.place(x=10+100*j, y=10+100*i, width=80, height=80)
        buttons.append(button)
        j += 1
screen.mainloop()