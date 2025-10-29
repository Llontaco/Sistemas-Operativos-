import pygame
import time
import random
import math

ESCENARIOS = {
    "A": [
        {"id": 1, "llegada": 0, "duracion": 72, "inicio": None, "fin": None},
        {"id": 2, "llegada": 0, "duracion": 15, "inicio": None, "fin": None},
        {"id": 3, "llegada": 0, "duracion": 38, "inicio": None, "fin": None},
        {"id": 4, "llegada": 0, "duracion": 5, "inicio": None, "fin": None},
        {"id": 5, "llegada": 0, "duracion": 61, "inicio": None, "fin": None},
        {"id": 6, "llegada": 0, "duracion": 29, "inicio": None, "fin": None},
        {"id": 7, "llegada": 0, "duracion": 47, "inicio": None, "fin": None},
        {"id": 8, "llegada": 0, "duracion": 80, "inicio": None, "fin": None},
        {"id": 9, "llegada": 0, "duracion": 3, "inicio": None, "fin": None},
        {"id": 10, "llegada": 0, "duracion": 55, "inicio": None, "fin": None}
    ],
    "B": [
        {"id": 1, "llegada": 0, "duracion": 13, "inicio": None, "fin": None},
        {"id": 2, "llegada": 1, "duracion": 1, "inicio": None, "fin": None},
        {"id": 3, "llegada": 4, "duracion": 1, "inicio": None, "fin": None},
        {"id": 4, "llegada": 2, "duracion": 2, "inicio": None, "fin": None},
        {"id": 5, "llegada": 7, "duracion": 2, "inicio": None, "fin": None},
        {"id": 6, "llegada": 8, "duracion": 2, "inicio": None, "fin": None},
        {"id": 7, "llegada": 2, "duracion": 3, "inicio": None, "fin": None},
        {"id": 8, "llegada": 4, "duracion": 3, "inicio": None, "fin": None},
        {"id": 9, "llegada": 4, "duracion": 4, "inicio": None, "fin": None},
        {"id": 10, "llegada": 7, "duracion": 4, "inicio": None, "fin": None},
        {"id": 11, "llegada": 1, "duracion": 5, "inicio": None, "fin": None},
        {"id": 12, "llegada": 8, "duracion": 5, "inicio": None, "fin": None},
        {"id": 13, "llegada": 4, "duracion": 8, "inicio": None, "fin": None},
        {"id": 14, "llegada": 6, "duracion": 10, "inicio": None, "fin": None},
        {"id": 15, "llegada": 7, "duracion": 11, "inicio": None, "fin": None},
        {"id": 16, "llegada": 2, "duracion": 13, "inicio": None, "fin": None},
        {"id": 17, "llegada": 3, "duracion": 14, "inicio": None, "fin": None},
        {"id": 18, "llegada": 5, "duracion": 14, "inicio": None, "fin": None},
        {"id": 19, "llegada": 7, "duracion": 14, "inicio": None, "fin": None},
        {"id": 20, "llegada": 7, "duracion": 14, "inicio": None, "fin": None}
    ],
    "C_BAJA": [
        {"id": 1, "llegada": 1, "duracion": 9, "inicio": None, "fin": None},
        {"id": 2, "llegada": 8, "duracion": 2, "inicio": None, "fin": None},
        {"id": 3, "llegada": 11, "duracion": 3, "inicio": None, "fin": None},
        {"id": 4, "llegada": 4, "duracion": 10, "inicio": None, "fin": None},
        {"id": 5, "llegada": 20, "duracion": 1, "inicio": None, "fin": None},
        {"id": 6, "llegada": 17, "duracion": 4, "inicio": None, "fin": None},
        {"id": 7, "llegada": 16, "duracion": 9, "inicio": None, "fin": None},
        {"id": 8, "llegada": 33, "duracion": 4, "inicio": None, "fin": None},
        {"id": 9, "llegada": 42, "duracion": 1, "inicio": None, "fin": None},
        {"id": 10, "llegada": 43, "duracion": 4, "inicio": None, "fin": None},
        {"id": 11, "llegada": 47, "duracion": 1, "inicio": None, "fin": None},
        {"id": 12, "llegada": 49, "duracion": 1, "inicio": None, "fin": None},
        {"id": 13, "llegada": 33, "duracion": 8, "inicio": None, "fin": None},
        {"id": 14, "llegada": 36, "duracion": 9, "inicio": None, "fin": None},
        {"id": 15, "llegada": 23, "duracion": 10, "inicio": None, "fin": None},
        {"id": 16, "llegada": 37, "duracion": 10, "inicio": None, "fin": None},
        {"id": 17, "llegada": 8, "duracion": 11, "inicio": None, "fin": None},
        {"id": 18, "llegada": 37, "duracion": 11, "inicio": None, "fin": None},
        {"id": 19, "llegada": 8, "duracion": 12, "inicio": None, "fin": None},
        {"id": 20, "llegada": 37, "duracion": 13, "inicio": None, "fin": None}
    ],
    "C_ALTA": [
        {"id": 11, "llegada": 0, "duracion": 1, "inicio": None, "fin": None},
        {"id": 10, "llegada": 1, "duracion": 1, "inicio": None, "fin": None},
        {"id": 4, "llegada": 0, "duracion": 2, "inicio": None, "fin": None},
        {"id": 5, "llegada": 0, "duracion": 3, "inicio": None, "fin": None},
        {"id": 14, "llegada": 1, "duracion": 3, "inicio": None, "fin": None},
        {"id": 13, "llegada": 2, "duracion": 3, "inicio": None, "fin": None},
        {"id": 8, "llegada": 3, "duracion": 3, "inicio": None, "fin": None},
        {"id": 12, "llegada": 3, "duracion": 3, "inicio": None, "fin": None},
        {"id": 16, "llegada": 1, "duracion": 4, "inicio": None, "fin": None},
        {"id": 9, "llegada": 1, "duracion": 5, "inicio": None, "fin": None},
        {"id": 17, "llegada": 1, "duracion": 5, "inicio": None, "fin": None},
        {"id": 18, "llegada": 1, "duracion": 5, "inicio": None, "fin": None},
        {"id": 19, "llegada": 3, "duracion": 5, "inicio": None, "fin": None},
        {"id": 2, "llegada": 0, "duracion": 8, "inicio": None, "fin": None},
        {"id": 1, "llegada": 1, "duracion": 9, "inicio": None, "fin": None},
        {"id": 15, "llegada": 3, "duracion": 11, "inicio": None, "fin": None},
        {"id": 3, "llegada": 3, "duracion": 13, "inicio": None, "fin": None},
        {"id": 6, "llegada": 3, "duracion": 13, "inicio": None, "fin": None},
        {"id": 7, "llegada": 1, "duracion": 14, "inicio": None, "fin": None},
        {"id": 20, "llegada": 2, "duracion": 14, "inicio": None, "fin": None}
    ]
}

def generar_procesos(n=10, llegada_max=5, duracion_max=8):
    procesos = []
    for i in range(1, n+1):
        llegada = random.randint(0, llegada_max)
        duracion = random.randint(1, duracion_max)
        procesos.append({"id": i, "llegada": llegada, "duracion": duracion, "inicio": None, "fin": None})
    return procesos

def cargar_escenario(clave_escenario):
    import copy
    procesos = copy.deepcopy(ESCENARIOS[clave_escenario])
    pendientes = sorted(procesos, key=lambda x: x["llegada"])
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    
    print(f"\n--- Escenario {clave_escenario} cargado ---")
    for p in procesos:
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}")
    
    return procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global

def reset_simulacion(escenario=None):
    if escenario:
        return cargar_escenario(escenario)
    
    procesos = generar_procesos()
    pendientes = sorted(procesos, key=lambda x: x["llegada"])
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    
    print("\n--- Nuevos procesos generados ---")
    for p in procesos:
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}")
    
    return procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global

def calcular_metricas(procesos):
    n = len(procesos)
    retorno_total = 0
    espera_total = 0
    respuesta_total = 0
    tiempos_espera = []

    for p in procesos:
        retorno = p['fin'] - p['llegada']
        espera = p['inicio'] - p['llegada']
        respuesta = p['inicio'] - p['llegada']
        retorno_total += retorno
        espera_total += espera
        respuesta_total += respuesta
        tiempos_espera.append(espera)

    promedio_retorno = retorno_total / n
    promedio_espera = espera_total / n
    promedio_respuesta = respuesta_total / n

    tiempo_total = max(p['fin'] for p in procesos) - min(p['llegada'] for p in procesos)
    throughput = n / tiempo_total if tiempo_total > 0 else 0

    tiempos_retorno = [p['fin'] - p['llegada'] for p in procesos]
    min_retorno = min(tiempos_retorno)
    max_retorno = max(tiempos_retorno)
    fairness = min_retorno / max_retorno if max_retorno > 0 else 0

    return promedio_retorno, promedio_espera, promedio_respuesta, throughput, fairness

def dibujar_rectangulo_sombra(surface, color, rect, radio=8, sombra_offset=4):
    sombra_rect = rect.copy()
    sombra_rect.x += sombra_offset
    sombra_rect.y += sombra_offset
    pygame.draw.rect(surface, (0, 0, 0, 50), sombra_rect, border_radius=radio)
    pygame.draw.rect(surface, color, rect, border_radius=radio)
    brillo_color = tuple(min(c + 40, 255) for c in color[:3])
    brillo_rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height // 3)
    s = pygame.Surface((brillo_rect.width, brillo_rect.height), pygame.SRCALPHA)
    pygame.draw.rect(s, (*brillo_color, 60), s.get_rect(), border_radius=radio)
    surface.blit(s, brillo_rect)

def simular_sjf_visual():
    pygame.init()
    ancho_max = 1700
    alto = 950
    ventana = pygame.display.set_mode((ancho_max, alto))
    pygame.display.set_caption("Algoritmo SJF")
    
    fuente = pygame.font.SysFont("Segoe UI", 18, bold=False)
    fuente_bold = pygame.font.SysFont("Segoe UI", 18, bold=True)
    fuente_titulo = pygame.font.SysFont("Segoe UI", 24, bold=True)
    fuente_tiempo = pygame.font.SysFont("Segoe UI", 32, bold=True)
    fuente_boton = pygame.font.SysFont("Segoe UI", 16, bold=True)
    fuente_pequena = pygame.font.SysFont("Segoe UI", 14, bold=False)
    
    colores = [
        (255, 107, 107), (78, 205, 196), (255, 195, 113), (162, 155, 254),
        (255, 234, 167), (108, 92, 231), (255, 159, 243), (87, 242, 135),
        (255, 121, 121), (95, 218, 210), (255, 209, 127), (176, 169, 255),
        (255, 241, 181), (122, 106, 245), (255, 173, 246), (101, 255, 149),
        (255, 135, 135), (112, 230, 223), (255, 223, 141), (190, 183, 255)
    ]
    
    fondo_top = (26, 32, 44)
    fondo_bottom = (45, 55, 72)
    color_panel = (30, 41, 59)
    color_texto = (226, 232, 240)
    color_texto_secundario = (148, 163, 184)
    color_acento = (99, 102, 241)
    color_acento_hover = (79, 70, 229)
    color_linea_tiempo = (251, 146, 60)
    color_error = (239, 68, 68)
    color_exito = (34, 197, 94)
    
    reloj = pygame.time.Clock()
    velocidad = 0.01

    boton_rect = pygame.Rect(ancho_max - 190, 20, 170, 45)
    boton_rect = pygame.Rect(ancho_max - 190, 20, 170, 45)
    
    boton_width = 160
    boton_height = 50
    spacing = 20
    total_width = 5 * boton_width + 4 * spacing
    start_x = (ancho_max - total_width) // 2
    botones_y = alto - 100
    
    botones_escenarios = {
        "A": pygame.Rect(start_x, botones_y, boton_width, boton_height),
        "B": pygame.Rect(start_x + boton_width + spacing, botones_y, boton_width, boton_height),
        "C_BAJA": pygame.Rect(start_x + 2 * (boton_width + spacing), botones_y, boton_width, boton_height),
        "C_ALTA": pygame.Rect(start_x + 3 * (boton_width + spacing), botones_y, boton_width, boton_height),
        "PERSONALIZADO": pygame.Rect(start_x + 4 * (boton_width + spacing), botones_y, boton_width, boton_height)
    }
    
    boton_regresar = pygame.Rect(ancho_max - 230, alto - 100, 210, 50)
    
    nombres_botones = {
        "A": "Escenario A",
        "B": "Escenario B",
        "C_BAJA": "Escenario C (Baja)",
        "C_ALTA": "Escenario C (Alta)",
        "PERSONALIZADO": "Personalizado"
    }

    # Estado para el modo personalizado
    modo_personalizado = False
    procesos_personalizados = []
    campo_activo = None  # (indice_proceso, "llegada" o "duracion")
    texto_input = ""
    mensaje_error = ""
    tiempo_mensaje = 0
    
    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion()
    corriendo = True
    simulacion_terminada = False
    proceso_seleccionado = None
    tiempo_seleccion = 0

    while corriendo:
        # Si estamos en modo personalizado, mostrar la pantalla de configuración
        if modo_personalizado:
            for y in range(alto):
                factor = y / alto
                r = int(fondo_top[0] + (fondo_bottom[0] - fondo_top[0]) * factor)
                g = int(fondo_top[1] + (fondo_bottom[1] - fondo_top[1]) * factor)
                b = int(fondo_top[2] + (fondo_bottom[2] - fondo_top[2]) * factor)
                pygame.draw.line(ventana, (r, g, b), (0, y), (ancho_max, y))
            
            # Panel principal
            panel_w = 1200
            panel_h = 700
            panel_x = (ancho_max - panel_w) // 2
            panel_y = (alto - panel_h) // 2
            
            s_panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
            pygame.draw.rect(s_panel, (*color_panel, 250), s_panel.get_rect(), border_radius=20)
            ventana.blit(s_panel, (panel_x, panel_y))
            
            # Título
            titulo = fuente_titulo.render("Configuración Personalizada", True, color_texto)
            ventana.blit(titulo, (panel_x + 40, panel_y + 30))
            
            # Instrucciones
            instruccion = fuente_pequena.render("Haz clic en los campos para editar. Máx: 10 procesos, llegada ≤ 50, duración ≤ 8", True, color_texto_secundario)
            ventana.blit(instruccion, (panel_x + 40, panel_y + 65))
            
            # Botones de añadir/quitar proceso
            boton_agregar = pygame.Rect(panel_x + 40, panel_y + 100, 150, 40)
            boton_quitar = pygame.Rect(panel_x + 210, panel_y + 100, 150, 40)
            boton_iniciar = pygame.Rect(panel_x + panel_w - 200, panel_y + panel_h - 80, 160, 50)
            boton_cancelar = pygame.Rect(panel_x + 40, panel_y + panel_h - 80, 160, 50)
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Dibujar botón agregar
            color_agregar = color_exito if boton_agregar.collidepoint(mouse_pos) and len(procesos_personalizados) < 10 else (34, 197, 94) if len(procesos_personalizados) < 10 else (100, 100, 100)
            pygame.draw.rect(ventana, color_agregar, boton_agregar, border_radius=8)
            texto_agregar = fuente_boton.render("+ Añadir Proceso", True, (255, 255, 255))
            ventana.blit(texto_agregar, (boton_agregar.x + 15, boton_agregar.y + 12))
            
            # Dibujar botón quitar
            color_quitar = color_error if boton_quitar.collidepoint(mouse_pos) and len(procesos_personalizados) > 0 else (239, 68, 68) if len(procesos_personalizados) > 0 else (100, 100, 100)
            pygame.draw.rect(ventana, color_quitar, boton_quitar, border_radius=8)
            texto_quitar = fuente_boton.render("- Quitar Proceso", True, (255, 255, 255))
            ventana.blit(texto_quitar, (boton_quitar.x + 15, boton_quitar.y + 12))
            
            # Tabla de procesos
            tabla_y = panel_y + 160
            encabezado = ["ID", "Tiempo Llegada", "Duración"]
            col_widths = [100, 200, 200]
            col_x = [panel_x + 40, panel_x + 140, panel_x + 340]
            
            # Encabezados
            for i, texto in enumerate(encabezado):
                txt = fuente_bold.render(texto, True, color_texto)
                ventana.blit(txt, (col_x[i], tabla_y))
            
            # Filas de procesos
            fila_height = 50
            for i in range(10):
                fila_y = tabla_y + 40 + i * fila_height
                
                # Fondo de fila
                if i < len(procesos_personalizados):
                    fondo_fila = pygame.Rect(panel_x + 40, fila_y, 500, fila_height - 5)
                    pygame.draw.rect(ventana, (45, 55, 72), fondo_fila, border_radius=8)
                
                # ID
                txt_id = fuente.render(f"P{i+1}", True, color_texto if i < len(procesos_personalizados) else color_texto_secundario)
                ventana.blit(txt_id, (col_x[0], fila_y + 12))
                
                # Campos de entrada
                if i < len(procesos_personalizados):
                    proceso = procesos_personalizados[i]
                    
                    # Campo llegada
                    rect_llegada = pygame.Rect(col_x[1], fila_y + 5, 180, 35)
                    es_activo_llegada = campo_activo == (i, "llegada")
                    color_campo = color_acento if es_activo_llegada else (60, 70, 90)
                    pygame.draw.rect(ventana, color_campo, rect_llegada, border_radius=6)
                    pygame.draw.rect(ventana, color_acento if es_activo_llegada else color_texto_secundario, rect_llegada, 2, border_radius=6)
                    
                    texto_llegada = texto_input if es_activo_llegada else str(proceso["llegada"])
                    txt_llegada = fuente.render(texto_llegada, True, color_texto)
                    ventana.blit(txt_llegada, (rect_llegada.x + 10, rect_llegada.y + 8))
                    
                    # Campo duración
                    rect_duracion = pygame.Rect(col_x[2], fila_y + 5, 180, 35)
                    es_activo_duracion = campo_activo == (i, "duracion")
                    color_campo = color_acento if es_activo_duracion else (60, 70, 90)
                    pygame.draw.rect(ventana, color_campo, rect_duracion, border_radius=6)
                    pygame.draw.rect(ventana, color_acento if es_activo_duracion else color_texto_secundario, rect_duracion, 2, border_radius=6)
                    
                    texto_duracion = texto_input if es_activo_duracion else str(proceso["duracion"])
                    txt_duracion = fuente.render(texto_duracion, True, color_texto)
                    ventana.blit(txt_duracion, (rect_duracion.x + 10, rect_duracion.y + 8))
            
            # Mensaje de error
            if mensaje_error and time.time() - tiempo_mensaje < 3:
                txt_error = fuente_pequena.render(mensaje_error, True, color_error)
                ventana.blit(txt_error, (panel_x + 40, panel_y + panel_h - 120))
            
            # Botón iniciar simulación
            color_iniciar = color_acento_hover if boton_iniciar.collidepoint(mouse_pos) and len(procesos_personalizados) > 0 else color_acento if len(procesos_personalizados) > 0 else (100, 100, 100)
            pygame.draw.rect(ventana, color_iniciar, boton_iniciar, border_radius=10)
            texto_iniciar = fuente_boton.render("Iniciar", True, (255, 255, 255))
            ventana.blit(texto_iniciar, (boton_iniciar.x + 50, boton_iniciar.y + 15))
            
            # Botón cancelar
            color_cancelar = (150, 150, 150) if boton_cancelar.collidepoint(mouse_pos) else (120, 120, 120)
            pygame.draw.rect(ventana, color_cancelar, boton_cancelar, border_radius=10)
            texto_cancelar = fuente_boton.render("Cancelar", True, (255, 255, 255))
            ventana.blit(texto_cancelar, (boton_cancelar.x + 40, boton_cancelar.y + 15))
            
            pygame.display.flip()
            reloj.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Botón agregar proceso
                    if boton_agregar.collidepoint(event.pos) and len(procesos_personalizados) < 10:
                        procesos_personalizados.append({"id": len(procesos_personalizados) + 1, "llegada": 0, "duracion": 1, "inicio": None, "fin": None})
                    
                    # Botón quitar proceso
                    elif boton_quitar.collidepoint(event.pos) and len(procesos_personalizados) > 0:
                        procesos_personalizados.pop()
                        if campo_activo and campo_activo[0] >= len(procesos_personalizados):
                            campo_activo = None
                            texto_input = ""
                    
                    # Botón iniciar
                    elif boton_iniciar.collidepoint(event.pos) and len(procesos_personalizados) > 0:
                        import copy
                        procesos = copy.deepcopy(procesos_personalizados)
                        pendientes = sorted(procesos, key=lambda x: x["llegada"])
                        terminados = []
                        en_cola = []
                        ejecutando = None
                        tiempo_global = 0
                        simulacion_terminada = False
                        proceso_seleccionado = None
                        modo_personalizado = False
                        campo_activo = None
                        texto_input = ""
                    
                    # Botón cancelar
                    elif boton_cancelar.collidepoint(event.pos):
                        modo_personalizado = False
                        campo_activo = None
                        texto_input = ""
                        procesos_personalizados = []
                    
                    # Campos de entrada
                    else:
                        campo_activo = None
                        for i in range(len(procesos_personalizados)):
                            fila_y = tabla_y + 40 + i * fila_height
                            rect_llegada = pygame.Rect(col_x[1], fila_y + 5, 180, 35)
                            rect_duracion = pygame.Rect(col_x[2], fila_y + 5, 180, 35)
                            
                            if rect_llegada.collidepoint(event.pos):
                                campo_activo = (i, "llegada")
                                texto_input = str(procesos_personalizados[i]["llegada"])
                                break
                            elif rect_duracion.collidepoint(event.pos):
                                campo_activo = (i, "duracion")
                                texto_input = str(procesos_personalizados[i]["duracion"])
                                break
                
                elif event.type == pygame.KEYDOWN and campo_activo:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        # Guardar valor
                        try:
                            valor = int(texto_input) if texto_input else 0
                            idx, campo = campo_activo
                            
                            if campo == "llegada":
                                if 0 <= valor <= 50:
                                    procesos_personalizados[idx][campo] = valor
                                    mensaje_error = ""
                                else:
                                    mensaje_error = "Error: El tiempo de llegada debe estar entre 0 y 50"
                                    tiempo_mensaje = time.time()
                            else:  # duracion
                                if 1 <= valor <= 8:
                                    procesos_personalizados[idx][campo] = valor
                                    mensaje_error = ""
                                else:
                                    mensaje_error = "Error: La duración debe estar entre 1 y 8"
                                    tiempo_mensaje = time.time()
                        except:
                            mensaje_error = "Error: Ingresa un número válido"
                            tiempo_mensaje = time.time()
                        
                        campo_activo = None
                        texto_input = ""
                    
                    elif event.key == pygame.K_BACKSPACE:
                        texto_input = texto_input[:-1]
                    
                    elif event.key == pygame.K_ESCAPE:
                        campo_activo = None
                        texto_input = ""
                    
                    elif event.unicode.isdigit() and len(texto_input) < 3:
                        texto_input += event.unicode
            
            continue
        
        # Renderizado normal de la simulación
        for y in range(alto):
            factor = y / alto
            r = int(fondo_top[0] + (fondo_bottom[0] - fondo_top[0]) * factor)
            g = int(fondo_top[1] + (fondo_bottom[1] - fondo_top[1]) * factor)
            b = int(fondo_top[2] + (fondo_bottom[2] - fondo_top[2]) * factor)
            pygame.draw.line(ventana, (r, g, b), (0, y), (ancho_max, y))

        mouse_pos = pygame.mouse.get_pos()
        
        color_boton = color_acento if not boton_rect.collidepoint(mouse_pos) else color_acento_hover
        sombra_boton = boton_rect.copy()
        sombra_boton.y += 3
        pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_boton, border_radius=8)
        pygame.draw.rect(ventana, color_boton, boton_rect, border_radius=8)
        texto_boton = fuente_bold.render("Reiniciar", True, (255, 255, 255))
        ventana.blit(texto_boton, (boton_rect.x + 45, boton_rect.y + 12))

        for key, rect_boton in botones_escenarios.items():
            hover = rect_boton.collidepoint(mouse_pos)
            color_btn = color_acento_hover if hover else color_acento
            
            sombra = rect_boton.copy()
            sombra.y += 3
            pygame.draw.rect(ventana, (0, 0, 0, 80), sombra, border_radius=10)
            pygame.draw.rect(ventana, color_btn, rect_boton, border_radius=10)
            
            texto = fuente_boton.render(nombres_botones[key], True, (255, 255, 255))
            texto_rect = texto.get_rect(center=rect_boton.center)
            ventana.blit(texto, texto_rect)
        
        # Botón regresar
        color_regresar = color_error if not boton_regresar.collidepoint(mouse_pos) else (209, 58, 58)
        sombra_regresar = boton_regresar.copy()
        sombra_regresar.y += 3
        pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_regresar, border_radius=10)
        pygame.draw.rect(ventana, color_regresar, boton_regresar, border_radius=10)
        texto_regresar = fuente_boton.render("Regresar", True, (255, 255, 255))
        texto_rect_reg = texto_regresar.get_rect(center=boton_regresar.center)
        ventana.blit(texto_regresar, texto_rect_reg)

        if proceso_seleccionado is None:
            nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
            for p in nuevos:
                en_cola.append(p)
                pendientes.remove(p)

            if ejecutando is None and not en_cola and pendientes:
                tiempo_global = pendientes[0]["llegada"]
                nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                for p in nuevos:
                    en_cola.append(p)
                    pendientes.remove(p)

        if ejecutando is None and en_cola and proceso_seleccionado is None:
            proceso_seleccionado = min(en_cola, key=lambda x: x["duracion"])
            tiempo_seleccion = time.time()
            idx_en_cola = en_cola.index(proceso_seleccionado)
            proceso_seleccionado["pos_inicial"] = (250 + idx_en_cola * 130, 20)
        
        if proceso_seleccionado and time.time() - tiempo_seleccion > 0.8:
            ejecutando = proceso_seleccionado
            ejecutando["inicio"] = tiempo_global
            ejecutando["fin"] = tiempo_global + ejecutando["duracion"]
            en_cola.remove(ejecutando)
            proceso_seleccionado = None

        tiempo_max_actual = max(39, tiempo_global)
        for p in terminados + ([ejecutando] if ejecutando else []):
            tiempo_max_actual = max(tiempo_max_actual, p["fin"])
        for p in en_cola:
            tiempo_max_actual = max(tiempo_max_actual, p["llegada"] + p["duracion"])
        tiempo_max_actual = max(39, math.ceil(tiempo_max_actual))
        escala = (ancho_max - 150) / (tiempo_max_actual + 2)

        panel_cola = pygame.Rect(30, 10, ancho_max - 240, 85)
        s_panel = pygame.Surface((panel_cola.width, panel_cola.height), pygame.SRCALPHA)
        pygame.draw.rect(s_panel, (*color_panel, 230), s_panel.get_rect(), border_radius=12)
        ventana.blit(s_panel, panel_cola)
        
        titulo_cola = fuente_titulo.render("Cola de Espera", True, color_texto)
        ventana.blit(titulo_cola, (50, 25))

        for i, p in enumerate(en_cola):
            if proceso_seleccionado and p["id"] == proceso_seleccionado["id"]:
                continue
                
            rect_x = 250 + i * 130
            rect_y = 20
            rect = pygame.Rect(rect_x, rect_y, 110, 65)
            
            color = colores[p["id"] % len(colores)]
            dibujar_rectangulo_sombra(ventana, color, rect, radio=10)
            
            texto_id = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255))
            texto_dur = fuente.render(f"{p['duracion']}s", True, (255, 255, 255))
            ventana.blit(texto_id, (rect_x + 10, rect_y + 8))
            ventana.blit(texto_dur, (rect_x + 10, rect_y + 35))
        
        if proceso_seleccionado:
            progreso = (time.time() - tiempo_seleccion) / 0.8
            progreso = min(progreso, 1.0)
            
            if progreso < 0.5:
                eased = 2 * progreso * progreso
            else:
                eased = 1 - pow(-2 * progreso + 2, 2) / 2
            
            x_inicial, y_inicial = proceso_seleccionado["pos_inicial"]
            fila = proceso_seleccionado['id'] - 1
            y_final = 130 + fila * 55
            x_final = 100 + int(tiempo_global * escala)
            
            x_actual = x_inicial + (x_final - x_inicial) * eased
            arco = -100 * math.sin(eased * math.pi)
            y_actual = y_inicial + (y_final - y_inicial) * eased + arco
            
            escala_rect = 1.0 + 0.3 * math.sin(eased * math.pi)
            ancho_rect = int(110 * escala_rect)
            alto_rect = int(65 * escala_rect if eased < 0.5 else 65 * escala_rect * 0.7)
            
            rect_anim = pygame.Rect(int(x_actual), int(y_actual), ancho_rect, alto_rect)
            color = colores[proceso_seleccionado["id"] % len(colores)]
            
            for offset in [15, 10, 5]:
                s_glow = pygame.Surface((ancho_rect + offset*2, alto_rect + offset*2), pygame.SRCALPHA)
                pygame.draw.rect(s_glow, (*color, int(20 * (1-progreso))), 
                               pygame.Rect(offset, offset, ancho_rect, alto_rect), border_radius=10)
                ventana.blit(s_glow, (int(x_actual) - offset, int(y_actual) - offset))
            
            dibujar_rectangulo_sombra(ventana, color, rect_anim, radio=10, sombra_offset=int(5 * escala_rect))
            
            texto_id = fuente_bold.render(f"P{proceso_seleccionado['id']}", True, (255, 255, 255))
            texto_dur = fuente.render(f"{proceso_seleccionado['duracion']}s", True, (255, 255, 255))
            ventana.blit(texto_id, (int(x_actual) + 10, int(y_actual) + 8))
            ventana.blit(texto_dur, (int(x_actual) + 10, int(y_actual) + 35))
            
            num_particulas = 8
            for j in range(num_particulas):
                angulo = (j / num_particulas) * 2 * math.pi + progreso * 2
                radio_particula = 30 + 20 * progreso
                px = int(x_actual + ancho_rect/2 + math.cos(angulo) * radio_particula)
                py = int(y_actual + alto_rect/2 + math.sin(angulo) * radio_particula)
                tamanho = int(3 * (1 - progreso))
                if tamanho > 0:
                    pygame.draw.circle(ventana, (*color, int(150 * (1-progreso))), (px, py), tamanho)

        for p in terminados + ([ejecutando] if ejecutando else []):
            fila = p['id'] - 1
            y_proceso = 130 + fila * 55
            x_inicio = 100 + int(p["inicio"] * escala)
            
            ancho_rect = int(max(min(tiempo_global, p["fin"]) - p["inicio"], 0) * escala) if p is ejecutando else int((p["fin"] - p["inicio"]) * escala)
            
            color = colores[p["id"] % len(colores)]
            rect = pygame.Rect(x_inicio, y_proceso, ancho_rect, 45)
            
            if p is ejecutando:
                alpha = int(128 + 127 * math.sin(tiempo_global * 3))
                s = pygame.Surface((ancho_rect + 8, 49), pygame.SRCALPHA)
                pygame.draw.rect(s, (*color, alpha), pygame.Rect(4, 2, ancho_rect, 45), border_radius=10)
                ventana.blit(s, (x_inicio - 4, y_proceso - 2))
            
            dibujar_rectangulo_sombra(ventana, color, rect, radio=10, sombra_offset=3)
            
            texto_p = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255))
            ventana.blit(texto_p, (x_inicio + 10, y_proceso + 12))
            
        if ejecutando and tiempo_global >= ejecutando["fin"]:
            terminados.append(ejecutando)
            ejecutando = None

        y_linea = alto - 230
        pygame.draw.line(ventana, color_texto_secundario, (100, y_linea), (ancho_max - 50, y_linea), 3)
        
        for t in range(tiempo_max_actual + 1):
            x = 100 + t * escala
            pygame.draw.line(ventana, color_texto_secundario, (x, y_linea-8), (x, y_linea+8), 2)
            texto_t = fuente.render(str(t), True, color_texto)
            ventana.blit(texto_t, (x-8, y_linea+12))
        
        x_tiempo = 100 + int(tiempo_global * escala)
        for offset in [6, 4, 2]:
            s_glow = pygame.Surface((offset*2, y_linea - 100), pygame.SRCALPHA)
            pygame.draw.line(s_glow, (*color_linea_tiempo, 40), (offset, 0), (offset, y_linea - 100), offset)
            ventana.blit(s_glow, (x_tiempo - offset, 120))
        pygame.draw.line(ventana, color_linea_tiempo, (x_tiempo, 120), (x_tiempo, y_linea), 3)
        
        pygame.draw.circle(ventana, color_linea_tiempo, (x_tiempo, y_linea), 8)
        pygame.draw.circle(ventana, (255, 255, 255), (x_tiempo, y_linea), 4)

        tiempo_texto = f"{int(tiempo_global)}s"
        texto_tiempo = fuente_tiempo.render(tiempo_texto, True, color_linea_tiempo)
        rect_tiempo = texto_tiempo.get_rect(center=(ancho_max//2, 110))
        
        fondo_tiempo = pygame.Rect(rect_tiempo.x - 20, rect_tiempo.y - 10, rect_tiempo.width + 40, rect_tiempo.height + 20)
        s_tiempo = pygame.Surface((fondo_tiempo.width, fondo_tiempo.height), pygame.SRCALPHA)
        pygame.draw.rect(s_tiempo, (*color_panel, 200), s_tiempo.get_rect(), border_radius=15)
        ventana.blit(s_tiempo, fondo_tiempo)
        ventana.blit(texto_tiempo, rect_tiempo)

        if not pendientes and not en_cola and ejecutando is None:
            if not simulacion_terminada:
                simulacion_terminada = True
                retorno, espera, respuesta, throughput, fairness = calcular_metricas(terminados)

            panel_x = 50
            panel_y = alto - 190
            panel_w = 1600
            panel_h = 170
            
            s_panel_metricas = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
            pygame.draw.rect(s_panel_metricas, (*color_panel, 240), s_panel_metricas.get_rect(), border_radius=15)
            ventana.blit(s_panel_metricas, (panel_x, panel_y))
            
            titulo_metricas = fuente_titulo.render("Metricas de Rendimiento", True, color_texto)
            ventana.blit(titulo_metricas, (panel_x + 20, panel_y + 15))
            
            metricas = [
                ("Tiempo Retorno", f"{retorno:.2f}"),
                ("Tiempo Espera", f"{espera:.2f}"),
                ("Tiempo Respuesta", f"{respuesta:.2f}"),
                ("Throughput", f"{throughput:.2f}"),
                ("Fairness", f"{fairness:.2f}")
            ]
            
            card_y = panel_y + 60
            card_w = 290
            card_h = 85
            spacing = 25
            
            for i, (nombre, valor) in enumerate(metricas):
                card_x = panel_x + 30 + i * (card_w + spacing)
                
                card_rect = pygame.Rect(card_x, card_y, card_w, card_h)
                color_card = colores[i % len(colores)]
                
                sombra_card = card_rect.copy()
                sombra_card.y += 4
                s_sombra = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
                pygame.draw.rect(s_sombra, (0, 0, 0, 60), s_sombra.get_rect(), border_radius=12)
                ventana.blit(s_sombra, sombra_card)
                
                s_card = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
                for y in range(card_h):
                    alpha = 200 - int(50 * (y / card_h))
                    pygame.draw.line(s_card, (*color_card, alpha), (0, y), (card_w, y))
                ventana.blit(s_card, card_rect)
                pygame.draw.rect(ventana, color_card, card_rect, 3, border_radius=12)
                
                texto_nombre = fuente.render(nombre, True, (255, 255, 255))
                texto_valor = fuente_bold.render(valor, True, (255, 255, 255))
                
                ventana.blit(texto_nombre, (card_x + 15, card_y + 15))
                ventana.blit(texto_valor, (card_x + 15, card_y + 45))

        pygame.display.flip()
        reloj.tick(60)
        
        if proceso_seleccionado is None:
            tiempo_global += 0.02
            if tiempo_global > tiempo_max_actual:
                tiempo_global = tiempo_max_actual
        time.sleep(0.05 * velocidad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if boton_regresar.collidepoint(event.pos):
                    pygame.quit()
                    import subprocess
                    import sys
                    subprocess.Popen([sys.executable, "menu_principal.py"])
                    return
                
                elif boton_rect.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion()
                    simulacion_terminada = False
                    proceso_seleccionado = None
                
                for clave, rect_boton in botones_escenarios.items():
                    if rect_boton.collidepoint(event.pos):
                        if clave == "PERSONALIZADO":
                            modo_personalizado = True
                            procesos_personalizados = [
                                {"id": 1, "llegada": 0, "duracion": 3, "inicio": None, "fin": None},
                                {"id": 2, "llegada": 0, "duracion": 5, "inicio": None, "fin": None},
                                {"id": 3, "llegada": 2, "duracion": 2, "inicio": None, "fin": None}
                            ]
                            campo_activo = None
                            texto_input = ""
                            mensaje_error = ""
                        else:
                            procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion(clave)
                            simulacion_terminada = False
                            proceso_seleccionado = None

    pygame.quit()

if __name__ == "__main__":
    simular_sjf_visual()