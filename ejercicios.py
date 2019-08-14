#!/usr/bin/env python
# coding: utf-8

# # EJERCICIOS DEL LIBRO
# 
# 
# De acuerdo al libro Qsdfsf se realizaran estos ejercicios de programación con el lenguaje python.
# 
# 1.1 Programa que sume dos numero complejos. funcion suma_C
# 2.2
# 
# 
# 
# 

# ### 1.1 SUMA DE COMPLEJOS

# Se define los dos numeros complejos en sus respectivos vectores, determinando que la posicion 0 sea la parte real y la posicion 1 la parte imaginaria. Y por definicion se sabe que la suma de complejos es la suma de las partes reales y las partes imaginarias.
# Para mostrar el programa que realice la suma de complejos se toma como ejemplo los numeros 3 + 5i y 2i.

# In[3]:


def suma_C(Cm1,Cm2):
    sum_com = [(Cm1[0]+Cm2[0]),(Cm1[1]+Cm2[1])]
    real = Cm1[0]+Cm2[0]
    img = Cm1[1]+Cm2[1]
    print("----------SUMA DE DOS NÚMEROS-------")
    #Numero 1
    if Cm1[0]==0:
        print("Numero complejo 1:",str(Cm1[1])+"i")
    elif Cm1[1]==0:
        print("Numero complejo 1:",Cm1[0])
    elif Cm1[1]<0:
        print("Numero complejo 1:",Cm1[0],str(Cm1[1])+"i")
    else:
        print("Numero complejo 1:",Cm1[0],"+"+str(Cm1[1])+"i")

    #Numero 2
    if Cm2[0]==0:
        print("Numero complejo 2:",str(Cm2[1])+"i")
    elif Cm2[1]==0:
        print("Numero complejo 2:",Cm2[0])
    elif Cm2[1]<0:
        print("Numero complejo 2:",Cm2[0],str(Cm2[1])+"i")
    else:
        print("Numero complejo 2:",Cm2[0],"+"+str(Cm2[1])+"i")
    
        
    #suma de numeros complejos
    if sum_com[0]==0:
        print("El resultado es:",str(sum_com[1])+"i")
    elif sum_com[1]==0:
        print("El resultado es:",sum_com[0])
    elif sum_com[1]<0:
        print("El resultado es:",sum_com[0],str(sum_com[1])+"i")
    else:
        print("El resultado es:",sum_com[0],"+"+str(sum_com[1])+"i")
    
     #Si alguna otra función necesita multiplicar dos numeros se devuelve el resultado
    return sum_com


# In[4]:


suma_C([3,5],[0,2])


# ### 1.2 Multiplicación

# In[24]:


def Mul_C(C1,C2):
    Real = (C1[0]*C2[0])-(C1[1]*C2[1])
    imag = (C1[0]*C2[1])+(C2[0]*C1[1])
    Resul = [Real,imag]
    print("----------MULTIPLICACIÓN DE DOS NÚMEROS-------")
    #Numero 1
    if C1[0]==0:
        print("Numero complejo 1:",str(C1[1])+"i")
    elif C1[1]==0:
        print("Numero complejo 1:",C1[0])
    elif C1[1]<0:
        print("Numero complejo 1:",C1[0],str(C1[1])+"i")
    else:
        print("Numero complejo 1:",C1[0],"+"+str(C1[1])+"i")

    #Numero 2
    if C2[0]==0:
        print("Numero complejo 2:",str(C2[1])+"i")
    elif C2[1]==0:
        print("Numero complejo 2:",C2[0])
    elif C2[1]<0:
        print("Numero complejo 2:",C2[0],str(C2[1])+"i")
    else:
        print("Numero complejo 2:",C2[0],"+"+str(C2[1])+"i")
    
        
    #Multiplicación de numeros complejos
    if Resul[0]==0:
        print("El resultado es:",str(Resul[1])+"i")
    elif Resul[1]==0:
        print("El resultado:",Resul[0])
    elif Resul[1]<0:
        print("El resultado:",Resul[0],str(Resul[1])+"i")
    else:
        print("El resultado:",Resul[0],"+"+str(Resul[1])+"i")
    
    #Si alguna otra función necesita multiplicar dos numeros se devuelve el resultado
    return Resul


# In[25]:


Mul_C([-5,4],[1,3])


# ### 1.3 CONJUGADO DE UN NUMERO COMPLEJO

# In[28]:


def Conju_C(C1):
    print("----------CONJUGADO DE UN NÚMERO-------")
    #Numero complejo
    if C1[0]==0:
        print("Numero complejo 1:",str(C1[1])+"i")
    elif C1[1]==0:
        print("Numero complejo 1:",C1[0])
    elif C1[1]<0:
        print("Numero complejo 1:",C1[0],str(C1[1])+"i")
    else:
        print("Numero complejo 1:",C1[0],"+"+str(C1[1])+"i")
    
    #Conjugado
    C1[1] = -C1[1]
    Resul = C1
    if C1[0]==0:
        print("El conjugado del numero complejo:",str(C1[1])+"i")
    elif C1[1]==0:
        print("El conjugado del numero complejo:",C1[0])
    elif C1[1]<0:
        print("El conjugado del numero complejo:",C1[0],str(C1[1])+"i")
    else:
        print("El conjugado del numero complejo:",C1[0],"+"+str(C1[1])+"i")
        
    #Si alguna otra función necesita multiplicar dos numeros se devuelve el resultado
    return Resul


# In[29]:


Conju_C([-5,4])


# ### 1.4 DIVISIÓN NÚMEROS IMAGINARIOS

# In[32]:


def Div_C(C1, C2):
    Conjugado = Conju_C(C2)
    Numerador = Mul_C(C1, Conjugado)
    Denominador = Mul_C(C2, Conjugado)
    
    Resul = [Numerador,Denominador]
    
    #División de numeros complejos
    if Resul[0]==0:
        print("El resultado es:",str(Resul[1])+"i")
    elif Resul[1]==0:
        print("El resultado:",Resul[0])
    elif Resul[1]<0:
        print("El resultado:",Resul[0],str(Resul[1])+"i")
    else:
        print("El resultado:",Resul[0],"+"+str(Resul[1])+"i")
    


# In[33]:


Div_C([-5,4],[1,3])


# In[ ]:




