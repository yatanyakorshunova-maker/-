# -*- coding: utf-8 -*-

__version__ = "1.0.0"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.95, 0.95, 0.95, 1)


class MyFirstApp(App):
    def build(self):
        screen = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        self.title_label = Label(
            text="Моё первое приложение",
            font_size=40,
            color=(0.2, 0.2, 0.8, 1),
            size_hint_y=None,
            height=80
        )

        self.info_label = Label(
            text="Нажми на кнопку ниже",
            font_size=24,
            color=(0.1, 0.1, 0.1, 1),
            size_hint_y=None,
            height=60
        )

        start_button = Button(
            text="Нажми на меня",
            font_size=28,
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 0.2, 1),
            color=(1, 1, 1, 1)
        )

        start_button.bind(on_press=self.button_clicked)

        screen.add_widget(self.title_label)
        screen.add_widget(self.info_label)
        screen.add_widget(start_button)

        return screen

    def button_clicked(self, button):
        self.info_label.text = "✅ Кнопка работает! 🎉"


if __name__ == "__main__":
    MyFirstApp().run()
