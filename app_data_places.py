"""

CUE Data Manager source code

Copyright (C) 2022 Iporã Brito Possantti

References:


************ GNU GENERAL PUBLIC LICENSE ************

https://www.gnu.org/licenses/gpl-3.0.en.html

Permissions:
 - Commercial use
 - Distribution
 - Modification
 - Patent use
 - Private use

Conditions:
 - Disclose source
 - License and copyright notice
 - Same license
 - State changes

Limitations:
 - Liability
 - Warranty

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import os
import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import END, RIGHT, LEFT, BooleanVar, DISABLED, NORMAL, ANCHOR
import platform
import pandas as pd
import numpy as np
import backend, inp, tools

def quit():
    """
    smart exit function
    :return:
    """
    b_ans = messagebox.askyesno(title="Exit", message="Confirm exit?")
    if b_ans:
        root.destroy()

def new_session():
    """
    start new session
    :return:
    """
    b_ans = messagebox.askokcancel(title="New Session", message="Confirm new?")
    if b_ans:
        print('OK')
        """clear_metadata()
        # fix colors
        for k in dct_lbls_wplc:
            dct_lbls_wplc[k].config(foreground=color_fg)
        for k in dct_lbls_inp:
            dct_lbls_inp[k].config(foreground=color_fg)
        for k in dct_lbls_params:
            dct_lbls_params[k].config(foreground=color_fg)
        # disable save
        menu_file.entryconfig(2, state=DISABLED)
        reset_status()
        get_entry_metadata()
        authorize()"""

# todo replace this
def command_demo():
    print("Hey")


def add_block():
    s_aux = "Wubba Lubba Dubdub! {}".format(np.random.randint(10, 20))
    listbox_blocks.insert(END, s_aux)


def remove_block():
    n_current = listbox_blocks.curselection()
    print(n_current)
    s_item = listbox_blocks.get(n_current)
    print(s_item)
    if 'Size' in s_item or '-' in s_item:
        pass
    else:
        listbox_blocks.delete(ANCHOR)

# >>> change current dir to here
s_current_dir = os.path.dirname(os.path.abspath(__file__))  # get file directory
os.chdir(path=s_current_dir)  # change dir

# >>> define window
root = tkinter.Tk()

# >>> TOOL SETUP

# block settings
lst_lbls_block = [
    "Block Size",
    "Place Trait ",
    "Place D",
    "Place Name",
    "Place Alias",
    "Place Color"
]
lst_lbls_block_aux = [
    "format: positive integer number",
    "format: positive real number ",
    "format: positive real number",
    "format: text",
    "format: text",
    "format: text"
]

# geometry setup
if platform.system().lower() == "linux":
    root.iconphoto(False, tkinter.PhotoImage(file="./gui/terminal.png"))
    n_height = 630
    n_width = 800
    n_entry_label_width = 11
    n_entry_width = 55
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 2
    n_widg_pady = 2
    n_width_board_button = 70
    n_width_options_labels = 20
    n_width_options_check = 2
elif platform.system().lower() == "windows":
    root.iconphoto(False, tkinter.PhotoImage(file="./gui/terminal.png"))
    n_height = 580
    n_width = 610
    n_entry_label_width = 10
    n_entry_width = 30
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 4
    n_widg_pady = 2
    n_width_board_button = 80
    n_width_options_labels = 20
    n_width_options_check = 2
elif platform.system().lower() == "darwin":
    n_height = 690
    n_width = 800
    n_entry_label_width = 15
    n_entry_width = 52
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 1
    n_widg_pady = 1
    n_width_board_button = 70
    n_width_options_labels = 20
    n_width_options_check = 2
else:
    n_height = 690
    n_width = 800
    n_entry_label_width = 15
    n_entry_width = 52
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 1
    n_widg_pady = 1
    n_width_board_button = 70
    n_width_options_labels = 20
    n_width_options_check = 2



root.geometry("{}x{}".format(int(n_width), int(n_height)))
root.resizable(0, 0)

# color setup
color_bg = "#343434"
color_bg_alt = "#484848"
color_actbg = "#df4a16"
color_fg = "white"

root.config(bg=color_bg)


# icons setup
img_logo = tkinter.PhotoImage(file="gui/logo.png")
img_open = tkinter.PhotoImage(file="gui/open.png")
img_about = tkinter.PhotoImage(file="gui/info.png")
img_play = tkinter.PhotoImage(file="gui/play.png")
img_save = tkinter.PhotoImage(file="gui/save.png")
img_exit = tkinter.PhotoImage(file="gui/exit.png")
img_file = tkinter.PhotoImage(file="gui/file.png")
img_update = tkinter.PhotoImage(file="gui/update.png")
img_brush = tkinter.PhotoImage(file="gui/brush.png")
img_chat = tkinter.PhotoImage(file="gui/chat.png")
img_terminal = tkinter.PhotoImage(file="gui/terminal.png")

# files setup
s_title = "Places Dataset Tool"
root.title(s_title)

# >> set menus

# Add the menu
menubar = tkinter.Menu(
    root, bg=color_bg, activeforeground=color_actbg, foreground=color_fg, bd=0
)
root.config(menu=menubar)

# >> create the File Menu
menu_file = tkinter.Menu(
    menubar, tearoff=0, bg=color_bg_alt, activebackground=color_actbg
)
# add menu items to the File menu
menu_file.add_command(
    label="New ",
    image=img_file,
    compound=LEFT,
    foreground=color_fg,
    activeforeground=color_fg,
    command=new_session,
)
# add separator
menu_file.add_separator()
# add Exit menu item
menu_file.add_command(
    label="Exit",
    image=img_exit,
    compound=LEFT,
    foreground=color_fg,
    activeforeground=color_fg,
    command=quit,
)
# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=menu_file,
    activeforeground=color_fg,
    activebackground=color_actbg,
)
# >> create the Help Menu
menu_help = tkinter.Menu(
    menubar, tearoff=0, bg=color_bg_alt, activebackground=color_actbg
)
# add menu items to the Settings menu
menu_help.add_command(
    label="About",
    image=img_about,
    compound=LEFT,
    foreground=color_fg,
    activeforeground=color_fg,
    command=command_demo,
)
menu_help.add_command(
    label="Language",
    image=img_chat,
    compound=LEFT,
    foreground=color_fg,
    activeforeground=color_fg,
    command=command_demo,
)
# add the File menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=menu_help,
    activeforeground=color_fg,
    activebackground=color_actbg,
)

## >>> Frames layout

frame_header = tkinter.Frame(root, width=n_width, bg=color_bg)
frame_info = tkinter.Frame(frame_header, bg=color_bg)
frame_logo = tkinter.Frame(frame_header, bg=color_bg)
frame_blocksets = tkinter.LabelFrame(
    root, text="Block Settings", width=n_width, bg=color_bg, foreground=color_fg
)
frame_board_block = tkinter.LabelFrame(
    root, text="Block Editor", width=n_width, bg=color_bg, foreground=color_fg
)
frame_list = tkinter.LabelFrame(
    root, text="Blocks Preview", width=n_width, bg=color_bg, foreground=color_fg
)
frame_board_export = tkinter.LabelFrame(
    root, text="Export File", width=n_width, bg=color_bg, foreground=color_fg
)
# pack frames
frame_header.pack(fill="x", padx=n_frame_padx)
frame_logo.pack(fill="x", padx=n_frame_padx, side=RIGHT)
frame_info.pack(fill="y", padx=n_frame_padx, side=RIGHT)
frame_blocksets.pack(fill="x", padx=n_frame_padx, pady=n_frame_pady)
frame_board_block.pack(fill="x", padx=n_frame_padx, pady=n_frame_pady)
frame_list.pack(padx=n_frame_padx, pady=n_frame_pady)



# >> Header layout
label_logo = tkinter.Label(
    frame_logo,
    image=img_logo,
    width=70,
    bg=color_bg,
    activebackground=color_actbg,
    foreground=color_fg,
    activeforeground=color_fg,
)
label_logo.pack(side=RIGHT)
s_head_msg = "CUE1d Data Management Tool - Places"
label_infos = tkinter.Label(
    frame_info,
    text=s_head_msg,
    width=n_width,
    anchor="w",
    bg=color_bg,
    activebackground=color_actbg,
    foreground=color_fg,
    activeforeground=color_fg,
)
label_infos.pack()


# >> Block Settings Frame layout

dct_lbls_blocks = dict()
dct_etr_blocks = dict()
dct_btn_upd_blocks = dict()
dct_lbls_blocks_aux = dict()
for i in range(len(lst_lbls_block)):
    s_lcl_key = lst_lbls_block[i]
    # label
    dct_lbls_blocks[s_lcl_key] = tkinter.Label(
        frame_blocksets,
        text=s_lcl_key,
        width=n_entry_label_width,
        anchor="e",
        bg=color_bg,
        activebackground=color_actbg,
        foreground=color_fg,
        activeforeground=color_fg,
    )
    dct_lbls_blocks[s_lcl_key].grid(row=i, column=0, pady=n_widg_pady, padx=n_widg_padx)
    # entry
    dct_etr_blocks[s_lcl_key] = tkinter.Entry(
        frame_blocksets,
        width=n_entry_width,
        bg=color_bg_alt,
        foreground=color_fg,
        selectbackground=color_actbg,
        selectforeground=color_fg,
        highlightbackground=color_bg_alt,
        bd=1,
    )
    dct_etr_blocks[s_lcl_key].grid(row=i, column=1, pady=n_widg_pady, padx=n_widg_padx)
    # update button
    dct_btn_upd_blocks[s_lcl_key] = tkinter.Button(
        frame_blocksets,
        image=img_update,
        bg=color_bg,
        activebackground=color_actbg,
        foreground=color_fg,
        activeforeground=color_fg,
        highlightbackground=color_bg,
        bd=0,
    )
    dct_btn_upd_blocks[s_lcl_key].grid(row=i, column=2, pady=n_widg_pady, padx=n_widg_padx)
    # label
    dct_lbls_blocks_aux[s_lcl_key] = tkinter.Label(
        frame_blocksets,
        text=lst_lbls_block_aux[i],
        width=int(2.5 * n_entry_label_width),
        anchor="w",
        bg=color_bg,
        activebackground=color_actbg,
        foreground=color_fg,
        activeforeground=color_fg,
    )
    dct_lbls_blocks_aux[s_lcl_key].grid(row=i, column=3, pady=n_widg_pady, padx=n_widg_padx)

# >> Main Board
# update button
button_update_entries = tkinter.Button(
    frame_board_block,
    text="Update",
    image=img_update,
    compound=LEFT,
    width=n_width_board_button,
    height=30,
)
button_update_entries.config(
    bg=color_bg_alt,
    activebackground=color_actbg,
    disabledforeground="grey",
    foreground=color_fg,
    activeforeground=color_fg,
    highlightbackground=color_bg,
    bd=0,
)
button_update_entries.config(command=command_demo)
button_update_entries.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# add button
button_add_block = tkinter.Button(
    frame_board_block,
    text="Add",
    image=img_terminal,
    compound=LEFT,
    width=n_width_board_button,
    height=30,
)
button_add_block.config(
    bg=color_bg_alt,
    activebackground=color_actbg,
    disabledforeground="grey",
    foreground=color_fg,
    activeforeground=color_fg,
    highlightbackground=color_bg,
    bd=0,
)
button_add_block.config(command=add_block)
#button_add_block.config(state=DISABLED)
button_add_block.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# new block
button_new_block = tkinter.Button(
    frame_board_block,
    text="New",
    image=img_file,
    compound=LEFT,
    width=n_width_board_button,
    height=30,
)
button_new_block.config(
    bg=color_bg_alt,
    activebackground=color_actbg,
    disabledforeground="grey",
    foreground=color_fg,
    activeforeground=color_fg,
    highlightbackground=color_bg,
    bd=0,
)
button_new_block.config(command=command_demo)
button_new_block.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# remove block
button_remove_block = tkinter.Button(
    frame_board_block,
    text="Remove",
    image=img_terminal,
    compound=LEFT,
    width=n_width_board_button,
    height=30,
)
button_remove_block.config(
    bg=color_bg_alt,
    activebackground=color_actbg,
    disabledforeground="grey",
    foreground=color_fg,
    activeforeground=color_fg,
    highlightbackground=color_bg,
    bd=0,
)
button_remove_block.config(command=remove_block)
button_remove_block.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# >> List frame widgets Layout
scrollbar_log_y = tkinter.Scrollbar(
    frame_list, bg=color_bg_alt, bd=0, activebackground=color_actbg
)
scrollbar_log_x = tkinter.Scrollbar(
    frame_list,
    orient="horizontal",
    bg=color_bg_alt,
    bd=0,
    activebackground=color_actbg,
)
s_blocks_header = ' {:8} {:8} {:8}'.format('Size', 'Trait', 'D')

listbox_blocks = tkinter.Listbox(
    frame_list,
    height=12,
    width=94,
    borderwidth=0,
    bd=0,
    bg="grey",
    foreground=color_fg,
    highlightbackground=color_bg,
    selectbackground=color_actbg,
    selectforeground=color_fg,
    yscrollcommand=scrollbar_log_y.set,
    xscrollcommand=scrollbar_log_x.set,
)
scrollbar_log_y.config(command=listbox_blocks.yview)
scrollbar_log_x.config(command=listbox_blocks.xview)
listbox_blocks.grid(row=1, column=0)
scrollbar_log_y.grid(row=1, column=1, sticky="NS")
scrollbar_log_x.grid(row=2, column=0, sticky="WE")
#listbox_log.config(state=DISABLED)

# >>> Commands
dct_btn_upd_blocks[lst_lbls_block[0]].config(
    command=lambda : command_demo()
)
dct_btn_upd_blocks[lst_lbls_block[1]].config(
    command=lambda : command_demo()
)
dct_btn_upd_blocks[lst_lbls_block[2]].config(
    command=lambda : command_demo()
)
dct_btn_upd_blocks[lst_lbls_block[3]].config(
    command=lambda : command_demo()
)
dct_btn_upd_blocks[lst_lbls_block[4]].config(
    command=lambda : command_demo()
)
dct_btn_upd_blocks[lst_lbls_block[5]].config(
    command=lambda : command_demo()
)

s_blocks_header = ' {:8} {:8} {:8}'.format('Size', 'Trait', 'D')
listbox_blocks.insert(END, s_blocks_header)
listbox_blocks.insert(END, '-' * 100)
# run root window
root.mainloop()
