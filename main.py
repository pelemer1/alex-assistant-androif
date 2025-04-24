from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.camera import Camera

class AlexInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.output = Label(size_hint_y=0.2, text='Szia Elemér, itt Alex. Kérdezz bármit!', valign='top')
        self.add_widget(self.output)
        self.camera = Camera(play=False)
        self.add_widget(self.camera)
        btn_layout = BoxLayout(size_hint_y=0.2)
        self.btn_cam = Button(text='Kirándulás mód', on_press=self.toggle_camera)
        self.btn_send = Button(text='Teszt üzenet', on_press=lambda x: self.show_response('Kirándulás mód aktiválva.'))
        btn_layout.add_widget(self.btn_cam)
        btn_layout.add_widget(self.btn_send)
        self.add_widget(btn_layout)
        self.input = TextInput(size_hint_y=0.1, multiline=False, hint_text='Írj ide...')
        self.input.bind(on_text_validate=self.on_enter)
        self.add_widget(self.input)

    def toggle_camera(self, instance):
        self.camera.play = not self.camera.play
        if self.camera.play:
            self.show_response('Kamera bekapcsolva: nézz körül!')
        else:
            self.show_response('Kamera kikapcsolva.')

    def on_enter(self, instance):
        msg = instance.text
        instance.text = ''
        self.show_response(f'> {msg}\nAlex: Még tanulok, de figyelek.')

    def show_response(self, text):
        self.output.text = text

class AlexApp(App):
    def build(self):
        return AlexInterface()

if __name__ == '__main__':
    AlexApp().run()
