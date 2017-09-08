
# coding: utf-8

# In[23]:


import ipywidgets as widgets
from IPython.display import display
from ipywidgets import Layout, Button, Box, Label

items_layout = Layout(flex='1 1 auto',
                      width='auto')     # override the default width of the button to 'auto' to let the button grow

box_layout = Layout(display='flex',
                    flex_flow='column',
                    align_items='stretch',
                    border='solid',
                    width='33%')

che1=widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)
che2=widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)
che3=widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)
che4=widgets.Checkbox(
    value=False,
    description='Check me',
    disabled=False
)

words = ['correct', 'horse', 'battery', 'staple']
items = [ che1,che2,che3,che4,che2,che3,che4,che2,che3,che4,che2,che3,che4]
items1 = [ che1,che2]


form_item_layout = Layout(
    display='flex',
    flex_flow='row',
    justify_content='space-between'
)

form_items = [
    Box([Label(value='Age of the captain'), che1], layout=form_item_layout),
    Box([Label(value='Egg style'),che2], layout=form_item_layout),
    Box([Label(value='Ship size'),che3], layout=form_item_layout),
    Box([Label(value='Information'),che4], layout=form_item_layout)
]



left_box = widgets.VBox(form_items)
right_box = widgets.VBox(form_items)


caja=Layout(
    border='solid 2px',
    width='100%'
)

a=widgets.HBox([left_box, right_box], layout=caja)

children = [ a, Box(children=items1)]
tab = widgets.Tab(layout=caja)
tab.children = children
tab.set_title(0,'Operaciones Unitarias')
tab.set_title(1, 'Vista')
display(tab)



# In[ ]:




