import customtkinter as CTk


class App(CTk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("630x420")
        self.title("Рассчет начальных геологических запасов нефти")
        self.resizable(False, False)
        self.configure(bg="white")

        self.label0 = CTk.CTkLabel(master=self, text="", height=420, width=630, bg_color="white")
        self.label0.place(x=0, y=0)

        self.label1 = CTk.CTkLabel(master=self, text="Площадь залежи, км2", height=30, width=150, fg_color="white",
                                   font=("GOST type B", 24), bg_color="white", text_color="black", corner_radius=10)
        self.label1.place(x=20, y=20)
        self.my_entry1 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry1.place(x=450, y=20)
        self.my_entry1.insert(0, "10")

        self.label2 = CTk.CTkLabel(master=self, text="Ср. эфф. нефтенасыщ. толщина, м", height=30, width=300,
                                   fg_color="white", font=("GOST type B", 24), bg_color="white", text_color="black",
                                   corner_radius=20)
        self.label2.place(x=20, y=70)
        self.my_entry2 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry2.place(x=450, y=70)
        self.my_entry2.insert(0, "15")

        self.label3 = CTk.CTkLabel(master=self, text="Пористость", height=30, width=150, fg_color="white",
                                   font=("GOST type B", 24), bg_color="white", text_color="black", corner_radius=20)
        self.label3.place(x=20, y=120)
        self.my_entry3 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry3.place(x=450, y=120)
        self.my_entry3.insert(0, "0.2")

        self.label4 = CTk.CTkLabel(master=self, text="Начальная нефтенасыщ.", height=30, width=150, fg_color="white",
                                   font=("GOST type B", 24), bg_color="white", text_color="black", corner_radius=20)
        self.label4.place(x=20, y=170)
        self.my_entry4 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry4.place(x=450, y=170)
        self.my_entry4.insert(0, "0.8")

        self.label5 = CTk.CTkLabel(master=self, text="Плотность нефти, г/см3", height=30, width=150, fg_color="white",
                                   font=("GOST type B", 24), bg_color="white", text_color="black", corner_radius=20)
        self.label5.place(x=20, y=220)
        self.my_entry5 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry5.place(x=450, y=220)
        self.my_entry5.insert(0, "0.85")

        self.label6 = CTk.CTkLabel(master=self, text="Объемный коэффициент нефти", height=30, width=150,
                                   fg_color="white", font=("GOST type B", 24), bg_color="white", text_color="black",
                                   corner_radius=20)
        self.label6.place(x=20, y=270)
        self.my_entry6 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry6.place(x=450, y=270)
        self.my_entry6.insert(0, "0.8")

        self.label7 = CTk.CTkLabel(master=self, text="Отбор нефти на момент рассч., млн.т.", height=30, width=150,
                                   fg_color="white", font=("GOST type B", 24), bg_color="white", text_color="black",
                                   corner_radius=20)
        self.label7.place(x=20, y=320)
        self.my_entry7 = CTk.CTkEntry(master=self, height=30, width=150, font=("GOST type B", 20), bg_color="white",
                                      text_color="black", corner_radius=10)
        self.my_entry7.place(x=450, y=320)
        self.my_entry7.insert(0, "5")

        # Атрибут для хранения ссылки на виджет результата
        self.my_entry8 = None

        def parse_entry(entry):
            return float(entry.replace(',', '.'))

        def calculate():
            area = parse_entry(self.my_entry1.get())
            Thickness = parse_entry(self.my_entry2.get())
            Porosity = parse_entry(self.my_entry3.get())
            Startingoil = parse_entry(self.my_entry4.get())
            Plotnost = parse_entry(self.my_entry5.get())
            Value = parse_entry(self.my_entry6.get())
            Otbor = parse_entry(self.my_entry7.get())
            my_Result = (area * Thickness * Porosity * Startingoil * Plotnost * Value + Otbor)
            my_Result = round(my_Result,4)
            my_Result = str(my_Result)
            my_Result = my_Result +" млн.т."
            print(my_Result)
            # Удаление предыдущего виджета результата, если он существует
            if self.my_entry8 is not None:
                self.my_entry8.destroy()

            # Создание нового виджета результата
            self.my_entry8 = CTk.CTkLabel(master=self, text=my_Result, height=30, width=150, fg_color="white",
                                          font=("GOST type B", 24), bg_color="white", text_color="black",
                                          corner_radius=20)
            self.my_entry8.place(x=450, y=370)

        self.Button1 = CTk.CTkButton(master=self, text="Рассчет", command=calculate, height=30, width=150,
                                     fg_color="transparent", font=("GOST type B", 24), bg_color="white",
                                     border_width=1, border_color="black", text_color="black", corner_radius=20)
        self.Button1.place(x=20, y=370)


if __name__ == "__main__":
    app = App()
    app.mainloop()



