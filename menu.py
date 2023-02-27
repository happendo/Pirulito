from libraries import *
from plot import *

#   inicialização do menu
print("Inizialiting menu of Graphs Maker Pirulito...")
main = ctk.CTk()
main.title("Graphs Maker Pirulito")
main.iconbitmap(os.path.dirname(__file__)+"\\icons\\dark\\menu.ico")
def setGeometry(who, app_width, app_height):
    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2); y = ((screen_height / 2) - (app_height / 2))-70
    who.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
setGeometry(main, 500, 200)
main.resizable(False, False)

#   customizable content variables
ctk.set_appearance_mode("Dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
def changeColorApp():
    global lblFont, lblColor, fgColor, backgroundColor
    if ctk.AppearanceModeTracker().get_mode() == 0:
        lblFont = "Arial"
        lblColor = "#201c1c"
        fgColor = "#F7F7F7"
        backgroundColor = "#F7F7F7"
    else:
        lblFont = "Arial"
        lblColor = "#F7F7F7"
        fgColor = "#201c1c"
        backgroundColor = "#F7F7F7"
changeColorApp()

#   barra do menu
menuBar = Menu(main)
options_menu = Menu(menuBar, tearoff=False, background=backgroundColor, fg=fgColor, activebackground=fgColor)
main.config(menu=menuBar)

menuBar.add_cascade(label="Options", menu=options_menu);

def newWindow():
    choice = messagebox.askokcancel("Aviso!", 
                           "Funcionalidade em desenvolvimento, existem bugs! Se deseja continuar clique em Ok.")
    if choice == 1:
        exec(open(os.path.dirname(__file__)+"\\menu.py").read())
options_menu.add_command(label="New Window", command=newWindow)

# change color
def openConfig():
    config_Menu = ctk.CTkToplevel()
    config_Menu.title("Configurations")
    config_Menu.iconbitmap(os.path.dirname(__file__)+"\\icons\\config.ico")
    setGeometry(config_Menu, 300, 100)
    config_Menu.resizable(False, False)
    def setAppearance(value):
        ctk.set_appearance_mode(value)
        changeColorApp()
        for widget in main.winfo_children(): 
            if isinstance(widget, ctk.CTkLabel): 
                widget.configure(text_color=lblColor)
        for widget in config_Menu.winfo_children(): 
            if isinstance(widget, ctk.CTkLabel): 
                widget.configure(text_color=lblColor)
        config_Menu.destroy()
        openConfig()
            
    appearanceLabel = ctk.CTkLabel(config_Menu, text="Select a color:", text_color=lblColor, font=(lblFont, 17, "bold")).grid(row=1, column=0, padx=10, pady=5)
    appearanceChange = ctk.CTkOptionMenu(config_Menu,values=["Dark", "Light"], 
                                         command=setAppearance, button_color="#201c1c", dropdown_text_color="#F7F7F7",
                                         button_hover_color="#201c1c", fg_color="#201c1c", font=(lblFont, 15), 
                                         dropdown_hover_color="#282424", dropdown_fg_color="#201c1c", 
                                         text_color="#F7F7F7").grid(row=1, column=1, padx=5, pady=10)
    
    config_Menu.grab_set()

options_menu.add_command(label="Configurations", command=openConfig) 
options_menu.add_separator(); 
options_menu.add_command(label="Exit", command=main.destroy)

#   body content widgets 

    #   body content introduction
hello_lbl = ctk.CTkLabel(main, text="Hello! this program is maded for a University Project.", font=(lblFont, 20), 
                     text_color=lblColor).grid(row=0,column=0,padx=20, pady=20)
propose_lbl = ctk.CTkLabel(main, text="My job is to create graphs from functions.", font=(lblFont, 15),
                     text_color=lblColor).grid(row=1,column=0, padx=20, pady=0)

    #   body content functionality
    
def buttonFunc():
    
    if chooseFunc_Option.get() == "I want to write by myself!":
        buttonFunc_btn.grid(padx=114)
        chooseFunc_Option.grid_remove()
        writeFunc_entry = ctk.CTkEntry(main, border_width=0,
                               placeholder_text="Write your function here!", width=155)
        writeFunc_entry.grid(row=2,column=0, padx=10, pady=20)
        
    if chooseFunc_Option.get() == "Select from hardcoded functions":
        firstGraph()
        
def moveButton(whatToDo):
    
    selectH_lbl.grid_remove()
    buttonFunc_btn.grid(row=2,column=0, sticky=tk.E)
    if whatToDo == "do nothing :)":
        buttonFunc_btn.grid(padx=140)
    if whatToDo == "I want to write by myself!":
        buttonFunc_btn.grid(padx=103)
    if whatToDo == "Choose a archive":
        buttonFunc_btn.grid(padx=125)
    if whatToDo == "Select from hardcoded functions":
        buttonFunc_btn.grid(padx=83)

chooseFunc_Option = ctk.CTkOptionMenu(main, values=["I want to write by myself!", 
                                                          "Choose a archive", "Select from hardcoded functions"],
                                      button_color="#282424", dropdown_text_color="#F7F7F7",
                                         button_hover_color="#282424", fg_color="#282424", font=(lblFont, 13), 
                                         dropdown_hover_color="#282424", dropdown_fg_color="#282424",
                                         text_color="#F7F7F7", command=moveButton)
chooseFunc_Option.set("")
chooseFunc_Option.grid(row=2,column=0, padx=5, pady=20)

selectH_lbl = ctk.CTkLabel(main, text="Selecione uma opção:")
selectH_lbl.grid(row=2, column=0, padx=40,sticky=tk.W)

buttonFunc_btn = ctk.CTkButton(main, text="go!", border_width=1, 
                               border_color=fgColor, text_color=backgroundColor, 
                               hover_color="#282424", fg_color=fgColor, width=50, 
                               command=buttonFunc)

#   credits for creators
creators = ctk.CTkLabel(main, text="Criado pela equipe Pirulito.", corner_radius=2)
creators.grid(row=3, column=0, padx=20,sticky=tk.E)

#   make happen
main.mainloop()