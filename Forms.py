# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import CheckBox, Form, Button, TextBox, ListBox, Label, OpenFileDialog, DialogResult
clr.AddReference('System.Drawing')
from System.Drawing import Point, Size
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB

from Params import get_parameters, button2click

uiapp = __revit__                          # noqa
app = __revit__.Application                # noqa
doc = __revit__.ActiveUIDocument.Document  # noqa

class Window(Form):
    def __init__(self):
        self.Size = Size(800, 600)
        self.CenterToScreen()
        self.MinimumSize = Size(800, 600)
        self.MaximumSize = Size(800, 600)
        self._initialize_components()

    def _initialize_components(self):
        self._text1 = Label()
        self._text1.Text = 'Изменение параметров в файлах семейств. Изменяет только общие у всех файлов параметры. Если параметра нет у семейства, пропускает этот файл'
        self._text1.Size = Size(800, 50)
        self._text1.Location = Point(0, 0)
        self.Controls.Add(self._text1)

        self._list_box = ListBox()
        self._list_box.Size = Size(600, 100)
        self._list_box.Location = Point(0, 50)
        self.Controls.Add(self._list_box)

        self._btn1 = Button()
        self._btn1.Text = 'Выбрать файлы'
        self._btn1.Size = Size(150, 20)
        self._btn1.Location = Point(605, 90)
        self.Controls.Add(self._btn1)
        self._btn1.Click += self.Button1Click

        self._list_box2 = ListBox()
        self._list_box2.Size = Size(600, 200)
        self._list_box2.Location = Point(0, 150)
        self.Controls.Add(self._list_box2)

        self._text3 = Label()
        self._text3.Text = 'Выберите необходимый параметр'
        self._text3.Size = Size(200, 50)
        self._text3.Location = Point(600, 250)
        self.Controls.Add(self._text3)

        self._text2 = TextBox()
        self._text2.Size = Size(200, 20)
        self._text2.Location = Point(0, 350)
        self.Controls.Add(self._text2)

        self._text4 = Label()
        self._text4.Text = 'Введите новое значение'
        self._text4.Size = Size(400, 25)
        self._text4.Location = Point(200, 355)
        self.Controls.Add(self._text4)

        self._chk = CheckBox()
        self._chk.Text = 'Это формула?'
        self._chk.Size = Size(150, 25)
        self._chk.Location = Point(0, 370)
        self.Controls.Add(self._chk)

        self._btn2 = Button()
        self._btn2.Text = 'Изменить параметр'
        self._btn2.Size = Size(150, 40)
        self._btn2.Location = Point(int(self.Size.Width / 2 - 75), 400)
        self.Controls.Add(self._btn2)
        self._btn2.Click += self.Button2Click

        self._text5 = Label()
        self._text5.Size = Size(400, 200)
        self._text5.Location = Point(int(self.Size.Width / 2 - 200), 450)
        self.Controls.Add(self._text5)

    def Button1Click(self, sender, event_args):
        FD = OpenFileDialog()
        FD.Multiselect = True
        if (FD.ShowDialog() == DialogResult.OK):
            self.global_files = []
            for s in FD.FileNames:
                if s not in self.global_files:
                    self.global_files.append(s)
            self._list_box.DataSource = None
            self._list_box.DataSource = self.global_files
            sets_parameters = []
            for glob in self.global_files:
                sets_parameters.extend(get_parameters(glob))
            self._list_box2.DataSource = list(set(sets_parameters))

    def Button2Click(self, sender, event_args):
        if self._text2.Text:
            button2click(self._text2.Text,
                         self.global_files,
                         self._list_box2.SelectedItem,
                         self._chk.Checked)
            self._text5.Text = 'Изменения сохранены'
        else:
            self._text5.Text = 'Необходимо выбрать параметр и ввести новое значение'