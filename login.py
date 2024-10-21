import flet as ft
import pyrebase
# mude a variável firebaseConfig para a de vocês 
firebaseConfig = {
'apiKey': "AIzaSyDHQvqxGrvewaoAgs6nw04z-Y_yBGIkoc0",
  'authDomain': "app-faculdade-6a57e.firebaseapp.com",
  'projectId': "app-faculdade-6a57e",
  'storageBucket': "app-faculdade-6a57e.appspot.com",
  'messagingSenderId': "655814165650",
  'appId': "1:655814165650:web:3df50279ad81fd54fd124b",
  'databaseURL' : "https:appfaculdade.firebaseio.com",
  'measurementId': "G-4PHP45KVP1"
  }

firebase = pyrebase.initialize_app(firebaseConfig)
auth= firebase.auth()

# Função que cria a página
def main(page: ft.page):
    page.title = "App Faculdade"
    page.window_width = 400
    page.window_height = 600
    page.theme_mode = 'white'
    page.bgcolor = 'white'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.spacing = 20
    page.window.maximizable = False

    #Função que cria e define a condição de login
    def btn_login(e):
        try:
            auth.sign_in_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content = ft.Text(
                    value = 'Login realizado com sucesso!'
                ),
                bgcolor= 'green',
                action='OK',
                duration= 2500
            )
            page.snack_bar.open = True
            usuario.value = None
            senha.value = None
            page.remove(btn_logar, botao_novo, usuario, senha, botao_msg) # remove os objetos da tela se o login estiver correto
            page.add(bemvindo, botao_voltar) # adiciona o botão voltar a tela
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content = ft.Text(
                    value='Email ou senha estão inválidos. Tente novamente!'
                ),
                bgcolor='red',
                action="OK",
                duration= 2500
            )
            page.snack_bar.open = True
            page.update()
    
    # Função do botão de mensagem
    def btn_msg(e):
        page.snack_bar = ft.SnackBar(
                content = ft.Text(
                    value='Bem vindo ao app do Sabor Supremo, faça seu login e aproveite para pedir um delivery! ;D',
                    color= 'white'
                ),
                bgcolor='black',
                action="OK",
                duration= 2500
            )
        page.snack_bar.open = True
        page.update()
    # Função responsável por transformar a página de login (fazer os objetos removidos no login, voltar)
    def btn_voltar(e):
        page.add(usuario, senha, btn_logar, botao_novo, botao_msg)
        page.remove(bemvindo, botao_voltar)
        page.update()  

    # Função que cria e define a condição de cadastro do usuário
    def btn_novo(e):
        try:
            auth.create_user_with_email_and_password(usuario.value, senha.value)
            page.snack_bar = ft.SnackBar(
                content= ft.Text(
                    value = 'Usuário criado com sucesso!'
                ),
                bgcolor='green',
                action='OK',
                duration= 2500
            )
            page.snack_bar.open = True
            usuario.value = None
            senha.value = None
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content= ft.Text(
                    value= 'Ocorreu um erro ao criar um novo usuário.'
                ),
                bgcolor='red',
                action='OK',
                duration= 2500
            )
            page.snack_bar.open = True
            page.update()
    
    img = ft.Image(
        src=f"logo.png",
        width=200,
        height=150,
        fit=ft.ImageFit.CONTAIN,
    )
    bemvindo = ft.Text(
                value = 'Seja Bem-vindo ao Sabor Supremo',
                size = 15,
                weight = 'bold',
                color = 'blue'
    )
    usuario = ft.TextField(
        hint_text = 'Email/Contato',
        label = 'Email/Contato',
        width = 200,
        border_color = 'white',
        color = 'blue',
        label_style = ft.TextStyle(
            color = 'blue' 
        )
    )
    senha = ft.TextField(
        hint_text = 'Senha',
        label= 'Senha',
        width= 200,
        height= 50,
        border_color= 'white',
        label_style= ft.TextStyle(
            color= 'blue'
        ),
        password= True,
        can_reveal_password= True
    )
    btn_logar = ft.ElevatedButton(
        text='Login',
        color= 'blue',
        bgcolor= 'Black',
        width= 200,
        height= 50,
        on_click= btn_login
    )
    botao_novo = ft.ElevatedButton(
        text= 'Criar conta',
        color= 'White',
        bgcolor= 'gray',
        width= 200,
        height= 50,
        on_click= btn_novo
    )
    botao_voltar = ft.ElevatedButton(
        text='Voltar',
        color= 'blue',
        bgcolor= 'Black',
        width= 200,
        height= 50,
        on_click= btn_voltar
    )
    botao_msg = ft.ElevatedButton(
        text='+',
        color= 'blue',
        bgcolor= 'Black',
        width= 60,
        height= 50,
        on_click= btn_msg
    )

    # Adiciona todos os elementos à página
    page.add(img, usuario, senha, btn_logar, botao_novo, botao_msg)
# Diz ao flet que deve iniciar a função MAIN
ft.app(target=main)