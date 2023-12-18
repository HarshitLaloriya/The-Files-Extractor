import os, shutil
import customtkinter as ctk
from PIL import Image,ImageTk

ctk.set_appearance_mode("dark")  

extensions = {  'VIDEO' : ['.webm','.flv','.mp4','.gif'],
                'AUDIO' : ['.mp3','.acc', '.3gp', '.wav'],
                'IMAGE' : ['.jpeg','.jpg','.png','.heif'],
                'DOCUMENT' : ['.pdf','.docx','.pptx','.ppt','.py','.ipynb','.txt','.csv','.xlsv','.odt','.rtf','.txt','.htm','.html','.xml','.tar','.rar','.zip']
             }

# --------- MAIN WINDOW ----------
root = ctk.CTk()
root.geometry('850x520')
root.title('File Extractor')
root.resizable(False,False)


#-------------- code for title --------------------
frame1 = ctk.CTkFrame(master= root)
frame1.grid(row = 0, padx = 200, pady = 10)
open_image = Image.open("./assets/x.png")
test = ImageTk.PhotoImage(open_image)
title = ctk.CTkLabel(master= frame1,text='',image=test)
title.grid(row = 0, padx = 5, pady = 5)
# ------------------------------------------------

# ----------------- file drive location function ----------------

def loc_check():
    if os.path.exists(entry_box_1_data.get()):
        entry_box_1_button.configure( text = 'success', fg_color= 'green', hover_color = 'green')
        print(entry_box_1_data.get())
    else:
        entry_box_1_button.configure( text = 'INVALID PATH!!', fg_color = 'red')
# ---------------------------------------------------------------

files_location = []
# ----------------- option menu function ------------------------
def search_files():
    files_location.clear()
    count = 0
    if os.path.exists(entry_box_1_data.get()) and option_menu_variable.get().strip() in list(extensions.keys()) :
        for loc,dir,l_file in os.walk(entry_box_1_data.get()):
            for filename in l_file:
                for ex in extensions[option_menu_variable.get().strip()]:
                    if filename.endswith(ex):
                        files_location.append((loc+"\\" + filename).replace('/','\\'))
                        count += 1
        if count>0:
            files_found_label_2.configure(text = f"{count}", text_color = 'green')  
            # just checking ------- let it run on terminal 
            m = 0
            for i in files_location:
                m += 1 
            print(len(files_location) == m)
            # ----------------------
        else :
            files_found_label_2.configure(text = f"{count}", text_color = 'orange')  

    else:
        pass
# ---------------------------------------------------------------

#-----------------------moving path function--------------------
def move_files():
    l = ['AUDIO', 'DOCUMENT', 'IMAGE', 'VIDEO']
    if os.path.exists(entry_box_1_data.get()) and option_menu_variable.get().strip() in l: 
        if os.path.exists(entry_box_2_data.get()):
            file_moving_location = entry_box_2_data.get() + '\\FILE EXTRACTOR'
            if os.path.exists(file_moving_location):
                shutil.rmtree(file_moving_location)
                print('deleted')
            os.mkdir(file_moving_location)
            for i in l :
                os.mkdir(file_moving_location+f'\\{i}')
            print('created')

            
            dependent_variable = 0
            for i  in files_location:
                shutil.move(i, f"{file_moving_location}\\{option_menu_variable.get().strip()}\\")
                dependent_variable += 1
           
            if dependent_variable == len(files_location):
                final_label = ctk.CTkButton(master= frame_3, text = f'Successfully Moved all Files', fg_color='yellow', text_color='black', hover= False)
                final_label.grid(row = 2, padx = 10 , pady = 10)
                option_menu_button.configure( text = f'All Moved', fg_color = 'green', hover = False,command = None,)

            print(f'{dependent_variable} \\ {len(files_location)} Files moved successfully')
            entry_box_2_button.configure(text = 'Done', fg_color = 'green',hover = False, command = None)
        else:
            entry_box_2_button.configure(text = 'Invalid path !!', fg_color = 'red')

#---------------------------------------------------------------

#--------------- code for location -----------------------------
frame2 = ctk.CTkFrame(master=root)
frame2.grid(row = 1, padx = 10, pady = 30)

walk_into = ctk.CTkLabel(master=frame2, text= 'FILES DRIVE PATH', font=('SMALL FONTS',24), text_color='#ECF0F1')
walk_into.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w' )

entry_box_1_data = ctk.StringVar()

entry_box_1 = ctk.CTkEntry(master= frame2,width= 400, textvariable= entry_box_1_data)
entry_box_1.grid(row = 0, column = 1, padx = 10, pady = 10)

entry_box_1_button = ctk.CTkButton(master= frame2, text= 'check', hover_color='purple', command=loc_check)
entry_box_1_button.grid(row = 0, column = 2, padx = 10, pady = 10)

# --------------- option menu ------------------
file_type_label = ctk.CTkLabel(master= frame2, text='SELECT FILE TYPE', font=('SMALL FONTS', 24), text_color='#F39C12')
file_type_label.grid(row = 1, column = 0, padx = 10, pady = 20, sticky = 'w')

option_menu_variable = ctk.StringVar()
option_menu_variable.set('SELECT ANY OF THE FILE TYPE')

option_menu = ctk.CTkOptionMenu(master = frame2, width= 400,values=[i + 80*" " for i in extensions.keys()], variable= option_menu_variable, button_color = 'purple')
option_menu.grid(row = 1, column = 1, padx = 10, pady = 10)

option_menu_button = ctk.CTkButton(master= frame2, text='search',hover_color='purple', command= search_files)
option_menu_button.grid(row = 1, column = 2, padx = 10, pady = 10)
# --------------- -------------------------------

new_location = ctk.CTkLabel(master = frame2, text='MOVE FILES HERE', text_color='#ECF0F1', font=('SMALL FONTS', 24))
new_location.grid(row = 2, column = 0, sticky = 'w', padx = 10, pady = 10)

entry_box_2_data = ctk.StringVar()
entry_box_2_data.set(f'{os.getcwd()}')
entry_box_2 = ctk.CTkEntry(master=frame2, width=400, textvariable= entry_box_2_data)
entry_box_2.grid(row = 2, column = 1, padx = 10, pady = 10)

entry_box_2_button = ctk.CTkButton(master= frame2, text= 'check', hover_color='purple', command=move_files)
entry_box_2_button.grid(row = 2, column = 2, padx = 10, pady = 10)
#-----------------------------------------------------

#---------------- last label ----------------------
frame_3 = ctk.CTkFrame(master= root)
frame_3.grid(row = 2, padx = 10, pady = 20) 

files_found_label = ctk.CTkButton(master=frame_3, text="TOTAL FILE'S FOUND", font=('small fonts', 20), fg_color='#145A32',hover = 'False')
files_found_label.grid(row = 0, padx = 10, pady = 10)

files_found_label_2 = ctk.CTkLabel(master=frame_3, text='0', font = ('small fonts', 30),text_color='red')
files_found_label_2.grid(row = 1)
#-------------------------------------------------


root.mainloop()
