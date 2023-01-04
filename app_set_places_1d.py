"""

CUE Data Manager for Places source code

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


def save_as():
    """
    save as routine
    :return: string filepath
    """
    s_ans = fd.asksaveasfilename(
        title="Save As",
        filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
    )
    if str(s_ans) == "()" or s_ans == "":
        return 'abort'
    else:
        # handle naming extension problem
        if s_ans[-4:] == '.txt':
            pass
        else:
            s_ans = s_ans + '.txt'
        return s_ans


def save_file():
    """
    save file routine
    :return: none
    """
    global b_ok_to_save
    authorize_save()
    if b_ok_to_save:
        s_filepath = save_as()
        if s_filepath == 'abort':
            pass
        else:
            # get list
            lst_listbox_blocks = listbox_blocks.get(0, END)
            lst_id = list()
            lst_x = list()
            lst_trait = list()
            lst_d = list()
            lst_name = list()
            lst_alias = list()
            lst_color = list()
            lst_sizes = list()
            # get sizes
            n_counter = 0
            for i in range(1, len(lst_listbox_blocks)):
                lst_local = lst_listbox_blocks[i].split(';')
                lst_local_values = list()
                # handle local values
                for j in range(len(lst_local)):
                    lst_local_values.append(lst_local[j].strip())
                # append to lists
                for j in range(int(lst_local_values[0])):
                    lst_id.append(n_counter + 1)
                    lst_x.append(n_counter)
                    lst_trait.append((lst_local_values[1]))
                    lst_d.append(lst_local_values[2])
                    lst_name.append(lst_local_values[3])
                    lst_alias.append(lst_local_values[4])
                    lst_color.append(lst_local_values[5])
                    # update counter
                    n_counter = n_counter + 1
            df_out = pd.DataFrame(
                {
                    'Id': lst_id,
                    'x': lst_x,
                    'Trait': lst_trait,
                    'C': lst_d,
                    'Name': lst_name,
                    'Alias': lst_alias,
                    'Color': lst_color,
                }
            )
            if bool(b_randomize.get()):
                # sample the dataframe with frac = 1 (100%)
                df_out = df_out.sample(frac=1).reset_index(drop=True)
                # reset fields
                df_out['Id'] = np.arange(0, len(df_out)) + 1
                df_out['x'] = np.arange(0, len(df_out))
            # exporto to file
            df_out.to_csv(s_filepath, sep=';', index=False)
            # todo export view
            tkinter.messagebox.showinfo(message="File Saved")
    else:
        messagebox.showwarning(
            title="Warning",
            message="Zero Blocks Found"
        )


def new_session():
    """
    start new session
    :return: none
    """
    b_ans = messagebox.askokcancel(title="New Session", message="Confirm new?")
    if b_ans:
        clear_entries()
        authorize_add()
        listbox_blocks.delete(0, END)
        append_header()
        authorize_save()
        # options
        b_randomize.set(False)



# todo replace this
def command_demo():
    print("Hey")


def format_string(lst_block, s_sep=' '):
    """
    convenient routine for string formatting
    :param lst_block: list of fields
    :param s_sep: string separator
    :return: string formatted
    """
    s_aux = ' {:>6s}{}{:>6s}{}{:>6s}{}{:>12s}{}{:>8s}{}{:>8s}'.format(
        lst_block[0].strip(),
        s_sep,
        lst_block[1].strip(),
        s_sep,
        lst_block[2].strip(),
        s_sep,
        lst_block[3].strip(),
        s_sep,
        lst_block[4].strip(),
        s_sep,
        lst_block[5].strip(),
    )
    return s_aux


def add_block():
    """
    add block to listbox
    :return: none
    """
    global b_ok_to_add
    update_all_entries(b_popup=False)
    if b_ok_to_add:
        lst_entries = get_entries_list()
        s_entries = format_string(lst_block=lst_entries, s_sep=';')
        listbox_blocks.insert(END, s_entries)
        authorize_save()
    else:
        messagebox.showwarning(
            title="Warning",
            message="Invalid Entry Found"
        )


def remove_block():
    """
    remove block from listbox
    :return: none
    """
    n_current = listbox_blocks.curselection()
    if len(n_current) > 0:
        s_item = listbox_blocks.get(n_current)
        if 'Size' in s_item or '-' in s_item:
            messagebox.showwarning(
                title="Warning",
                message="Select a Block Item"
            )
        else:
            b_ans = messagebox.askokcancel(
                title="Remove Block",
                message="Confirm remove?"
            )
            if b_ans:
                listbox_blocks.delete(ANCHOR)
    else:
        messagebox.showwarning(
            title="Warning",
            message="Select a Block Item"
        )


def new_block():
    """
    refresh block forms
    :return: none
    """
    b_ans = messagebox.askokcancel(
        title="New Block",
        message="Confirm new block?"
    )
    if b_ans:
        clear_entries()
    authorize_add()


def get_entries_list():
    """
    load entries to list
    :return:
    """
    lst_etr_values = list()
    for k in dct_lbls_blocks:
        lst_etr_values.append(dct_etr_blocks[k].get())
    return lst_etr_values


def clear_entries():
    """
    clean up entries
    :return:
    """
    # labels
    for k in dct_lbls_blocks:
        dct_etr_blocks[k].delete(0, END)
        dct_lbls_blocks[k].config(foreground=color_fg)
        dct_status[k] = False


def validate_int(entry_value):
    """
    Validate integer entry
    :param entry_value: int entry value
    :return:
    """
    b_valid = True
    try:
        entry_value_int = int(entry_value)
        entry_value_float = float(entry_value)
        if entry_value_float % 1 == 0:
            b_valid = True
        else:
            b_valid = False
    except ValueError:
        b_valid = False
    return b_valid


def validate_float(entry_value):
    """
    validate float entry
    :param entry_value:
    :return:
    """
    b_valid = True
    try:
        entry_value_int = float(entry_value)
    except ValueError:
        b_valid = False
    return b_valid


def update_all_entries(b_popup=True):
    """
    Batch update routine
    :param b_popup: boolean for popup messages
    :return: none
    """
    global b_ok_to_add
    for i in range(len(lst_lbls_block)):
        update_entry(
            s_entry=lst_lbls_block[i],
            s_entry_type=lst_types_block[i],
            b_popup=False,
            )
    if b_popup:
        tkinter.messagebox.showinfo(message="All entries were updated")
        if b_ok_to_add:
            pass
        else:
            messagebox.showwarning(
                title="Warning",
                message="Invalid Entry Found"
            )


def update_entry(s_entry, s_entry_type, b_popup=True):
    """
    update string entry
    :param s_entry: string entry label
    :param s_entry_type: string entry type (Int, Real, Text, ...)
    :param b_popup: boolean for popup msg
    :return: none
    """
    s_entry_value = dct_etr_blocks[s_entry].get()
    if len(s_entry_value) == 0:
        # change color
        dct_lbls_blocks[s_entry].config(foreground="red")
        # change status
        dct_status[s_entry] = False
        # message
        if b_popup:
            messagebox.showerror(
                title="Error", message="{}: empty entry".format(s_entry)
            )
    else:
        # get valid boolean
        b_valid = True
        if s_entry_type == "Int":
            b_valid = validate_int(entry_value=s_entry_value)
        elif s_entry_type == "Real":
            b_valid = validate_float(entry_value=s_entry_value)
        else:
            b_valid = True
        # action
        if b_valid:
            # reset color
            dct_lbls_blocks[s_entry].config(foreground=color_fg)
            # change status
            dct_status[s_entry] = True
            # message
            if b_popup:
                tkinter.messagebox.showinfo(message="{}: updated".format(s_entry))
        else:
            # change color
            dct_lbls_blocks[s_entry].config(foreground="red")
            # change status
            dct_status[s_entry] = False
            # message
            if b_popup:
                tkinter.messagebox.showerror(
                    title="Error", message="{}: invalid format".format(s_entry)
                )
    authorize_add()


def authorize_add():
    """
    evaluate if is ok to run -- all metadata must be OK
    :return:
    """
    global b_ok_to_add
    b_ok_to_add = True
    for k in dct_status:
        b_ok_to_add = b_ok_to_add * dct_status[k]
    if b_ok_to_add:
        button_add_block.config(state=NORMAL)
    else:
        button_add_block.config(state=DISABLED)


def authorize_save():
    """
    evaluate if it is ok to save file
    :return:
    """
    global b_ok_to_save
    lst_listbox_blocks = listbox_blocks.get(0, END)
    if len(lst_listbox_blocks) > 1:
        b_ok_to_save = True
        button_export.config(state=NORMAL)
    else:
        b_ok_to_save = False
        button_export.config(state=DISABLED)


def reset_status():
    """
    reset run status
    :return:
    """
    global dct_status
    # status setup
    dct_status = dict()
    for k in lst_lbls_block:
        dct_status[k] = False


def append_header():
    """
    append header to listbox
    :return:
    """
    lst_head = [
        'Size', 'Trait', 'C', 'Name', 'Alias', 'Color'
    ]
    s_blocks_header = format_string(lst_block=lst_head, s_sep=';')
    listbox_blocks.insert(END, s_blocks_header)
    #listbox_blocks.insert(END, '-' * len(s_blocks_header))


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
    "Place C",
    "Place Name",
    "Place Alias",
    "Place Color"
]
lst_types_block = [
    'Int',
    'Real',
    'Real',
    'Text',
    'Text',
    'Text',
]
lst_lbls_block_aux = [
    "format: positive integer number",
    "format: positive real number ",
    "format: positive real number",
    "format: text",
    "format: text",
    "format: text"
]

# ----- geometry setup

# get platform name
s_platform = platform.system().lower()
# load setup dataframe
df_setup = pd.read_csv('./gui/setup.txt', sep=';', skipinitialspace=True)
# try to set
try:
    n_height = df_setup.loc[df_setup["Name"] == 'height', s_platform].values[0]
    n_width = df_setup.loc[df_setup["Name"] == 'width', s_platform].values[0]
    n_entry_label_width = df_setup.loc[df_setup["Name"] == 'entry label width', s_platform].values[0]
    n_entry_width_file = df_setup.loc[df_setup["Name"] == 'entry width file', s_platform].values[0]
    n_entry_width = df_setup.loc[df_setup["Name"] == 'entry width', s_platform].values[0]
    n_frame_padx = df_setup.loc[df_setup["Name"] == 'frame padx', s_platform].values[0]
    n_frame_pady = df_setup.loc[df_setup["Name"] == 'frame pady', s_platform].values[0]
    n_widg_padx = df_setup.loc[df_setup["Name"] == 'widget padx', s_platform].values[0]
    n_widg_pady = df_setup.loc[df_setup["Name"] == 'widget pady', s_platform].values[0]
    n_width_board_button = df_setup.loc[df_setup["Name"] == 'button board width', s_platform].values[0]
    n_width_options_labels = df_setup.loc[df_setup["Name"] == 'option label width', s_platform].values[0]
    n_width_options_check = df_setup.loc[df_setup["Name"] == 'option check width', s_platform].values[0]
    n_listbox_height = df_setup.loc[df_setup["Name"] == 'listbox height', s_platform].values[0]
    n_listbox_width = df_setup.loc[df_setup["Name"] == 'listbox width', s_platform].values[0]
except KeyError:
    # standard setup
    n_height = 610
    n_width = 610
    n_entry_label_width = 15
    n_entry_width_file = 52
    n_entry_width = 20
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 4
    n_widg_pady = 2
    n_width_board_button = 100
    n_width_options_labels = 20
    n_width_options_check = 2
    n_listbox_height = 7
    n_listbox_width = 72
except IndexError:
    # standard setup
    n_height = 610
    n_width = 610
    n_entry_label_width = 15
    n_entry_width_file = 52
    n_entry_width = 20
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 4
    n_widg_pady = 2
    n_width_board_button = 70
    n_width_options_labels = 20
    n_width_options_check = 2
    n_listbox_height = 7
    n_listbox_width = 72
# set
root.geometry("{}x{}".format(int(n_width), int(n_height)))
root.resizable(0, 0)

# color setup
color_bg = "#343434"
color_bg_alt = "#484848"
color_actbg = "#df4a16"
color_fg = "white"

root.config(bg=color_bg)


# icons setup
# todo board buttons icon
img_add = tkinter.PhotoImage(file="gui/add.png")
img_remove = tkinter.PhotoImage(file="gui/remove.png")
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

# set icon
root.iconphoto(False, tkinter.PhotoImage(file="./gui/terminal.png"))


# files setup
s_title = "Places File Tool - CUE1d"
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
frame_board_params = tkinter.LabelFrame(
    root, text="Options", width=n_width, bg=color_bg, foreground=color_fg
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
frame_list.pack(fill="x", padx=n_frame_padx, pady=n_frame_pady)
frame_board_params.pack(fill="x", padx=n_frame_padx, pady=n_frame_pady)
frame_board_export.pack(fill="x", padx=n_frame_padx, pady=n_frame_pady)



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
s_head_msg = "CUE1d Data Management Tool - Places 1D"
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

# >>> Commands
dct_btn_upd_blocks[lst_lbls_block[0]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[0],
                                  s_entry_type=lst_types_block[0])
)
dct_btn_upd_blocks[lst_lbls_block[1]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[1],
                                  s_entry_type=lst_types_block[1])
)
dct_btn_upd_blocks[lst_lbls_block[2]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[2],
                                  s_entry_type=lst_types_block[2])
)
dct_btn_upd_blocks[lst_lbls_block[3]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[3],
                                  s_entry_type=lst_types_block[3])
)
dct_btn_upd_blocks[lst_lbls_block[4]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[4],
                                  s_entry_type=lst_types_block[4])
)
dct_btn_upd_blocks[lst_lbls_block[5]].config(
    command=lambda : update_entry(s_entry=lst_lbls_block[5],
                                  s_entry_type=lst_types_block[5])
)


# >> block Board

# update button
button_update_entries = tkinter.Button(
    frame_board_block,
    text="Update Block",
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
button_update_entries.config(command=lambda : update_all_entries(b_popup=True))
button_update_entries.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# add button
button_add_block = tkinter.Button(
    frame_board_block,
    text="Add Block",
    image=img_add,
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
button_add_block.config(state=DISABLED)
button_add_block.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# new block
button_new_block = tkinter.Button(
    frame_board_block,
    text="New Block",
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
button_new_block.config(command=new_block)
button_new_block.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)

# remove block
button_remove_block = tkinter.Button(
    frame_board_block,
    text="Remove Block",
    image=img_remove,
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
listbox_blocks = tkinter.Listbox(
    frame_list,
    height=n_listbox_height,
    width=n_listbox_width,
    borderwidth=0,
    bd=0,
    bg="grey",
    font="TkFixedFont",
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


# >> Parameters Board

b_randomize = BooleanVar()
label_randomize = tkinter.Label(
    frame_board_params,
    text='Randomize Blocks',
    width=n_width_options_labels,
    anchor="e",
    bg=color_bg,
    activebackground=color_actbg,
    foreground=color_fg,
    activeforeground=color_fg,
)
check_randomize = tkinter.Checkbutton(
    frame_board_params,
    variable=b_randomize,
    width=n_width_options_check,
    bg=color_bg,
    activebackground=color_actbg,
    highlightbackground=color_bg,
    bd=0,
)
label_randomize.pack(side=LEFT)
check_randomize.pack(side=LEFT)



# >> Export Board

# export button
button_export = tkinter.Button(
    frame_board_export,
    text="Save File",
    image=img_save,
    compound=LEFT,
    width=n_width_board_button,
    height=30,
)
button_export.config(
    bg=color_bg_alt,
    activebackground=color_actbg,
    disabledforeground="grey",
    foreground=color_fg,
    activeforeground=color_fg,
    highlightbackground=color_bg,
    bd=0,
)
button_export.config(command=lambda : save_file())
button_export.pack(side=LEFT, padx=n_widg_padx, pady=n_widg_pady)


# append header
append_header()

# reset status
reset_status()

authorize_save()

# run root window
root.mainloop()
