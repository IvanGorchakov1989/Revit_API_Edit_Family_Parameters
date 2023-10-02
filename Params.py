# -*- coding: utf-8 -*-
import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit import DB

uiapp = __revit__                          # noqa
app = __revit__.Application                # noqa
doc = __revit__.ActiveUIDocument.Document  # noqa

# def unit_converter(
#         doc,
#         value,
#         to_internal=False,
#         unit_type=None,
#         number_of_digits=None):
#     display_units = doc.GetUnits().GetFormatOptions(unit_type).DisplayUnits
#     method = DB.UnitUtils.ConvertToInternalUnits if to_internal \
#         else DB.UnitUtils.ConvertFromInternalUnits
#     if number_of_digits is None:
#         return method(value, display_units)
#     elif number_of_digits > 0:
#         return round(method(value, display_units), number_of_digits)
#     return int(round(method(value, display_units), number_of_digits))

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

def button2click(text, global_files, selectedItem, checked):
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