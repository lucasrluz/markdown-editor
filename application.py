import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

class Application(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title = "Markdown Editor")

def on_activate(app):
    win = Application(application = app)
    win.present()

app = Gtk.Application(application_id = "com.github.lucasrluz.MarkdownEditor")
app.connect("activate", on_activate)

app.run(None)
