import flet as ft

def main(pagina):
    Titulo = ft.Text("NetTalk")
    TituloJanelaPopUp = ft.Text("Entrar no Chat")
    CampoNomeUsuario = ft.TextField(label="Digite seu nome")

    
    Chat = ft.TextField(label="Digite sua mensagem")
    

    BotaoEnviar = ft.ElevatedButton("Enviar", on_click=lambda e: EnviarMensagem(e))
    

    LinhaChat = ft.Row([Chat, BotaoEnviar])
    

    Mensagens = ft.Column()


    def AbrirPopUp(evento):
        pagina.dialog = JanelaPopUp
        JanelaPopUp.open = True
        pagina.update()


    def EnviarMensagemTunel(mensagem):
        Mensagens.controls.append(ft.Text(mensagem))
        pagina.update()
        

    pagina.pubsub.subscribe(EnviarMensagemTunel)


    def EnviarMensagem(evento):
        texto = "{}: {}".format(CampoNomeUsuario.value, Chat.value)
        Chat.value = ""
        pagina.pubsub.send_all(texto)
        pagina.update()


    def EntrarChat(evento):
        pagina.remove(Titulo)
        pagina.remove(BotaoEntrar)
        JanelaPopUp.open = False
        EntrouChat = "{} entrou no chat".format(CampoNomeUsuario.value)
        Mensagens.controls.append(ft.Text(EntrouChat))
        pagina.add(Mensagens)
        pagina.add(LinhaChat)
        pagina.update()


    EntrarChatButton = ft.ElevatedButton("Entrar", on_click=EntrarChat)
    

    BotaoEntrar = ft.ElevatedButton("Entrar no Chat", on_click=AbrirPopUp)
    

    JanelaPopUp = ft.AlertDialog(title=TituloJanelaPopUp, content=CampoNomeUsuario, actions=[EntrarChatButton])


    pagina.add(Titulo)
    pagina.add(BotaoEntrar)

ft.app(main, view=ft.WEB_BROWSER)
