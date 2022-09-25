import kivy

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

kivy.require('2.1.0')

class TelaPrincipal(GridLayout):
    sexo = ObjectProperty(None)

    def verifica(self):
        sexo = self.sexo
        nome = self.ids.nome.text
        idade = int(self.ids.idade.text)
        if idade < 25 and sexo.text == 'Feminino':
            self.ids.txtResult.text += str(nome) + '\n' + str("ACEITA!")
        else:
            self.ids.txtResult.text += str(nome) + '\n' + str("NÃO ACEITA!")
    def limpa(self):
        self.ids.nome.text = ''
        #self.sexo.text = disabled
        self.ids.idade.text = ''
        self.ids.txtResult.text = ''


class VerificaApp(App):

    def build(self):
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'width', '580')
        Config.set('graphics', 'height', '300')
        tela = TelaPrincipal()
        return tela


if __name__ == "__main__":
    VerificaApp().run()
