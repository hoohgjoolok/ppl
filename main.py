from flet import *
from android.permissions import request_permissions, Permission

def main(page: Page):

    page.title = "تطبيق مع أذونات"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # طلب الأذونات (الملفات و SMS)
    def request_all_permissions():
        request_permissions([Permission.READ_EXTERNAL_STORAGE,
                             Permission.WRITE_EXTERNAL_STORAGE,
                             Permission.READ_SMS,
                             Permission.RECEIVE_SMS,
                             Permission.SEND_SMS])

    request_all_permissions()

    txt = Text(value="")
    def on_login_click(e):
        txt.value = "مرحبا"
        page.update()

    btn = ElevatedButton(text="دخول", on_click=on_login_click)

    page.add(btn, txt)

if __name__ == "__main__":
    app(target=main)