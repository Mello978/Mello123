from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.list import MDList


class BurgerShopApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"  # Define a cor principal
        self.theme_cls.accent_palette = "Teal"  # Cor de destaque
        
        # Layout principal
        self.layout = BoxLayout(orientation="vertical")
        
        # Título do site
        title = MDLabel(
            text="Burger Shop",
            theme_text_color="Secondary",
            halign="center",
            font_style="H3",
            size_hint=(1, 0.1),
        )
        
        self.layout.add_widget(title)
        
        # ScrollView para os hambúrgueres
        scroll_view = ScrollView()
        card_layout = MDGridLayout(cols=1, padding=10, spacing=10, size_hint_y=None)
        card_layout.bind(minimum_height=card_layout.setter("height"))
        
        # Lista de hambúrgueres
        self.burgers = [
            {"name": "Cheeseburger", "price": "R$ 15,00"},
            {"name": "Bacon Burger", "price": "R$ 18,00"},
            {"name": "Veggie Burger", "price": "R$ 20,00"},
            {"name": "Chicken Burger", "price": "R$ 17,00"},
        ]
        
        # Carrinho de compras
        self.cart = []
        
        # Criando os cards de hambúrgueres
        for burger in self.burgers:
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
                font_style="H5",
            )
            
            # Preço do hambúrguer
            price_label = MDLabel(
                text=burger["price"],
                theme_text_color="Secondary",
                size_hint_y=None,
                height="48dp",
                halign="center",
                font_style="H6",
            )
            
            # Botão de adicionar ao carrinho
            add_button = MDRaisedButton(
                text="Adicionar ao Carrinho",
                size_hint=(None, None),
                size=("200dp", "40dp"),
                pos_hint={"center_x": 0.5},
                on_release=lambda x, burger=burger: self.add_to_cart(burger),
            )
            
            # Adicionando os componentes ao card
            card_box.add_widget(name_label)
            card_box.add_widget(price_label)
            card_box.add_widget(add_button)
            
            card.add_widget(card_box)
            card_layout.add_widget(card)
        
        # Adicionando o ScrollView com os hambúrgueres ao layout
        scroll_view.add_widget(card_layout)
        self.layout.add_widget(scroll_view)
        
        # Botão para mostrar o carrinho
        show_cart_button = MDRaisedButton(
            text="Mostrar Carrinho",
            size_hint=(None, None),
            size=("200dp", "40dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.show_cart,
        )
        
        self.layout.add_widget(show_cart_button)
        
        return self.layout

    def add_to_cart(self, burger):
        # Adiciona o item ao carrinho
        self.cart.append(burger)
        print(f'{burger["name"]} foi adicionado ao carrinho!')

    def remove_from_cart(self, burger):
        # Remove o item do carrinho
        if burger in self.cart:
            self.cart.remove(burger)
            print(f'{burger["name"]} foi removido do carrinho!')
            self.show_cart(None)  # Atualiza a interface após remoção

    def show_cart(self, instance):
        # Exibe o conteúdo do carrinho
        cart_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        if not self.cart:
            cart_layout.add_widget(MDLabel(text="Carrinho vazio", halign="center"))
        else:
            # Lista de itens no carrinho
            cart_list = MDList()
            for item in self.cart:
                cart_item = BoxLayout(orientation="horizontal", size_hint_y=None, height="50dp")
                
                # Exibe o nome e preço do item
                cart_item.add_widget(MDLabel(text=f'{item["name"]} - {item["price"]}', size_hint_x=0.8))
                
                # Botão para remover o item do carrinho
                remove_button = MDRaisedButton(
                    text="Remover",
                    size_hint=(None, None),
                    size=("80dp", "30dp"),
                )
                
                # Corrigindo o fechamento
                remove_button.bind(
                    on_release=lambda btn, burger=item: self.remove_from_cart(burger)
                )
                
                cart_item.add_widget(remove_button)
                cart_list.add_widget(cart_item)
            
            cart_layout.add_widget(cart_list)

        back_button = MDRaisedButton(
            text="Voltar",
            size_hint=(None, None),
            size=("200dp", "40dp"),
            pos_hint={"center_x": 0.5},
            on_release=self.back_to_main,
        )
        
        cart_layout.add_widget(back_button)
        self.layout.clear_widgets()
        self.layout.add_widget(cart_layout)

    def back_to_main(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.build())


# Iniciar o app
if __name__ == "__main__":
    BurgerShopApp().run()
