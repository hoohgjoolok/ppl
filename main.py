from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import mainthread

# استيراد طلب الأذونات للأندرويد
from android.permissions import request_permissions, Permission, check_permission
from android import mActivity

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.status_label = Label(text="يرجى الضغط على دخول")
        self.add_widget(self.status_label)

        self.login_button = Button(text="دخول", size_hint=(1, 0.3))
        self.login_button.bind(on_press=self.request_permissions_and_login)
        self.add_widget(self.login_button)

    def request_permissions_and_login(self, instance):
        # قائمة الأذونات المطلوبة
        permissions = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_SMS]

        # طلب الأذونات
        request_permissions(permissions, self.permissions_callback)

    @mainthread
    def permissions_callback(self, permissions, grants):
        # تفحص إن تم منح كل الأذونات
        if all(grants):
            self.status_label.text = "مرحبا"
        else:
            self.status_label.text = "لم تُمنح جميع الأذونات"


class MyApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    MyApp().run()