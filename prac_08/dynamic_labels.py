from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def build(self):
        # Sample list of names
        names = ["hao zhang", "tian", "xiao", "hao", "tian"]

        # Create the root layout
        root = BoxLayout(orientation='vertical')

        # Create a child layout to hold the labels
        label_layout = BoxLayout(orientation='vertical')

        # Dynamically create labels for each name and add them to the label layout
        for name in names:
            label = Label(text=name)
            label_layout.add_widget(label)

        # Add the label layout to the root layout
        root.add_widget(label_layout)

        return root

if __name__ == '__main__':
    DynamicLabelsApp().run()
