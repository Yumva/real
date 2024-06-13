from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.grid = GridLayout(cols=4)
        self.operations = ['+', '-', '*', '/']
        self.text_input = TextInput(multiline=False)
        self.grid.add_widget(self.text_input)

        for i in range(1, 10):
            self.grid.add_widget(Button(text=str(i), on_press=self.on_button_press))

        for op in self.operations:
            self.grid.add_widget(Button(text=op, on_press=self.on_button_press))

        self.grid.add_widget(Button(text='C', on_press=self.clear_text))
        self.grid.add_widget(Button(text='0', on_press=self.on_button_press))
        self.grid.add_widget(Button(text='=', on_press=self.calculate_result))

        return self.grid

    def on_button_press(self, instance):
        self.text_input.text += instance.text

    def clear_text(self, instance):
        self.text_input.text = ''

    def calculate_result(self, instance):
        try:
            self.text_input.text = str(eval(self.text_input.text))
        except Exception as e:
            self.text_input.text = 'Error'


if __name__ == '__main__':
    CalculatorApp().run()

