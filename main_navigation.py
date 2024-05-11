import customtkinter as ctk
import os
from PIL import Image
import numpy as np

from frames import HomeFrame, UserFrame

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25


class NavigationTab(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame configuration
        self.grid_rowconfigure(5, weight=1)

        # main title
        self.label = ctk.CTkLabel(self,
                                  text='   AHP-based DSS',
                                  image=master.logo_image,
                                  compound='left',
                                  font=ctk.CTkFont(size=header, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # navigation buttons
        navigation_buttons_kwargs = dict(corner_radius=5, height=50, border_spacing=10,
                                         font=ctk.CTkFont(size=semi_header), fg_color='transparent',
                                         text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                         compound='left', anchor='w')
        ## home button
        self.home_button = ctk.CTkButton(self, text='Home', image=master.home_image, **navigation_buttons_kwargs)
        self.home_button.grid(row=1, column=0, sticky="ew")
        
        ## user details button
        self.user_button = ctk.CTkButton(self, text='User Details', image=master.user_image, **navigation_buttons_kwargs)
        self.user_button.grid(row=2, column=0, sticky="ew")

        ## user preference button
        self.preference_button = ctk.CTkButton(self, text='User Preference', image=master.rank_image, **navigation_buttons_kwargs)
        self.preference_button.grid(row=3, column=0, sticky="ew")

        ## criteria comparison button
        self.criteria_button = ctk.CTkButton(self, text='Criteria', image=master.criteria_image, **navigation_buttons_kwargs)
        self.criteria_button.grid(row=4, column=0, sticky="ew")

        ## list of buttons
        self.buttons = [self.home_button, self.user_button, self.preference_button, self.criteria_button]

        # appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self,
                                                  text='Appearance Mode: ',
                                                  font=ctk.CTkFont(size=normal, weight='bold'))
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(20,10), sticky='nsew')
        self.apperance_mode_menu = ctk.CTkOptionMenu(self, values=["Dark", "Light", "System"],
                                                     width=150, anchor='center', font=ctk.CTkFont(size=normal),
                                                    command=self.change_appearance_mode_event)
        self.apperance_mode_menu.grid(row=7, column=0, padx=20, pady=(0,20), sticky='s')

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title('Student-centered DSS for Major Course Selection using AHP')
        self.geometry(f'{1080}x{720}')
        self.minsize(width=500, height=300)

        # configure grid (1x2)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images
        self.load_images('images')

        # create navigation frame
        self.navigation_frame = NavigationTab(self, corner_radius=0, width=150)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew')
        
        # create home frame
        self.home_frame = HomeFrame(self, corner_radius=0, fg_color="transparent")

        # create user frame
        self.user_frame = UserFrame(self, corner_radius=0, fg_color='transparent')

        self.select_frame_by_name("home")  # sets home as default frame

    def select_frame_by_name(self, name:str):
        names = ["home", "user", "preference", 'criteria']

        # set the foreground color of selected button
        for idx, button in enumerate(self.navigation_frame.buttons):
            button.configure(fg_color=("gray75", "gray25") if names[idx] == name else "transparent")

        # show selected frame
        show_kwargs = dict(row=0, column=1, sticky="nsew")
        if name == "home":
            self.home_frame.grid(**show_kwargs)
        else:
            self.home_frame.grid_forget()

        if name == "user":
            self.user_frame.grid(**show_kwargs)
        else:
            self.user_frame.grid_forget()


    # navigation button callbacks
    def home_button_callback(self):
        self.select_frame_by_name("home")

    def user_button_callback(self):
        self.select_frame_by_name("user")
    
    def preference_button_callback(self):
        self.select_frame_by_name("preference")

    def criteria_button_callback(self):
        self.select_frame_by_name("criteria")
    
    def load_images(self, folder_name:str):
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), folder_name)
        self.logo_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "main_logo_light.png")), 
                                       dark_image=Image.open(os.path.join(image_path, "main_logo_dark.jpg")),
                                       size=(50, 50))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'home_dark.png')),
                                       dark_image=Image.open(os.path.join(image_path, 'home_light.png')),
                                       size=(30,30))
        self.user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'user_dark.png')),
                                       dark_image=Image.open(os.path.join(image_path, 'user_light.png')),
                                       size=(30,30))
        self.rank_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'list_dark.png')),
                                       dark_image=Image.open(os.path.join(image_path, 'list_light.png')),
                                       size=(30,30))
        self.criteria_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'criteria_dark.png')),
                                       dark_image=Image.open(os.path.join(image_path, 'criteria_light.png')),
                                       size=(30,30))
        self.save_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, 'save_dark.png')),
                                       dark_image=Image.open(os.path.join(image_path, 'save_light.png')),
                                       size=(30,30))
        self.next_image = ctk.CTkImage(Image.open(os.path.join(image_path, 'next_light.png')),
                                       size=(30,30))
        self.back_image = ctk.CTkImage(Image.open(os.path.join(image_path, 'back_light.png')),
                                       size=(30,30))

if __name__ == "__main__":
    app = App()
    app.mainloop()
