# -*- coding: utf-8 -*-
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB

uiapp = __revit__                          # noqa
app = __revit__.Application                # noqa
doc = __revit__.ActiveUIDocument.Document  # noqa

def get_parameters(file):
    f_doc = app.OpenDocumentFile(
        DB.FilePath(file),
        DB.OpenOptions())
    f_manager = f_doc.FamilyManager
    parameters = []
    for i in f_manager.GetParameters():
        if i.Definition.Name not in parameters:
            parameters.append(i.Definition.Name)
    return parameters

def button2click(text, global_files, selectedItem, checked, progress_bar):
    for file in global_files:
        f_doc = app.OpenDocumentFile(
            DB.FilePath(file),
            DB.OpenOptions()
        )
        f_manager = f_doc.FamilyManager
        parameter = f_manager.get_Parameter(selectedItem)
        with DB.Transaction(f_doc, 'Modify File') as t:
            t.Start()
            if parameter:
                for f_type in f_manager.Types:
                    f_manager.CurrentType = f_type
                    if checked:
                        f_manager.SetFormula(
                            parameter,
                            str(text))
                    else:
                        f_manager.Set(
                            parameter,
                            str(text))
            t.Commit()
        f_doc.Close()
        progress_bar.PerformStep()
