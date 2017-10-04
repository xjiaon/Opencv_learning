import os
from win32com import client
old=input('old:')
new=input('new:')
path='./'
app = client.Dispatch('Word.Application')
for a,b,c in os.walk(path):
    for c0 in c:
        
        abs=os.path.abspath(path)
        abc=(abs+a+"\\"+c0).replace('./','\\')
        
        if c0.endswith(".doc"):
            if c0.startswith("~"):
                continue
        
            print (abc)
            doc=app.Documents.Open(abc)
            #print(os.path.abspath("aa1.doc"))
            app.Visible = False
            app.ScreenUpdating = False

            app.Selection.Find.Execute(old, False, False, False, False, False, True, 1, True, new, 2)
            doc.Save()
            doc.Close()
app.Quit()
