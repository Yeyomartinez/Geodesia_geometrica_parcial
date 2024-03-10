import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def elipsoides():
    print("1) Internacional")
    print("2) GRS - 84")
    Seleccionar_variable = int(input("Seleccione el elipsoide a utilizar: "))
    
    if Seleccionar_variable == 1:
        a = float(input("Ingrese el valor de a para el elipsoide Internacional: "))
        e = float(input("Ingrese el valor de e para el elipsoide Internacional: "))
    elif Seleccionar_variable == 2:
        a = float(input("Ingrese el valor de a para el elipsoide GRS - 84: "))
        e = float(input("Ingrese el valor de e para el elipsoide GRS - 84: "))
    else:
        print("OPCIÓN NO VÁLIDA")
        return None
    
    return a, e 

def pedir_xyz(a, e):
    print("ADVERTENCIA: Una vez los valores sean inscritos no hay retroceso")
    while True:
        x_entrada = float(input("Ingrese el valor de X= "))
        y_entrada = float(input("Ingrese el valor de y= "))
        z_entrada = float(input("Ingrese el valor de Z= "))
        
        # Verificar si los valores están dentro del elipsoide
        r = math.sqrt(x_entrada**2 + y_entrada**2 + z_entrada**2)
        if r <= a:
            break
        else:
            print("Los valores están fuera del elipsoide. Ingréselos nuevamente.")

    return x_entrada, y_entrada, z_entrada

def calculo_1ra_iteracion(a, e, x_entrada, y_entrada, z_entrada):
    Calculo_phi_1_a = 1 / (1 - e)
    Calculo_phi_1_b = z_entrada / math.sqrt(x_entrada**2 + y_entrada**2)
    Calculo_phi_1 = math.degrees(math.atan(Calculo_phi_1_a * Calculo_phi_1_b))
    Calculo_de_n_1 = a / math.sqrt(1 - e * (math.sin(math.radians(Calculo_phi_1))**2))
    Calculo_de_h_1 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(Calculo_phi_1))) - Calculo_de_n_1
    return Calculo_phi_1, Calculo_de_n_1, Calculo_de_h_1

def calculo_lambda(x_entrada, y_entrada):
    Calculo_lambda_final = math.degrees(math.atan(y_entrada / x_entrada))
    grados_0 = abs(int(Calculo_lambda_final))
    grados_0_sin_abs = int(Calculo_lambda_final)
    minutos_dec_0 = (Calculo_lambda_final - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_lambda =  f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
    if Calculo_lambda_final >= 0:
        print("Su valor de λ: ", visualizacion_lambda, "E")
    elif Calculo_lambda_final <= 0:
        print("Su valor de λ: ", visualizacion_lambda, "W")
    else:
        print("Su valor de λ: ", visualizacion_lambda, "MERIDIANO CENTRAL")
    
    return Calculo_lambda_final, visualizacion_lambda

def calculo_2da_iteracion(calculo_phi_1, Calculo_de_n_1, a, e, x_entrada, y_entrada, z_entrada):
    calculo_phi_2_a = z_entrada + e * Calculo_de_n_1 * math.sin(math.radians(calculo_phi_1))
    calculo_phi_2_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_2 = math.degrees(math.atan(calculo_phi_2_a / calculo_phi_2_b))
    Calculo_de_n_2 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_2))**2))
    Calculo_de_h_2 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_2))) - Calculo_de_n_2
    return calculo_phi_2, Calculo_de_n_2, Calculo_de_h_2

def calculo_3ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_2, Calculo_de_n_2):
    calculo_phi_3_a = z_entrada + e * Calculo_de_n_2 * math.sin(math.radians(calculo_phi_2))
    calculo_phi_3_b = math.sqrt(x_entrada**2 + y_entrada**2)
    calculo_phi_3 = math.degrees(math.atan(calculo_phi_3_a / calculo_phi_3_b))
    Calculo_de_n_3 = a / math.sqrt(1 - e * (math.sin(math.radians(calculo_phi_2))**2))
    Calculo_de_h_3 = (math.sqrt(x_entrada**2 + y_entrada**2)) / (math.cos(math.radians(calculo_phi_2))) - Calculo_de_n_2
    return calculo_phi_3, Calculo_de_n_3, Calculo_de_h_3

def imprimir_resultados(calculo_phi_3, Calculo_de_h_3):
    grados_0 = abs(int(calculo_phi_3))
    grados_0_sin_abs = int(calculo_phi_3)
    minutos_dec_0 = (calculo_phi_3 - grados_0_sin_abs) * 60
    minutos_0 = abs(int(minutos_dec_0))
    minutos_0_sin_abs = int(minutos_dec_0)
    segundos_0 = abs((minutos_dec_0 - minutos_0_sin_abs) * 60)
    visualizacion_phi = f"{grados_0}° {minutos_0}' {segundos_0:.5f}\""
    
    if calculo_phi_3 >= 0:
        print("Su valor de φ:", visualizacion_phi, "N")
    elif calculo_phi_3 <= 0:
        print("Su valor de φ:", visualizacion_phi, "S")
    else:
        print("Su valor de φ:", visualizacion_phi, "ECUADOR")
    
    print("Su valor de H (altura sobre el nivel del mar):", Calculo_de_h_3)
    
    return visualizacion_phi

def graficar_coordenadas(longitudes, latitudes, alturas, a, e, x_entrada, y_entrada, z_entrada, visualizacion_phi):
    phi = np.linspace(-np.pi/2, np.pi/2, 100)
    theta = np.linspace(0, 2*np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)
    r = a / np.sqrt(1 - e**2 * np.sin(phi)**2)

    x = r * np.cos(phi) * np.cos(theta)
    y = r * np.cos(phi) * np.sin(theta)
    z = r * np.sin(phi)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z, color='c', alpha=0.3, linewidth=0, antialiased=False)
    ax.scatter(longitudes, latitudes, alturas, c='r', marker='o')

    # Añadir vector desde el centro del elipsoide hasta el punto
    ax.quiver(0, 0, 0, x_entrada, y_entrada, z_entrada, color='b', label=f'Vector desde el centro a φ: {visualizacion_phi}')

    ax.set_xlabel('Longitud')
    ax.set_ylabel('Latitud')
    ax.set_zlabel('Altura sobre el nivel del mar')
    ax.legend()

    plt.show()

# Resto del código...

a, e = elipsoides()
x_entrada, y_entrada, z_entrada = pedir_xyz(a, e)
calculo_phi_1, Calculo_de_n_1, Calculo_de_h_1 = calculo_1ra_iteracion(a, e, x_entrada, y_entrada, z_entrada)
Calculo_lambda_result, visualizacion_phi = calculo_lambda(x_entrada, y_entrada)
calculo_phi_2, Calculo_de_n_2, Calculo_de_h_2 = calculo_2da_iteracion(calculo_phi_1, Calculo_de_n_1, a, e, x_entrada, y_entrada, z_entrada)
calculo_phi_3, Calculo_de_n_3, Calculo_de_h_3 = calculo_3ra_iteracion(a, e, x_entrada, y_entrada, z_entrada, calculo_phi_2, Calculo_de_n_2)
imprimir_resultados(calculo_phi_3, Calculo_de_h_3)

# Llamar a la función para graficar coordenadas
graficar_coordenadas([Calculo_lambda_result], [calculo_phi_3], [Calculo_de_h_3], a, e, x_entrada, y_entrada, z_entrada, visualizacion_phi)
