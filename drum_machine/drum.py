"""
Modul zawiera aplikacje umozliwiajaca granie na perkusji do wbudowanej sciezki basowej (lub bez niej).
Wymagany jest pakiet pyglet.
"""
import pyglet
pyglet.options['audio'] = ('openal', 'silent')
import numpy
from pyglet.window import key
import pyglet.media as media
window = pyglet.window.Window()
x, y = window.get_location()
window.set_location(x+600, y-300)
kick = pyglet.media.load('./drum_machine/sample01.wav', streaming=False)
snare = pyglet.media.load('./drum_machine/sample02.wav', streaming=False)
openhh = pyglet.media.load('./drum_machine/sample03.wav', streaming=False)
closehh = pyglet.media.load('./drum_machine/sample04.wav', streaming=False)
leftc = pyglet.media.load('./drum_machine/sample05.wav', streaming=False)
rightc = pyglet.media.load('./drum_machine/sample06.wav', streaming=False)
bass1 = pyglet.media.load('./drum_machine/bass.wav', streaming=False)
player = pyglet.media.Player()
player.volume=0.5
witaj = pyglet.text.Label('Witaj. Wcisnij enter',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//10, y=4*window.height//5+30,
                          anchor_x='left', anchor_y='top')

label = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-30,
                          anchor_x='left', anchor_y='top')
label2 = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-60,
                          anchor_x='left', anchor_y='top')
label3 = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-90,
                          anchor_x='left', anchor_y='top')
label4 = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-120,
                          anchor_x='left', anchor_y='top')
label5 = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-150,
                          anchor_x='left', anchor_y='top')
label6 = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-180,
                          anchor_x='left', anchor_y='top')
gotowy = pyglet.text.Label('',
                          font_name='Times New Roman',
                          font_size=21,
                          x=window.width//10+10, y=4*window.height//5-210,
                          anchor_x='left', anchor_y='top')
@window.event
def on_draw():
    window.clear()
    witaj.draw()
    label2.draw()
    label3.draw()
    label4.draw()
    label5.draw()
    label6.draw()
    gotowy.draw()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ENTER:
        witaj.text = "Przypisania klawiszy:"
        label.text = "A - kick"
        label2.text = "D - snare"
        label3.text = "K - closed hihat"
        label4.text = "L - open hihat"
        label5.text = "J - right crash"
        label6.text = "H - left crash"
        gotowy.text = 'Gotowy? Nacisnij b, aby zaczac'
    if symbol == key.A:
        kick.play()
    if symbol == key.D:
        snare.play()      
    if symbol == key.L:
        openhh.play()
    if symbol == key.K:
        closehh.play()
    if symbol == key.J:
        leftc.play()
    if symbol == key.H:
        rightc.play()
    if symbol == key.B:
        player.next_source()
        player.queue(bass1)
        player.play()
pyglet.app.run()

