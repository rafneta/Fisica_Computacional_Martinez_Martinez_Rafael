
# coding: utf-8

# In[62]:

######################BITACORA############################
##### #########Días/horas de programación########### #####
##### Día 1: viernes 01/septiembre/2017------7 horas #####
##### Día 2: sabado  02/septiembre/2017------2 horas #####
##### Día 3: domingo  03/septiembre/2017------2 horas #####
##### Día 4: miercoles  06/septiembre/2017------3:30 horas #####
#####----------------------------------------------- #####
#####                                 TOTAL: 14:30 horas #####
##########################################################


get_ipython().magic(u'matplotlib inline')
#import sympy
from sympy import *
#import numpy as np
import matplotlib.pyplot as plt # importamos el submódulo para gráfica
#import matplotlib as mpl
#print mpl.get_cachedir()
#from IPython.html import widgets
#from IPython.html.widgets import interact, interactive, fixed, 
from ipywidgets import interact, interactive, fixed, interactive_output, interact_manual, Layout, Button, Box,FloatText, Textarea, Dropdown, Label, IntSlider

import ipywidgets as widgets
from IPython.display import display, Latex, Math
from sympy.abc import x, y, mu, r, tau
#init_printing(use_latex='mathjax') # impresion en formato latex
init_printing()
x, y, z, t, xx = symbols('x y z t xx')

solve(x**2+1,x)
Abs(z)
arg(z)
z.as_real_imag()
eq = Add(2*x, 3*x, evaluate=False)

#display(Math(r"""%s""" %latex(t**2)))


def Granumcom(real,imag, norma, fase, fp, conj, inverso, inversoa, mz, alpha, 
              raizn, n, potencia, p):
    
    z=real+imag*I
    plt.figure(figsize=(6,6))
    plt.rc('text', usetex=False)
    #plt.rc('font', family='serif')
    #plt.rc('font', family='cm')
    ax = plt.axes()
    
    s="$z=%s$"
    
    if fp==True:
        s="Forma polar: $z=%0.2f$"%Abs(z)+"$e^{%s i}$\n"%latex(round((arg(z)),3))+s
    
    
    if fase==True:
        if z==0:
            s="No es posible encontrar la fase si $z=%s$"
        else:
            if arg(z)<0:
                s=r"Fase: $\measuredangle z=%s$"%latex(round((arg(z)),3))+                " radianes \n o $\measuredangle z=%s$ "% latex(round((arg(z)+pi+pi).evalf(),3))+                " radianes\n "+s
            else:
                s=r"Fase: $\measuredangle z=%s$"%latex(round((arg(z)),3))+" radianes\n"+s

                
    
    if norma==True:
        s="Norma: $|z|=%0.2f$\n"%Abs(z)+s
    
    
    

    ax.plot([0, re(z)],[0,im(z)],'r',lw=3,label=s % latex(z))
    ax.plot(re(z),im(z), "r", marker="*",markersize=10)
    #plt.legend(loc = "best")
    plt.legend(bbox_to_anchor=(1.1, 0.5, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
    ax.grid()
    
    if z==0 and inverso==True:
        inverso=False
        ax.axis([-0.3,1,-0.3,1])
        ax.text(0.05, 0.9, r"No es posible obtener el inverso"  ,                 horizontalalignment='left', rotation=0, fontsize=15, color='red')
        ax.text(0.05, 0.8, r"multiplicativo si $z=0$"  ,                 horizontalalignment='left', rotation=0, fontsize=15, color='red')
        
    if z==0 and p<=0  and potencia==True:
        potencia=False
        ax.axis([-0.3,1,-0.3,1])
        ax.text(0.05, 0.5, r"No es posible obtener la "   ,                 horizontalalignment='left', rotation=0, fontsize=15, color='red')
        ax.text(0.05, 0.4, r"potencia %s de $z$ si $z=0$"%latex(p)  ,                 horizontalalignment='left', rotation=0, fontsize=15, color='red')
        
    if conj==True:
        zc=conjugate(z);
    
    if inverso==True:
        zi=conjugate(z)/(Abs(z)**2);
        zi=round(re(zi), 3)+round(im(zi),3)*I
        
    if inversoa==True:
        zia=z*-1;
        
    
        
                
    #########################
    # Posiciones de los Ejes
    ########################
    
        
    if conj==True:
        ax.plot([0, re(zc)],[0,im(zc)],'b',lw=3,label=r"Conjugado: $\bar{z}=%s$" % latex(zc))
        ax.plot(re(zc),im(zc), "b", marker="*",markersize=10)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
    
    if inverso==True:
        ax.plot([0, re(zi)],[0,im(zi)],'g',lw=3,label=r"Inverso multiplicativo: $z^{-1}=%s$" % latex(zi))
        ax.plot(re(zi),im(zi), "g", marker="*",markersize=10)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
        #(x0, y0, width, height)
        
    if inversoa==True:
        ax.plot([0, re(zia)],[0,im(zia)],'m',lw=3,label=r"Inverso Aditivo: $-z=%s$" % latex(zia))
        ax.plot(re(zia),im(zia), "m", marker="*",markersize=10)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
        #(x0, y0, width, height)
        
    if mz==True:
        ax.plot([0, re(alpha*z)],[0,im(alpha*z)],'k',lw=3,label=r"Multiplo: $\alpha z=%s$" % latex(alpha*z))
        ax.plot(re(alpha*z),im(alpha*z), "k", marker="*",markersize=10)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
        #(x0, y0, width, height)

    
    if raizn==True:
        a=solve(t**n-z,t)
        j=0;
        for i in a:
            ax.plot([0, re(i)],[0,im(i)],'y',lw=3,label=r"raiz $z_{%d}$"%(j+1)+"$=%s$"                    % latex(round(re(a[j]),3)+round(im(a[j]),3)*I))
            ax.plot(re(i),im(i), "y", marker="*",markersize=10)
        #plt.legend(loc = "best")
            plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
            j=j+1
            
    if potencia==True:
        
        zp=expand_complex(z**p).evalf()
        zp=round(re(zp),3)+round(im(zp),3)*I
        ax.plot([0, re(z**p)],[0,im(z**p)],'c',lw=3,label=r"Potencia: $z^p=%s$" % latex(zp))
        ax.plot(re(z**p),im(z**p), "c", marker="*",markersize=10)
        #plt.legend(loc = "best")
        plt.legend(bbox_to_anchor=(1.1, 0.1, 1.1, 1), loc=3,           ncol=1, mode="expand", borderaxespad=0., fontsize=15)
        #(x0, y0, width, height)

    
        
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)


    #xlabel = ax.xaxis.get_label()                               
    #lpos = xlabel.get_position()
    #xlabel.set_position((1.04, lpos[1]))

    #ylabel = ax.yaxis.get_label()
    #lpos = ylabel.get_position()
    #ylabel.set_position((1.04, lpos[1]))

    ax.xaxis.set_label_coords(0.5, -0.05)
    ax.yaxis.set_label_coords(-0.05,0.5)
    #ax.
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlabel(r"$\mathbb{R}e$ ",fontsize=20)
    ax.set_ylabel(r"$\mathbb{I}m$",fontsize=20)
    title=ax.set_title(r"Operaciones unitarias para $z=%s$" %latex(z), y=1.05,        fontsize=16, color="k")
          
    #ax.axis([x0,x1,y0,y1])
    #ax.set_xlim(-1, 1)


    plt.show()



titulo=widgets.HTML(
    value='''<div class="alert alert-warning"><h2>Operaciones unitarias</h2></div>''',
    placeholder='Some HTML')


def nuco(real,imaginario):
    #global w
    style = {'description_width': 'initial'}
    r1=widgets.FloatText(
        value=1.5,
        description=r'\(\mathbb{R}e\text{(z)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )

    ima1=widgets.FloatText(
        value=-2.5,
        description=r'\(\mathbb{I}m\text{(z)}\)',
        step=0.5,
        continuous_update=False,
        style=style
    )


    #b = widgets.FloatSlider()

    #c=widgets.jslink((r1, 'value'), (b, 'value'))

    Norma=widgets.Checkbox(
        value=True,
        description='Norma'
    )

    Fase=widgets.Checkbox(
        value=True,
        description='Fase'
    )

    FP=widgets.Checkbox(
        value=True,
        description='Forma polar'
    )


    conj=widgets.Checkbox(
        value=True,
        description='Conjugado'
    )

    inverm=widgets.Checkbox(
        value=True,
        description='Inverso multiplicativo'
    )


    invera=widgets.Checkbox(
        value=True,
        description='Inverso aditivo'
    )




    rn0=widgets.Checkbox(
        value=True,
        description='Raiz n de z: '
    )


    n=widgets.FloatText(value=2,
            description='valor de n:',
            step=0.5,
            continuous_update=False)

    MZ=widgets.Checkbox(
        value=True,
        description='Multiplo  az: '
    )


    Alpha=widgets.FloatText(value=-0.5,
            description='valor de a:',
            step=0.5,
            continuous_update=False)

    Potencia=widgets.Checkbox(
        value=True,
        description='Potencia p de z: '
    )


    P=widgets.FloatText(value=-0.5,
            description='valor de p:',
            step=0.5,
            continuous_update=False)
    items_layout = Layout(flex='1 1 auto',
                          width='auto')     
    box_layout = Layout(display='flex',
                        flex_flow='column',
                        align_items='stretch',
                        border='solid',
                        width='33%')

    form_item_layout = Layout(
        display='flex',
        flex_flow='row',
        justify_content='space-between'
    )
    
    
    form_items1 = [
        Box([Label(value=' '), r1], layout=form_item_layout),
        Box([Label(value=' '),ima1], layout=form_item_layout)]

    form_items2 = [
        Box([Label(value=''), Norma], layout=form_item_layout),
        Box([Label(value=''),Fase], layout=form_item_layout),
        Box([Label(value=''),FP], layout=form_item_layout)
    ]

    form_items3 = [

        Box([Label(value=''),conj], layout=form_item_layout),
        Box([Label(value=''), inverm], layout=form_item_layout),
        Box([Label(value=''), invera], layout=form_item_layout)
    ]
    
    form_items4 = [
        Box([Label(value=' '), r1], layout=form_item_layout),
        Box([Label(value=' '),ima1], layout=form_item_layout)]


    box1 = widgets.VBox(form_items1)
    box2 = widgets.VBox(form_items2)
    box3 = widgets.VBox(form_items3)


    caja=Layout(
        border='solid 2px',
        width='100%'
    )

    a=widgets.HBox([box1, box2,box3], layout=caja)

    children = [ a, Box(children=form_items4)]
    tab = widgets.Tab(layout=caja)
    tab.children = children
    tab.set_title(0,'Operaciones')
    tab.set_title(1, 'Vista')

    r1.value=real
    ima1.value=imaginario
    
    #display(titulo)
    display(interactive_output(Granumcom,{'real':r1,         'imag':ima1, 'norma':Norma, 'fase':Fase, 'fp':FP, 'conj':conj,          'inverso':inverm, 'inversoa':invera,  'mz':MZ, 'alpha':Alpha,         'raizn':rn0, 'n':n, 'potencia':Potencia, 'p':P}))
    
    
    display(tab)
    

def nucom(real,imaginario):
    r1.value=real
    ima1.value=imaginario
    interact_manual(Granumcom, real=r1,         imag=ima1, norma=Norma, fase=Fase, fp=FP, conj=conj,          inverso=inverm, inversoa=invera,  mz=MZ, alpha=Alpha,         raizn=rn0, n=n, potencia=Potencia, p=P, continuous_update=False);

