from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
import requests
import webbrowser


class WomenSafetyApp(App):

    def build(self):

        Window.clearcolor = (0.1, 0.1, 0.15, 1)

        layout = BoxLayout(
            orientation='vertical',
            padding=50,
            spacing=40
        )

        title = Label(
            text="WOMEN SAFETY",
            font_size=32,
            color=(1, 1, 1, 1)
        )

        subtitle = Label(
            text="One Tap Emergency Protection",
            font_size=18,
            color=(0.8, 0.8, 0.8, 1)
        )

        sos_button = Button(
            text="🚨 SEND SOS",
            font_size=30,
            size_hint=(1, 0.5),
            background_color=(1, 0, 0, 1)
        )

        sos_button.bind(on_press=self.send_sos)

        layout.add_widget(title)
        layout.add_widget(subtitle)
        layout.add_widget(sos_button)

        return layout


    def send_sos(self, instance):

        # 🔊 Play alarm
        sound = SoundLoader.load("alarm.mp3")
        if sound:
            sound.play()

        # 🌍 Get location
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        location = data["loc"]
        lat, lon = location.split(",")

        maps_link = f"https://www.google.com/maps?q={lat},{lon}"
        webbrowser.open(maps_link)

        print("🚨 SOS Activated!")
        print("Location:", maps_link)

        popup = Popup(
            title="Emergency Alert",
            content=Label(text="Alert Sent Successfully"),
            size_hint=(None, None),
            size=(400, 200)
        )
        popup.open()


# ✅ VERY IMPORTANT — KEEP THIS AT BOTTOM
if __name__ == "__main__":
    WomenSafetyApp().run()