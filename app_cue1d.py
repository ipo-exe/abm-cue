'''

CUE 1d GUI source code

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

'''
import os
import tkinter
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import END, RIGHT, LEFT, BooleanVar, DISABLED, NORMAL
import webbrowser
import platform
import pandas as pd
import backend, inp, tools


def callsub():

    import subprocess
    subprocess.run(["inkscape"])


def command_demo():
    print('Hey')


def quit():
    """
    smart exit function
    :return:
    """
    b_ans = messagebox.askyesno(title='Exit', message='Confirm exit?')
    if b_ans:
        root.destroy()


def save():
    """
    save file
    :return:
    """
    global s_metadata_filepath, df_meta
    get_entry_metadata()
    # export to file
    df_meta.to_csv(s_metadata_filepath, sep=';', index=False)
    print_report_msg(s_msg='Save : Saved to {}'.format(s_metadata_filepath))


def save_as():
    """
    save as file routine
    :return:
    """
    global s_metadata_filepath
    s_ans = fd.asksaveasfilename(title='Save As',
                                 initialdir=dct_etr_wplc['Input Folder'].get(),
                                 filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    if str(s_ans) == '()' or s_ans == '':
        pass
    else:
        s_metadata_filepath = s_ans
        save()
        # enable save
        menu_file.entryconfig(2, state=NORMAL)


def print_report_msg(s_msg):
    """
    report string message to log listbox
    :param s_msg:
    :return:
    """
    # report
    listbox_log.config(state=NORMAL)
    s_report = ' {} >>> {}'.format(backend.timestamp_log(), s_msg)
    listbox_log.insert(END, s_report)
    listbox_log.config(state=DISABLED)


def reload_entries():
    """
    Reload entries from tool metadata dataframe
    :return:
    """
    # workplace
    for k in dct_etr_wplc:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        if pd.isna(s_reload):
            s_reload = ''
        # clear first
        dct_etr_wplc[k].delete(0, END)
        # insert
        dct_etr_wplc[k].insert(0, s_reload)
    # input files
    for k in dct_etr_inp:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        if pd.isna(s_reload):
            s_reload = ''
        # clear first
        dct_etr_inp[k].delete(0, END)
        # insert
        dct_etr_inp[k].insert(0, s_reload)
    # parameters
    for k in dct_etr_params:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        if pd.isna(s_reload):
            s_reload = ''
        # clear first
        dct_etr_params[k].delete(0, END)
        # insert
        dct_etr_params[k].insert(0, s_reload)
    # options
    for k in dct_var_opts:
        df_lcl = df_meta.query('Metadata == "{}"'.format(k))
        # retrieve value from metadata
        s_reload = df_lcl['Value'].values[0]
        # set
        if s_reload == 'True':
            dct_var_opts[k].set(True)
        else:
            dct_var_opts[k].set(False)


def new_session():
    """
    start new session
    :return:
    """
    b_ans = messagebox.askokcancel(title='New Session', message='Confirm new?')
    if b_ans:
        clear_metadata()
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
        authorize()


def clear_metadata():
    """
    flush out tool metadata
    :return:
    """
    # clear entries
    for k in dct_etr_wplc:
        dct_etr_wplc[k].delete(0, END)
    for k in dct_etr_inp:
        dct_etr_inp[k].delete(0, END)
    for k in dct_etr_params:
        dct_etr_params[k].delete(0, END)
    for k in dct_var_opts:
        dct_var_opts[k].set(False)
    # update dataframe
    get_entry_metadata()
    # clear log
    listbox_log.config(state=NORMAL)
    listbox_log.delete(0, END)
    listbox_log.config(state=DISABLED)
    print_report_header()


def run():
    """
    run button routine
    :return:
    """
    global df_meta, b_ok_to_run
    # report
    print_report_msg(s_msg='Run : Processing...')
    # update things
    update_all_entries(b_popup=False, b_report_error=True, b_report_update=False, b_silent=True)
    if b_ok_to_run:
        # freeze button
        button_run.config(state=DISABLED)
        #
        # Create run dir
        backend.status('creating output directory', process=True)
        s_lcl_wkplc = df_meta[df_meta['Metadata'] == 'Run Folder']['Value'].values[0]
        s_folder = backend.create_rundir(label='CUE1d', wkplc=s_lcl_wkplc)
        # save metadata to run dir
        backend.status('saving simulation parameters', process=True)
        fsim = '{}/param_simulation.txt'.format(s_folder)
        df_meta.to_csv(fsim, sep=';', index=False)

        # run things
        backend.status('running model', process=True)
        try:
            # RUN
            dct_out = tools.run_cue1d(fsim=fsim, wkplc=False, s_dir_out=s_folder)

            # report
            print_report_msg(s_msg='Run : Task done')
            print_report_msg(s_msg='Run : Results at {}'.format(s_folder))
            messagebox.showinfo(title='Run Status', message='Success. See log report for output folder.')
        except MemoryError:
            # report
            print_report_msg(s_msg='Run : Memory Error')
            messagebox.showerror(title='Run Status', message='Memory Error')
        except TypeError:
            # report
            print_report_msg(s_msg='Run : Type Error in input files. Check out data.')
            messagebox.showerror(title='Run Status', message='Type Error in input files. Check out data.')
        except KeyError:
            # report
            print_report_msg(s_msg='Run : Key Error in input files. Check out field names.')
            messagebox.showerror(title='Run Status', message='Key Error in input files. Check out field names.')
        # enable button
        button_run.config(state=NORMAL)
    else:
        messagebox.showwarning(title='Run Status', message='Problems found. See log report for error messages')


def get_entry_metadata():
    """
    get from entries all metadata
    :return:
    """
    global df_meta, lst_lbls_wplc, dct_etr_wplc, lst_lbls_inp, dct_etr_inp, lst_lbls_opts, dct_var_opts
    lst_metadata = list()
    lst_values = list()
    lst_status = list()
    # append timestamp
    lst_metadata.append('Timestamp')
    lst_values.append(backend.timestamp_log())
    lst_status.append(True)
    # update folders
    for i in range(len(lst_lbls_wplc)):
        s_lcl_key = lst_lbls_wplc[i]
        lst_metadata.append(s_lcl_key)
        lst_values.append(dct_etr_wplc[s_lcl_key].get())
    # update files
    for i in range(len(lst_lbls_inp)):
        s_lcl_key = lst_lbls_inp[i]
        lst_metadata.append(s_lcl_key)
        lst_values.append(dct_etr_inp[s_lcl_key].get())
    # update paramters
    for i in range(len(lst_lbls_params)):
        s_lcl_key = lst_lbls_params[i]
        lst_metadata.append(s_lcl_key)
        lst_values.append(dct_etr_params[s_lcl_key].get())
    # update options
    for i in range(len(lst_lbls_opts)):
        s_lcl_key = lst_lbls_opts[i]
        lst_metadata.append(s_lcl_key)
        lst_values.append(dct_var_opts[s_lcl_key].get())
    # re-instantiate dataframe
    df_meta = pd.DataFrame({'Metadata': lst_metadata,
                            'Value':lst_values})
    #print(df_meta.to_string())

def authorize():
    """
    evaluate if is ok to run -- all metadata must be OK
    :return:
    """
    global b_ok_to_run
    b_ok_to_run = True
    for k in dct_status:
        b_ok_to_run = b_ok_to_run * dct_status[k]
    if b_ok_to_run:
        button_run.config(state=NORMAL)
    else:
        button_run.config(state=DISABLED)


def open_about_input(n_entry=0):
    """
    open doc link of input file
    :param n_entry:
    :return:
    """
    webbrowser.open(url=lst_urls_inp[n_entry])


def reset_status():
    """
    reset run status
    :return:
    """
    global dct_status
    # status setup
    dct_status = dict()
    for k in lst_lbls_wplc:
        dct_status[k] = False
    for k in lst_lbls_inp:
        dct_status[k] = False


def invalid_entry(s_entry, s_msg='', s_cat='param'):
    if s_msg == '':
        s_msg = '{} : Invalid entry.'.format(s_entry)
    else:
        s_msg = '{} : Invalid entry. {}.'.format(s_entry, s_msg)
    messagebox.showwarning(title='Warning', message=s_msg)
    print_report_msg(s_msg=s_msg)
    if s_cat == 'param':
        dct_etr_params[s_entry].focus()
        dct_lbls_params[s_entry].config(foreground='red')
    elif s_cat == 'inputfile':
        dct_etr_inp[s_entry].focus()
    elif s_cat == 'workplace':
        dct_etr_wplc[s_entry].focus()


def validate_int(entry_value):
    b_valid = True
    try:
        entry_value_int = int(entry_value)
        entry_value_float = float(entry_value)
        if entry_value_float%1 == 0:
            b_valid = True
        else:
            b_valid = False
    except ValueError:
        b_valid = False
    return b_valid


def validate_float(entry_value):
    b_valid = True
    try:
        entry_value_int = float(entry_value)
    except ValueError:
        b_valid = False
    return b_valid


def update_all_entries(b_popup=True, b_report_error=True, b_report_update=True, b_silent=False):
    """
    Update all entries
    :return:
    """
    if b_silent:
        # report
        print_report_msg(s_msg='Update')
    # workplace
    for i in range(len(lst_lbls_wplc)):
        update_folder(s_entry=lst_lbls_wplc[i],
                      b_popup=b_popup,
                      b_report_error=b_report_error,
                      b_report_update=b_report_update)
    # input files
    for i in range(len(lst_lbls_inp)):
        update_file(s_entry=lst_lbls_inp[i],
                      b_popup=b_popup,
                      b_report_error=b_report_error,
                      b_report_update=b_report_update)
    # parameters
    for i in range(len(lst_lbls_params)):
        update_parameter(s_entry=lst_lbls_params[i],
                         s_entry_type=lst_widget_params[i],
                         b_popup=b_popup,
                         b_report_error=b_report_error,
                         b_report_update=b_report_update)


def update_folder(s_entry, b_popup=True, b_report_error=True, b_report_update=True):
    """
    Update folder entry
    :param n_entry: int index of entry
    :return:
    """
    global df_meta, dct_etr_wplc
    s_lcl_key = s_entry
    s_path = dct_etr_wplc[s_lcl_key].get()
    if len(s_path) == 0:
        # change color
        dct_lbls_wplc[s_lcl_key].config(foreground='red')
        # change status
        dct_status[s_lcl_key] = False
        # message
        if b_popup:
            messagebox.showerror(title='Error', message='{}: empty entry'.format(s_lcl_key))
        if b_report_error:
            # report
            print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    else:
        if os.path.isdir(s_path):
            # change color
            dct_lbls_wplc[s_lcl_key].config(foreground=color_fg)
            # change status
            dct_status[s_lcl_key] = True
            if b_popup:
                tkinter.messagebox.showinfo(message='{}: updated'.format(s_lcl_key))
            if b_report_update:
                # report
                print_report_msg(s_msg='{} : Updated {}'.format(s_lcl_key, s_path))
        else:
            # change color
            dct_lbls_wplc[s_lcl_key].config(foreground='red')
            # change status
            dct_status[s_lcl_key] = False
            if b_popup:
                tkinter.messagebox.showerror(title='Error', message='{}: not found'.format(s_lcl_key))
            if b_report_error:
                # report
                print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    # get entry metadata
    get_entry_metadata()
    # authorize run
    authorize()


def update_file(s_entry, b_popup=True, b_report_error=True, b_report_update=True):
    """
    Update file entry
    :param n_entry: int index of entry
    :return:
    """
    global df_meta, dct_etr_inp
    s_lcl_key = s_entry
    s_path = dct_etr_inp[s_lcl_key].get()
    if len(s_path) == 0:
        # change color
        dct_lbls_inp[s_lcl_key].config(foreground='red')
        # change status
        dct_status[s_lcl_key] = False
        # message
        if b_popup:
            messagebox.showerror(title='Error', message='{}: empty entry'.format(s_lcl_key))
        if b_report_error:
            # report
            print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    else:
        if os.path.isfile(s_path):
            # reset color
            dct_lbls_inp[s_lcl_key].config(foreground=color_fg)
            # change status
            dct_status[s_lcl_key] = True
            # message
            if b_popup:
                tkinter.messagebox.showinfo(message='{}: updated'.format(s_lcl_key))
            if b_report_update:
                # report
                print_report_msg(s_msg='{} : Updated {}'.format(s_lcl_key, s_path))
        else:
            # change color
            dct_lbls_inp[s_lcl_key].config(foreground='red')
            # change status
            dct_status[s_lcl_key] = False
            # message
            if b_popup:
                tkinter.messagebox.showerror(title='Error', message='{}: not found'.format(s_lcl_key))
            if b_report_error:
                # report
                print_report_msg(s_msg='{} : Error -- not found'.format(s_lcl_key))
    # get entry metadata
    get_entry_metadata()
    # authorize run
    authorize()


def update_parameter(s_entry, s_entry_type, b_popup=True, b_report_error=True, b_report_update=True):
    global df_meta, dct_etr_params
    s_lcl_key = s_entry
    s_entry_value = dct_etr_params[s_lcl_key].get()
    if len(s_entry_value) == 0:
        # change color
        dct_lbls_params[s_lcl_key].config(foreground='red')
        # change status
        dct_status[s_lcl_key] = False
        # message
        if b_popup:
            messagebox.showerror(title='Error', message='{}: empty entry'.format(s_lcl_key))
        if b_report_error:
            # report
            print_report_msg(s_msg='{} : Error -- empty entry'.format(s_lcl_key))
    else:
        # get valid boolean
        b_valid = True
        if s_entry_type == 'Int':
            b_valid = validate_int(entry_value=s_entry_value)
        elif s_entry_type == 'Real':
            b_valid = validate_float(entry_value=s_entry_value)
        else:
            b_valid = True
        # action
        if b_valid:
            # reset color
            dct_lbls_params[s_lcl_key].config(foreground=color_fg)
            # change status
            dct_status[s_lcl_key] = True
            # message
            if b_popup:
                tkinter.messagebox.showinfo(message='{}: updated'.format(s_lcl_key))
            if b_report_update:
                # report
                print_report_msg(s_msg='{} : Updated to {}'.format(s_lcl_key, s_entry_value))
        else:
            # change color
            dct_lbls_params[s_lcl_key].config(foreground='red')
            # change status
            dct_status[s_lcl_key] = False
            # message
            if b_popup:
                tkinter.messagebox.showerror(title='Error', message='{}: invalid format'.format(s_lcl_key))
            if b_report_error:
                # report
                print_report_msg(s_msg='{} : Error -- invalid format'.format(s_lcl_key))
    # get entry metadata
    get_entry_metadata()
    # authorize run
    authorize()


def pick_folder(s_entry):
    """
    pick folder helper
    :param n_entry: int index of folder entry
    :return:
    """
    global lst_lbls_wplc
    while True:
        s_folderpath = fd.askdirectory(title='Select a folder')
        if len(s_folderpath) == 0:
            break
        # confirm exit
        b_ans = tkinter.messagebox.askokcancel(title='Confirm folder', message=s_folderpath)
        if b_ans:
            # change entry
            dct_etr_wplc[s_entry].delete(0, END) # clear
            dct_etr_wplc[s_entry].insert(0, s_folderpath) # insert
            update_folder(s_entry=s_entry)
            break


def pick_file(s_entry, tpl_file_type, s_initialdir):
    """
    pick file helper
    :param tpl_file_type: tuple of file type
    :param s_initialdir: string path to initial dir
    :param n_entry:
    :return:
    """
    global lst_lbls_inp
    while True:
        tpl_filetypes = (tpl_file_type, ('All files', '*.*'))
        s_filepath = fd.askopenfilename(title='Select a file',
                                        initialdir=s_initialdir,
                                        filetypes=tpl_filetypes)

        if len(s_filepath) == 0:
            break
        # confirm exit
        b_ans = messagebox.askokcancel(title='Confirm file', message=s_filepath)
        if b_ans:
            # change entry
            dct_etr_inp[s_entry].delete(0, END)  # clear
            dct_etr_inp[s_entry].insert(0, s_filepath)  # insert
            update_file(s_entry=s_entry)
            break


def load_tool_file():
    global dct_etr_wplc, lst_lbls_wplc
    global s_metadata_filepath
    s_initialdir = dct_etr_wplc[lst_lbls_wplc[0]].get()
    tpl_filetypes = (('Text File', '*.txt'), ('All files', '*.*'))
    s_filepath = fd.askopenfilename(title='Select a file',
                                    initialdir=s_initialdir,
                                    filetypes=tpl_filetypes)
    if len(s_filepath) == 0:
            pass
    else:
        s_metadata_filepath = s_filepath
        load_metadata()
        # enable save
        menu_file.entryconfig(2, state=NORMAL)


def load_metadata():
    """
    load metadata from file
    :return:
    """
    global s_metadata_filepath, df_meta
    if os.path.isfile(s_metadata_filepath):
        s_fields = 'Metadata & Value'
        dct_inp = inp.open_df(s_filepath=s_metadata_filepath, s_mandatory_fields=s_fields)
        if dct_inp['OK Flag']:
            # check more things
            df_loaded = dct_inp['df']
            # check length
            if len(df_loaded) != len(df_meta):
                messagebox.showerror(title='Error', message='Invalid Formatting')
            # check static values match
            else:
                sr_aux = (df_loaded['Metadata'] == df_meta['Metadata'])
                b_aux = sr_aux.min()
                if b_aux:
                    df_meta = df_loaded
                    # report
                    print_report_msg(s_msg='Open : {}'.format(s_metadata_filepath))
                    reload_entries()
                    update_all_entries(b_popup=False)
                else:
                    messagebox.showerror(title='Error', message='Invalid Formatting')
        else:
            messagebox.showerror(title='Error', message=dct_inp['Error Report'])
            # report
            print_report_msg(s_msg='Open : Error -- {}'.format(dct_inp['Error Report']))


def print_report_header():
    print_report_msg(s_msg=' {} Basic Tool {} '.format('*' * 30, '*' * 30))
    print_report_msg(s_msg='Initiate session')


# >>> define window
root = tkinter.Tk()

# >>> TOOL SETUP

# workplace
lst_lbls_wplc = ['Input Folder', 'Run Folder']
# input files
lst_lbls_inp = ['Agents File', 'Places File']
lst_urls_inp = ['https://www.google.com', 'https://www.google.com']
lst_types_inp = [('Text File', '*.txt'), ('Text File', '*.txt')]
# parameters
lst_lbls_params = ['Steps']
lst_widget_params = ['Int']
# boolean options
lst_lbls_opts = ['Return Agents', 'Trace Back', 'Plot Results']

# reset status
reset_status()



# geometry setup

# define for different platforms
if platform.system().lower() == 'linux':
    root.iconphoto(False, tkinter.PhotoImage(file='./gui/terminal.png'))
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
elif platform.system().lower() == 'windows':
    root.iconphoto(False, tkinter.PhotoImage(file='./gui/terminal.png'))
    n_height = 580
    n_width = 610
    n_entry_label_width = 10
    n_entry_width = 52
    n_frame_padx = 5
    n_frame_pady = 2
    n_widg_padx = 4
    n_widg_pady = 2
    n_width_board_button = 70
    n_width_options_labels = 20
    n_width_options_check = 2
elif platform.system().lower() == 'darwin':
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


root.geometry('{}x{}'.format(int(n_width), int(n_height)))
root.resizable(0,0)

# color setup
color_bg = '#343434'
color_bg_alt = '#484848'
color_actbg = '#df4a16'
color_fg = 'white'
'''
# day theme:
color_bg = '#959ca3'
color_bg_alt = '#bec9d4'
color_actbg = '#df4a16'
color_fg = 'black'

'''
root.config(bg=color_bg)


# icons setup
img_logo = tkinter.PhotoImage(file='gui/logo.png')
img_open = tkinter.PhotoImage(file='gui/open.png')
img_about = tkinter.PhotoImage(file='gui/info.png')
img_play = tkinter.PhotoImage(file='gui/play.png')
img_save = tkinter.PhotoImage(file='gui/save.png')
img_exit = tkinter.PhotoImage(file='gui/exit.png')
img_file = tkinter.PhotoImage(file='gui/file.png')
img_update = tkinter.PhotoImage(file='gui/update.png')
img_brush = tkinter.PhotoImage(file='gui/brush.png')
img_chat = tkinter.PhotoImage(file='gui/chat.png')
img_terminal = tkinter.PhotoImage(file='gui/terminal.png')

# files setup
s_title = 'CUE1d Tool'
root.title(s_title)

# >> set menus

# Add the manu
menubar = tkinter.Menu(root,
                       bg=color_bg,
                       activeforeground=color_actbg,
                       foreground=color_fg,
                       bd=0)
root.config(menu=menubar)

# >> create the File Menu
menu_file = tkinter.Menu(menubar, tearoff=0, bg=color_bg_alt, activebackground=color_actbg)
# add menu items to the File menu
menu_file.add_command(label='New ',
                      image=img_file,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=new_session)
# open item
menu_file.add_command(label='Open',
                      image=img_open,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=load_tool_file)
# save item
menu_file.add_command(label='Save',
                      image=img_save,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=save)
# disable save
menu_file.entryconfig(2, state=DISABLED)
# save as item
menu_file.add_command(label='Save As',
                      image=img_save,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=save_as)
# add separator
menu_file.add_separator()
# add Exit menu item
menu_file.add_command(label='Exit',
                      image=img_exit,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=quit)
# add the File menu to the menubar
menubar.add_cascade(label="File",
                    menu=menu_file,
                    activeforeground=color_fg,
                    activebackground=color_actbg)

# >> create the Help Menu
menu_help = tkinter.Menu(menubar,
                         tearoff=0,
                         bg=color_bg_alt,
                         activebackground=color_actbg)
# add menu items to the Settings menu
menu_help.add_command(label='About',
                      image=img_about,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=command_demo)
menu_help.add_command(label='Language',
                      image=img_chat,
                      compound=LEFT,
                      foreground=color_fg,
                      activeforeground=color_fg,
                      command=command_demo)
# add the File menu to the menubar
menubar.add_cascade(label="Help",
                    menu=menu_help,
                    activeforeground=color_fg,
                    activebackground=color_actbg)

## >>> Frames layout

frame_header = tkinter.Frame(root,
                             width=n_width,
                             bg=color_bg)
frame_info = tkinter.Frame(frame_header,
                           bg=color_bg)
frame_logo = tkinter.Frame(frame_header,
                           bg=color_bg)
frame_workplace = tkinter.LabelFrame(root,
                                     text='Workplace',
                                     width=n_width,
                                     bg=color_bg,
                                     foreground=color_fg, )
frame_inputfiles = tkinter.LabelFrame(root,
                                      text='Input files',
                                      width=n_width,
                                      bg=color_bg,
                                      foreground=color_fg)
frame_params = tkinter.LabelFrame(root,
                                  text='Parameters',
                                  width=n_width,
                                  bg=color_bg,
                                  foreground=color_fg)
frame_options = tkinter.LabelFrame(root,
                                   text='Options',
                                   width=n_width,
                                   bg=color_bg,
                                   foreground=color_fg)
frame_board = tkinter.Frame(root,
                            width=n_width,
                            bg=color_bg)

frame_reports = tkinter.Frame(root,
                              width=n_width,
                              bg=color_bg)
# pack frames
frame_header.pack(fill='x', padx=n_frame_padx)
frame_logo.pack(fill='x', padx=n_frame_padx, side=RIGHT)
frame_info.pack(fill='y', padx=n_frame_padx, side=RIGHT)
frame_workplace.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_inputfiles.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_params.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_options.pack(fill='x', padx=n_frame_padx, pady=n_frame_pady)
frame_board.pack(padx=n_frame_padx, pady=n_frame_pady)
frame_reports.pack(padx=n_frame_padx, pady=n_frame_pady)


# >> Header layout
label_logo = tkinter.Label(frame_logo,
                           image=img_logo,
                           width=70,
                           bg=color_bg,
                           activebackground=color_actbg,
                           foreground=color_fg,
                           activeforeground=color_fg)
label_logo.pack(side=RIGHT)
s_head_msg = 'CUE1d Application Tool'
label_infos = tkinter.Label(frame_info,
                            text=s_head_msg,
                            width=n_width,
                            anchor='w',
                            bg=color_bg,
                            activebackground=color_actbg,
                            foreground=color_fg,
                            activeforeground=color_fg)
label_infos.pack()

# >> Workplace Frame layout

# place widgets
dct_lbls_wplc = dict()
dct_etr_wplc = dict()
dct_btn_update_wplc = dict()
dct_btn_search_wplc = dict()
for i in range(len(lst_lbls_wplc)):
    s_lcl_key = lst_lbls_wplc[i]
    # labels
    dct_lbls_wplc[s_lcl_key] = tkinter.Label(frame_workplace,
                                             text=s_lcl_key,
                                             width=n_entry_label_width,
                                             anchor="e",
                                             bg=color_bg,
                                             activebackground=color_actbg,
                                             foreground=color_fg,
                                             activeforeground=color_fg)
    dct_lbls_wplc[s_lcl_key].grid(row=i, column=0, pady=n_widg_pady, padx=n_widg_padx)
    # entries
    dct_etr_wplc[s_lcl_key] = tkinter.Entry(frame_workplace,
                                            width=n_entry_width,
                                            bg=color_bg_alt,
                                            foreground=color_fg,
                                            selectbackground=color_actbg,
                                            selectforeground=color_fg,
                                            highlightbackground=color_bg_alt,
                                            bd=1)
    dct_etr_wplc[s_lcl_key].grid(row=i, column=1, pady=n_widg_pady, padx=n_widg_padx)
    # update button
    dct_btn_update_wplc[s_lcl_key] = tkinter.Button(frame_workplace,
                                                    image=img_update,
                                                    bg=color_bg,
                                                    activebackground=color_actbg,
                                                    foreground=color_fg,
                                                    activeforeground=color_fg,
                                                    highlightbackground=color_bg,
                                                    bd=0)
    dct_btn_update_wplc[s_lcl_key].grid(row=i, column=2, pady=n_widg_pady, padx=n_widg_padx)
    # search buttons
    dct_btn_search_wplc[s_lcl_key] = tkinter.Button(frame_workplace,
                                                    text='Search',
                                                    image=img_open,
                                                    compound=LEFT,
                                                    bg=color_bg_alt,
                                                    activebackground=color_actbg,
                                                    foreground=color_fg,
                                                    activeforeground=color_fg,
                                                    highlightbackground=color_bg_alt,
                                                    bd=0)
    dct_btn_search_wplc[s_lcl_key].grid(row=i, column=3, pady=n_widg_pady, padx=n_widg_padx)

# >> Input files

# place widgets in dicts
dct_lbls_inp = dict()
dct_etr_inp = dict()
dct_btn_upd_inp = dict()
dct_btn_search_inp = dict()
dct_btn_about_inp = dict()
for i in range(len(lst_lbls_inp)):
    s_lcl_key = lst_lbls_inp[i]
    # label
    dct_lbls_inp[s_lcl_key] = tkinter.Label(frame_inputfiles,
                                            text=s_lcl_key,
                                            width=n_entry_label_width,
                                            anchor="e",
                                            bg=color_bg,
                                            activebackground=color_actbg,
                                            foreground=color_fg,
                                            activeforeground=color_fg)
    dct_lbls_inp[s_lcl_key].grid(row=i, column=0, pady=n_widg_pady, padx=n_widg_padx)
    # entry
    dct_etr_inp[s_lcl_key] = tkinter.Entry(frame_inputfiles,
                                           width=n_entry_width,
                                           bg=color_bg_alt,
                                           foreground=color_fg,
                                           selectbackground=color_actbg,
                                           selectforeground=color_fg,
                                           highlightbackground=color_bg_alt,
                                           bd=1)
    dct_etr_inp[s_lcl_key].grid(row=i, column=1, pady=n_widg_pady, padx=n_widg_padx)
    # update button
    dct_btn_upd_inp[s_lcl_key] = tkinter.Button(frame_inputfiles,
                                                image=img_update,
                                                bg=color_bg,
                                                activebackground=color_actbg,
                                                foreground=color_fg,
                                                activeforeground=color_fg,
                                                highlightbackground=color_bg,
                                                bd=0)
    dct_btn_upd_inp[s_lcl_key].grid(row=i, column=2, pady=n_widg_pady, padx=n_widg_padx)
    # search button
    dct_btn_search_inp[s_lcl_key] = tkinter.Button(frame_inputfiles,
                                                   text='Search',
                                                   image=img_open,
                                                   compound=LEFT,
                                                   bg=color_bg_alt,
                                                   activebackground=color_actbg,
                                                   foreground=color_fg,
                                                   activeforeground=color_fg,
                                                   highlightbackground=color_bg_alt,
                                                   bd=0)
    dct_btn_search_inp[s_lcl_key].grid(row=i, column=3, pady=n_widg_pady, padx=n_widg_padx)
    # about button
    dct_btn_about_inp[s_lcl_key] = tkinter.Button(frame_inputfiles,
                                                  text='About',
                                                  image=img_about,
                                                  compound=LEFT,
                                                  bg=color_bg_alt,
                                                  activebackground=color_actbg,
                                                  foreground=color_fg,
                                                  activeforeground=color_fg,
                                                  highlightbackground=color_bg_alt, bd=0)
    dct_btn_about_inp[s_lcl_key].grid(row=i, column=4, pady=n_widg_pady, padx=n_widg_padx)


# >> Parameters
dct_lbls_params = dict()
dct_etr_params = dict()
dct_btn_upd_params = dict()
for i in range(len(lst_lbls_params)):
    s_lcl_key = lst_lbls_params[i]
    # label
    dct_lbls_params[s_lcl_key] = tkinter.Label(frame_params,
                                               text=s_lcl_key,
                                               width=12, anchor="e",
                                               bg=color_bg,
                                               activebackground=color_actbg,
                                               foreground=color_fg,
                                               activeforeground=color_fg)
    dct_lbls_params[s_lcl_key].pack(side=LEFT)
    # entry
    dct_etr_params[s_lcl_key] = tkinter.Entry(frame_params,
                                              width=6,
                                              bg=color_bg_alt,
                                              foreground=color_fg,
                                              selectbackground=color_actbg,
                                              selectforeground=color_fg,
                                              highlightbackground=color_bg_alt,
                                              bd=1,
                                              validate='focusout')
    dct_etr_params[s_lcl_key].pack(side=LEFT)
    # update button
    dct_btn_upd_params[s_lcl_key] = tkinter.Button(frame_params,
                                                   image=img_update,
                                                   bg=color_bg,
                                                   activebackground=color_actbg,
                                                   foreground=color_fg,
                                                   activeforeground=color_fg,
                                                   highlightbackground=color_bg,
                                                   bd=0)
    dct_btn_upd_params[s_lcl_key].pack(side=LEFT)

# >> Tool Options

# place options checkbuttons
dct_lbls_opts = dict()
dct_checks_opts = dict()
dct_var_opts = dict()
for i in range(len(lst_lbls_opts)):
    s_lcl_key = lst_lbls_opts[i]
    dct_var_opts[s_lcl_key] = BooleanVar()
    dct_lbls_opts[s_lcl_key] = tkinter.Label(frame_options,
                                             text=s_lcl_key,
                                             width=n_width_options_labels,
                                             anchor="e",
                                             bg=color_bg,
                                             activebackground=color_actbg,
                                             foreground=color_fg,
                                             activeforeground=color_fg
                                             )
    dct_checks_opts[s_lcl_key] = tkinter.Checkbutton(frame_options,
                                                     variable=dct_var_opts[s_lcl_key],
                                                     width=n_width_options_check,
                                                     bg=color_bg,
                                                     activebackground=color_actbg,
                                                     highlightbackground=color_bg,
                                                     bd=0
                                                     )
    dct_lbls_opts[s_lcl_key].pack(side=LEFT)
    dct_checks_opts[s_lcl_key].pack(side=LEFT)

dct_var_opts[lst_lbls_opts[2]].set(True)

# >> Main Board
# run button
button_run = tkinter.Button(frame_board,
                            text='Run',
                            image=img_terminal,
                            compound=LEFT,
                            width=n_width_board_button)
button_run.config(bg=color_bg_alt,
                  activebackground=color_actbg,
                  disabledforeground='grey',
                  foreground=color_fg,
                  activeforeground=color_fg,
                  highlightbackground=color_bg,
                  bd=0)
button_run.config(command=run)
button_run.config(state=DISABLED)
button_run.pack(side=RIGHT, padx=2)
# update button
button_update_entries = tkinter.Button(frame_board,
                                       text='Update',
                                       image=img_update,
                                       compound=LEFT,
                                       width=n_width_board_button)
button_update_entries.config(bg=color_bg_alt,
                             activebackground=color_actbg,
                             disabledforeground='grey',
                             foreground=color_fg,
                             activeforeground=color_fg,
                             highlightbackground=color_bg,
                             bd=0)
button_update_entries.config(command=lambda : update_all_entries(b_popup=False))
button_update_entries.pack(side=RIGHT, padx=2)


# Report Log frame widgets
scrollbar_log_y = tkinter.Scrollbar(frame_reports,
                                    bg=color_bg_alt,
                                    bd=0,
                                    activebackground=color_actbg)
scrollbar_log_x = tkinter.Scrollbar(frame_reports,
                                    orient='horizontal',
                                    bg=color_bg_alt,
                                    bd=0,
                                    activebackground=color_actbg)
listbox_log = tkinter.Listbox(frame_reports,
                              height=12,
                              width=94,
                              borderwidth=0,
                              bd=0,
                              bg='black',
                              foreground=color_fg,
                              highlightbackground=color_bg,
                              yscrollcommand=scrollbar_log_y.set,
                              xscrollcommand=scrollbar_log_x.set)
scrollbar_log_y.config(command=listbox_log.yview)
scrollbar_log_x.config(command=listbox_log.xview)
listbox_log.grid(row=0, column=0)
scrollbar_log_y.grid(row=0, column=1, sticky='NS')
scrollbar_log_x.grid(row=1, column=0, sticky='WE')
listbox_log.config(state=DISABLED)
print_report_header()

# >>> Commands

# config workplace search buttons commmands
dct_btn_search_wplc[lst_lbls_wplc[0]].config(command=lambda : pick_folder(s_entry=lst_lbls_wplc[0]))
dct_btn_search_wplc[lst_lbls_wplc[1]].config(command=lambda : pick_folder(s_entry=lst_lbls_wplc[1]))
dct_btn_update_wplc[lst_lbls_wplc[0]].config(command=lambda : update_folder(s_entry=lst_lbls_wplc[0]))
dct_btn_update_wplc[lst_lbls_wplc[1]].config(command=lambda : update_folder(s_entry=lst_lbls_wplc[1]))

# config input update buttons commmands
dct_btn_upd_inp[lst_lbls_inp[0]].config(command=lambda : update_file(s_entry=lst_lbls_inp[0]))
dct_btn_upd_inp[lst_lbls_inp[1]].config(command=lambda : update_file(s_entry=lst_lbls_inp[1]))

# config input search buttons commmands
dct_btn_search_inp[lst_lbls_inp[0]].config(command=lambda : pick_file(s_entry=lst_lbls_inp[0],
                                                                      tpl_file_type=lst_types_inp[0],
                                                                      s_initialdir=dct_etr_wplc[lst_lbls_wplc[0]].get()))
dct_btn_search_inp[lst_lbls_inp[1]].config(command=lambda : pick_file(s_entry=lst_lbls_inp[1],
                                                                      tpl_file_type=lst_types_inp[1],
                                                                      s_initialdir=dct_etr_wplc[lst_lbls_wplc[0]].get()))
# config input about buttons commands
dct_btn_about_inp[lst_lbls_inp[0]].config(command=lambda : open_about_input(n_entry=0))
dct_btn_about_inp[lst_lbls_inp[1]].config(command=lambda : open_about_input(n_entry=1))


# config param update buttons
dct_btn_upd_params[lst_lbls_params[0]].config(command=lambda : update_parameter(s_entry=lst_lbls_params[0],
                                                                                s_entry_type=lst_widget_params[0]))

get_entry_metadata()

# run root window
root.mainloop()
