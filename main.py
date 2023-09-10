from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Date'
            icon: 'calendar'

            MDLabel:
                text: 'Введите дату отправки соообщения'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Time'
            icon: 'clock'

            MDLabel:
                text: 'Установите время'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Message'
            icon: 'text'

            MDLabel:
                text: 'Введите сообщение'
                halign: 'center'
'''
        )


Test().run()