from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# from kivy.graphics.instructions import Canvas
# from kivy.properties import 
# from kivy.core.window import Window

light_green = Color(0.3138888888888889, 1.13, 1.13, mode="hsv")

def HSVtoRGB(color1,color2,color3):
    return tuple(Color(color1, color2, color3, mode='hsv').rgba)



def getRGB(x,y,z):
    cx,cy,cz = x/255,y/255,z/255
    return (cx, cy, cz, 1)

def getHSV(val):
    data = val.split(",")
    print(data)
    x, y, z = data[0], data[1], data[2]
    a, b, c = int(x[:-1])/360, int(x[:-1])/100, int(x[:-1])/100
    return a, b, c


class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba = (1,1,1,1))
            Rectangle(pos=self.pos, size=self.size)


class YourApp(App):
    def build(self):
        root_widget = BoxLayout(orientation="vertical")

        # self.color = Color(rgba=(,0,0,1))
        # self.canvas = Canvas()
        self.output_label = MyLabel(size_hint_y=1,font_size=40,color=(0,0,0,1))


        button_symbols = ('(', ')', 'AC', 'C',
                          '1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '*',
                          '.', '0', '/', '=')
        functions = ("AC", "C", "=")

        button_grid = GridLayout(cols=4, size_hint_y=2.5)
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol, font_size=40, color=(0,0,0,1), background_color=(1, 1, 1, 0.9), background_normal="", background_down=""))

        non_function_btn = []
        for btn in button_grid.children[0:]:
            if btn.text not in functions:         
                btn.bind(on_press=self.print_in_label)

        # button_grid.children[0].background_color= getRGB(68, 255, 0)
        # button_grid.children[0].background_normal= ""
        button_grid.children[0].bind(on_press=self.evaluate)
        button_grid.children[16].bind(on_press=self.del_character)
        button_grid.children[17].bind(on_press=self.clear_screen)

        bottom_con = GridLayout(cols=2, size_hint_y=0.5)

        del_button = Button(
            text="C", font_size=45, background_color=getRGB(245, 94, 7), background_normal="")
        del_button.bind(on_press=self.del_character)

        bottom_con.add_widget(del_button)

        clear_all_button = Button(
            text='Clear', font_size=45, background_color=getRGB(255,0,0), background_normal="", border=(10,10,10,10))
        clear_all_button.bind(on_press=self.clear_screen)


        # bottom_con.add_widget(clear_all_button)

        root_widget.add_widget(self.output_label)
        root_widget.add_widget(button_grid)
        # root_widget.add_widget(bottom_con)

        return root_widget

    def print_in_label(self, instance):
        if "syntax error" in self.output_label.text:
            self.output_label.text = ""
        
        self.output_label.text += instance.text

    def resize_label_height(self, new_height):
        self.output_label.font_size = 0.5*self.label.height

    def clear_screen(self, instance):
        self.output_label.text = ""

    def del_character(self, instance):
        self.output_label.text = self.output_label.text[:-1]
        

    def evaluate(self, instance):
        try:
            self.output_label.text = str(eval(self.output_label.text))
        except:
            self.output_label.text = "syntax error"



if __name__ == "__main__":
    app = YourApp()
    app.run()

