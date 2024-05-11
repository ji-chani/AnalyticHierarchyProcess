import customtkinter as ctk

# text sizes
global normal, average, semi_header, header
normal, average, semi_header, header = 15, 18, 20, 25

class UserFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # frame configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        # create instructions
        self.instructions_label = ctk.CTkLabel(self, text='Instructions: ', font=ctk.CTkFont(size=semi_header, weight="bold"))
        self.instructions_label.grid(row=0, column=0, padx=20, pady=(20,10), sticky="w")

        instructions_text = "Insert instructions here ... \n\n " + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n \n" * 20
        self.instructions = ctk.CTkTextbox(self, width=250, height=300, 
                                           font=ctk.CTkFont(size=average))
        self.instructions.grid(row=1, column=0, padx=20, pady=(0,20), sticky='new')
        self.instructions.insert(index="0.0", text=instructions_text)
        self.instructions.configure(state="disabled")

        # degree program option menu
        self.deg_prog_label = ctk.CTkLabel(self, text="Degree Program", anchor='center',
                                           font=ctk.CTkFont(size=average, weight='bold'))
        self.deg_prog_label.grid(row=2, column=0, pady=(0,15))
        self.deg_prog = ctk.CTkOptionMenu(self, corner_radius=5, width=150, anchor='center',
                                          values=["BS AMAT", "BS MATH"],
                                          font=ctk.CTkFont(size=average))
        self.deg_prog.grid(row=3, column=0, pady=(0,20), sticky='ns')

        # SP/thesis option menu
        self.option_label = ctk.CTkLabel(self, text="Option", anchor='center',
                                           font=ctk.CTkFont(size=average, weight='bold'))
        self.option_label.grid(row=4, column=0, pady=(0,15))
        self.option = ctk.CTkOptionMenu(self, corner_radius=5, width=150, anchor='center',
                                        values=['Special Problem', 'Thesis'],
                                        font=ctk.CTkFont(size=average))
        self.option.grid(row=5, column=0, pady=(0,20), sticky='ns')

        # back and save frame
        self.user_back_save_frame = ctk.CTkFrame(self, **kwargs)
        self.user_back_save_frame.grid(row=6, column=0, pady=20, sticky='s')

        # back button
        self.user_back_button = ctk.CTkButton(self.user_back_save_frame, text='Back', anchor='center', bg_color='transparent',
                                              image=master.back_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.home_button_callback)
        self.user_back_button.grid(row=0, column=0, padx=10, pady=(10,10), sticky='s')

        # save button
        self.user_save_button = ctk.CTkButton(self.user_back_save_frame, text='Save', anchor='center', bg_color='transparent',
                                              image=master.save_image, compound='left',
                                              font=ctk.CTkFont(size=semi_header, weight='bold'),
                                              command=master.preference_button_callback)
        self.user_save_button.grid(row=0, column=1, padx=10, pady=(10,10), sticky='s')

