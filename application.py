import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

class Application(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title = "Markdown Editor")

        self.set_default_size(800, 600)

        # Header Bar Layout
        self.headerBar = Gtk.HeaderBar()
        self.set_titlebar(self.headerBar)

        # Open File Button
        openFileButton = Gtk.Button(label = "Open File")
        openFileButton.connect("clicked", self.on_open_file_button)
        self.headerBar.pack_start(openFileButton)

        # Box Layout
        box = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 12)
        self.set_child(box)

        # Scrolled Window, Text View
        scrolledWindow = Gtk.ScrolledWindow()
        scrolledWindow.props.hexpand = True
        scrolledWindow.props.vexpand = True
        box.append(scrolledWindow)

        textView = Gtk.TextView()
        textView.set_wrap_mode(Gtk.WrapMode.WORD)
        textView.set_top_margin(30)
        textView.set_left_margin(60)
        textView.set_right_margin(60)
        textView.set_bottom_margin(30)

        self.textBuffer = textView.get_buffer()
        self.textBuffer.set_text("Hello, world")

        scrolledWindow.set_child(textView)

    # Header Bar Button
    def on_open_file_button(self, _widget):
        self.fileDialog = Gtk.FileDialog()
        self.fileDialog.open(self, None, self.on_file_opened)

    def on_file_opened(self, dialog, result):
        file = dialog.open_finish(result)

        with open(file.get_path(), "r", encoding="utf-8") as f:
            fileContent = f.read()
            self.textBuffer.set_text(fileContent)

def on_activate(app):
    win = Application(application = app)
    win.present()

app = Gtk.Application(application_id = "com.github.lucasrluz.MarkdownEditor")
app.connect("activate", on_activate)

app.run(None)
