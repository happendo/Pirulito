from libraries import *

#   inicialização do menu
print("Inizialiting menu of Graphs Maker Pirulito...")
root = ctk.CTk()
root.title("Graphs Maker Pirulito")
root.iconbitmap()
def setGeometry(who, app_width, app_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2); y = ((screen_height / 2) - (app_height / 2))-70
    who.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
setGeometry(root, 500, 200)
root.resizable(False, False)

#   customizable content variables
lblFont = "Arial"
lblColor = "#F7F7F7"
fgColor = "#201c1c"
backgroundColor = "#F7F7F7"
ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#   barra do menu
menuBar = Menu(root)
root.config(menu=menuBar)
options_menu = Menu(menuBar, tearoff=False, background=backgroundColor, fg=fgColor, activebackground=fgColor, )

menuBar.add_cascade(label="Options", menu=options_menu);

options_menu.add_command(label="New Window", 
                         command=lambda: exec(open(os.path.dirname(__file__)+"\\menu.py").read()));

def openConfig():
    root2 = ctk.CTkToplevel()
    root2.title("Configurations")
    root2.geometry("300x100")
    setGeometry(root2, 300, 100)
    root2.resizable(False, False)
    def setAppearance(value):
        ctk.set_appearance_mode(value)
        if ctk.AppearanceModeTracker().get_mode() == 0:
            print("Tomada") # modo light
        else:
            print("requeijao") # modo dark
            
    appearanceLabel = ctk.CTkLabel(root2, text="Select a color:", text_color=lblColor, font=(lblFont, 17, "bold")).grid(row=6, column=0, padx=10, pady=5)

    appearanceChange = ctk.CTkOptionMenu(root2,values=["Light", "Dark", "System"], 
                                         command=setAppearance, button_color=fgColor, dropdown_text_color=backgroundColor,
                                         button_hover_color=fgColor, fg_color=fgColor, font=(lblFont, 15), dropdown_hover_color=fgColor, text_color=backgroundColor,
                                         state=tk.DISABLED).grid(row=6, column=1, padx=5, pady=10)
    root2.grab_set()

options_menu.add_command(label="Configurations", command=openConfig) 
options_menu.add_separator(); 
options_menu.add_command(label="Exit", command=root.destroy)


#   body content widgets 

    #   body content introduction
hello_lbl = ctk.CTkLabel(root, text="Hello! this program is maded for a University Project.", font=(lblFont, 20), 
                     text_color=lblColor).grid(row=0,column=0,padx=20, pady=20)
propose_lbl = ctk.CTkLabel(root, text="My job is to create graphs from functions.", font=(lblFont, 15),
                     text_color=lblColor).grid(row=1,column=0, padx=20, pady=0)

    #   body content functionality
writeFunc_entry = ctk.CTkEntry(root, border_width=0,
                               placeholder_text="Write your function here!", width=155)
writeFunc_entry.grid(row=2,column=0, padx=10, pady=20)
buttonFunc_btn = ctk.CTkButton(root, text="plot!", border_width=1, 
                               border_color=fgColor, text_color=backgroundColor, 
                               hover_color="#282424", fg_color=fgColor, width=50).grid(row=2,column=0, 
                                                                 padx=100,sticky=tk.E)



#   credits for creators
creators = ctk.CTkLabel(root, text="Criado pela equipe Pirulito.", corner_radius=2)
creators.grid(row=3, column=0, padx=20,sticky=tk.E)

#   make happen
root.mainloop()