from pynput import mouse

#buscando as coordenadas da tela do computador
def on_click(x, y, button, pressed):
    if not pressed and button == mouse.Button.middle:
        print(x, y)

#fazendo o click esquerdo do mouse
with mouse.Listener(on_click=on_click) as coordenadas:
    coordenadas.join()

