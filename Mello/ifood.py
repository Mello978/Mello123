from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.scrollview import ScrollView

class BurgerShopApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Define a cor principal
        self.theme_cls.accent_palette = "Teal"   # Cor de destaque
        
        # Layout principal
        layout = BoxLayout(orientation="vertical")
        
        # Título do site
        title = MDLabel(
            text="Burger Shop",
            theme_text_color="Secondary",
            halign="center",
            font_style="H3",
            size_hint=(1, 0.1)
        )
        
        layout.add_widget(title)
        
        # ScrollView para os hambúrgueres
        scroll_view = ScrollView()
        card_layout = MDGridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        card_layout.bind(minimum_height=card_layout.setter('height'))
        
        # Lista de hambúrgueres
        burgers = [
            {"name": "Cheeseburger", "price": "R$ 15,00"},
            {"name": "Bacon Burger", "price": "R$ 18,00"},
            {"name": "Veggie Burger", "price": "R$ 20,00"},
            {"name": "Chicken Burger", "price": "R$ 17,00"},
        ]
        
        # Criando os cards de hambúrgueres
        for burger in burgers:
            card = MDCard(
                size_hint=(None, None),
                size=("280dp", "180dp"),
                pos_hint={"center_x": 0.5},
                elevation=10,
                padding=10,
            )
            
            # Layout do card
            card_box = BoxLayout(orientation="vertical", spacing=10)
            
            # Nome do hambúrguer
            name_label = MDLabel(
                text=burger["name"],
                theme_text_color="Primary",
                size_hint_y=None,
                height="48dp",
                halign="center",
                font_style="H5"
            )
            
            # Preço do hambúrguer
            price_label = MDLabel(
                text=burger["price"],
                theme_text_color="Secondary",
                size_hint_y=None,
                height="48dp",
                halign="center",
                font_style="H6"
            )
            
            # Botão de adicionar ao carrinho
            add_button = MDRaisedButton(
                text="Adicionar ao Carrinho",
                size_hint=(None, None),
                size=("200dp", "40dp"),
                pos_hint={"center_x": 0.5},
                on_release=lambda x, burger=burger: self.add_to_cart(burger)
            )
            
            # Adicionando os componentes ao card
            card_box.add_widget(name_label)
            card_box.add_widget(price_label)
            card_box.add_widget(add_button)
            
            card.add_widget(card_box)
            card_layout.add_widget(card)
        
        # Adicionando o ScrollView com os hambúrgueres ao layout
        scroll_view.add_widget(card_layout)
        layout.add_widget(scroll_view)
        
        return layout
    
    def add_to_cart(self, burger):
        # Simula a adição ao carrinho e exibe um popup
        print(f'{burger["name"]} foi adicionado ao carrinho!')

BurgerShopApp().run()