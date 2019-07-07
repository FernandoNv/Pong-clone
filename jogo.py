from PPlay.window import *

janela = Window(500, 500)
janela.set_title("jogo")

janela.set_background_color((255,0,0))
text = "Fernando"
x = 150
y = 150
janela.draw_text(text, x, y, size=12, color=(0,0,0), font_name="Arial", bold=False, italic=False)
while True:
    janela.update()