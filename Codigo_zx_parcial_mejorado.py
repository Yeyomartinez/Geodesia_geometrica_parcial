import math

def elipsoides():
    print("1) Internacional")
    print("2) GRS - 84")
    Seleccionar_variable = int(input("Seleccione el elipsoide a utilizar: "))
    
    if Seleccionar_variable == 1:
        a = 6378388
        e = 0.006722670022
    elif Seleccionar_variable == 2:
        a = 6378137 
        e = 0.00669438002290  
    else:
        print("OPCIÓN NO VÁLIDA")
    
    return a, e 

def nortesur():
    Seleccionar_norte_sur = int(input("Seleccione (1) si su latitud es norte, o a su vez seleccione (2) si su latitud es sur: "))
    valor_phi_grados = float(input("Ingrese el valor para la transformación en grados: "))
    valor_phi_minutos = float(input("Ingrese el valor para la transformación en minutos: "))
    valor_phi_segundos = float(input("Ingrese el valor para la transformación en segundos: "))
    
    Calculo_de_phi_decimal = valor_phi_grados + valor_phi_minutos/60 + valor_phi_segundos/3600
    
    if Seleccionar_norte_sur == 1:
        resultado_ns = Calculo_de_phi_decimal * 1
    elif Seleccionar_norte_sur == 2:
        resultado_ns = Calculo_de_phi_decimal * -1
    else:
        print("NO VALIDO")
        
    resultado_ns_rad = math.radians (resultado_ns)
        
    return (resultado_ns_rad)

def calculo_de_transformacion(a, e, resultado_ns_rad):
    calculo_de_w = math.degrees(math.atan((math.tan(resultado_ns_rad) * (1 - e))))
    ang_w_rad = math.radians(calculo_de_w)
    
    grados_0 = abs(int(calculo_de_w))
    grados_0_sin_abs = int(calculo_de_w)
    minutos_dec_0 = (calculo_de_w - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
    if calculo_de_w >= 0:
        print("Su valor de ω:", visualizacion_phi, "N")
    elif calculo_de_w <= 0:
        print("Su valor de ω:", visualizacion_phi, "S")
    else:
        print("Su valor de ω:", visualizacion_phi, "ECUADOR")
        
    return ang_w_rad

def calculo_de_phi_en_tetha(a, e, resultado_ns_rad):
    calculo_de_tetha = math.degrees(math.atan(math.tan(resultado_ns_rad) * math.sqrt(1 - e)))
    ang_tetha_rad = math.radians(calculo_de_tetha)
    
    grados_0 = abs(int(calculo_de_tetha))
    grados_0_sin_abs = int(calculo_de_tetha)
    minutos_dec_0 = (calculo_de_tetha - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
    if calculo_de_tetha >= 0:
        print("Su valor de θ:", visualizacion_phi, "N")
    elif calculo_de_tetha <= 0:
        print("Su valor de θ:", visualizacion_phi, "S")
    else:
        print("Su valor de θ:", visualizacion_phi, "ECUADOR")
        
    return ang_tetha_rad
def calculo_de_coodernadas_xz_phi(a, e, resultado_ns_rad):
    N = a / math.sqrt(1 - e * (math.sin(resultado_ns_rad) ** 2))
    x = N * math.cos(resultado_ns_rad)
    z = N * (1 - e) * math.sin(resultado_ns_rad)
    
    print("Los valores de x en φ= ", x)
    print("Los valores de z en φ= ", z)
    
    
    return x, z

def calculo_de_coordendas_xz_w(a, e, ang_w_rad):
    RgP = a * math.sqrt(1 - e)
    w = math.sqrt(1 - e * (math.cos(ang_w_rad) ** 2))
    Rg = RgP / w
    x_w = Rg * math.cos(ang_w_rad)
    z_w = Rg * math.sin(ang_w_rad)
    
    print("Los valores de x en ω= ",x_w)
    print("Los valores de z en ω= ",z_w)
    
    return x_w, z_w     

def calculo_de_coordendas_xz_0(a, e, ang_tetha_rad):
    b = a * math.sqrt(1 - e)
    x_0 = a * math.cos(ang_tetha_rad)
    z_0 = b * math.sin(ang_tetha_rad)
    
    print("Los valores de x en θ= ", x_0)
    print("Los valores de z en θ= ", z_0)
    
    return x_0, z_0

a, e = elipsoides()
resultado_ns_rad = nortesur()
ang_w_rad = calculo_de_transformacion(a, e, resultado_ns_rad)
ang_tetha_rad = calculo_de_phi_en_tetha(a, e, resultado_ns_rad)
calculo_de_coodernadas_xz_phi(a, e, resultado_ns_rad)
calculo_de_coordendas_xz_w(a, e, ang_w_rad)
calculo_de_coordendas_xz_0(a, e, ang_tetha_rad)
