import plotly.express as px
import pandas as pd
grupos = ["Leo/need", "More More Jump!", "Vivid BAD SQUAD", "WonderlandxShowtime", "Nightchord at 25", "Grupo Misto", "Leo/need", "More More Jump!", "Vivid BAD SQUAD", "WonderlandxShowtime", "Nightchord at 25", "Grupo Misto", "Leo/need", "More More Jump!", "Vivid BAD SQUAD", "WonderlandxShowtime", "Nightchord at 25", "Grupo Misto", "Leo/need", "More More Jump!", "Vivid BAD SQUAD", "WonderlandxShowtime", "Nightchord at 25", "Grupo Misto", "Leo/need", "More More Jump!", "Vivid BAD SQUAD", "WonderlandxShowtime", "Nightchord at 25", "Grupo Misto"]
tipos = ["Evento Cool", "Evento Cool","Evento Cool","Evento Cool","Evento Cool", "Evento Cool", "Evento Mysterious", "Evento Mysterious", "Evento Mysterious", "Evento Mysterious", "Evento Mysterious", "Evento Mysterious", "Evento Cute", "Evento Cute", "Evento Cute", "Evento Cute", "Evento Cute", "Evento Cute", "Evento Pure", "Evento Pure", "Evento Pure", "Evento Pure", "Evento Pure", "Evento Pure", "Evento Happy", "Evento Happy", "Evento Happy", "Evento Happy", "Evento Happy", "Evento Happy"]
quantidade = [4,5,4,3,4,6,3,3,3,3,3,10,2,3,4,3,3,8,4,3,2,2,3,10,4,2,4,5,3,7]
df = pd.DataFrame(dict(grupos=grupos,tipos=tipos,quantidade=quantidade))
df["all"] = "all" #garante um único nó raiz
fig = px.treemap(df,path=[tipos,grupos],values=quantidade)
fig.show()