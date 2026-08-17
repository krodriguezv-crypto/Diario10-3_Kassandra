import flet as ft 

    

def main(page: ft.page):
    page.tittle = "Mi primera app con flet"
    mensaje = ft.Text("Aqui va un mensaje")
    nombre = ft.TextField(label="Escriba su nombre" , autofocus=True)
    
    def mostrar_mensaje(txt_mensaje):
        dialogo = ft.AlertDialog(
            title=ft.Text("Mensaje"),
            content=ft.Text(txt_mensaje)   
        )
        page.show_dialog(dialogo)
    
    def saludar(e):
        if nombre.value =="":
            mensaje.value = "Hola, desconocido"
        else:
            mensaje.value = "Hola, " + nombre.value
        mostrar_mensaje(mensaje.value)
    
    page.add(
        ft.Text("Hola Andres"),
        ft.Button("Click aqui!!!!!" , on_click = saludar),
        mensaje,
        nombre
        )

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    