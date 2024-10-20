import flet as ft 


#Função que cria a página
def main(page: ft.page):
    page.title = "Meu App"
    page.window_width = 300
    page.window_height = 500
    page.theme_mode = 'dark'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 20
    
    def btn_login(e):
        pass

    texto_login = ft.Text(
        value = 'Login',
        size = 42,
        weight = 'bold',
        color = 'green'
    )
    usuario = ft.TextField(
        hint_text = 'Email',
        label = 'Email',
        width = 200,
        border_color = 'white',
        color = 'green',
        label_style = ft.TextStyle(
            color = 'green' 
        )
    )
    senha = ft.TextField(
        hint_text='Senha',
        label='Senha',
        width=200,
        border_color='white',
        label_style=ft.TextStyle(
            color='green'
        ),
        password=True,
        can_reveal_password=True
    )
    botao_logar = ft.ElevatedButton(
        text='Login',
        color='green',
        bgcolor='Black',
        width=200,
        height=50,
        on_click=btn_login
    )

    #Adiciona todos os elementos na página
    page.add(texto_login, usuario, senha, botao_logar)


#Diz ao FLET que deve iniciar na função MAIN
ft.app(target=main)
    


