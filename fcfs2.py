import pygame
import time
import math

def generar_escenario_A():
    """Escenario A: Todos los procesos llegan al mismo tiempo (alta concurrencia inicial)."""
    procesos = [
        {"id": 1, "llegada": 0, "duracion": 6, "inicio": None, "fin": None, "tipo": None},
        {"id": 2, "llegada": 0, "duracion": 8, "inicio": None, "fin": None, "tipo": None},
        {"id": 3, "llegada": 0, "duracion": 4, "inicio": None, "fin": None, "tipo": None},
        {"id": 4, "llegada": 0, "duracion": 7, "inicio": None, "fin": None, "tipo": None},
        {"id": 5, "llegada": 0, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
        {"id": 6, "llegada": 0, "duracion": 9, "inicio": None, "fin": None, "tipo": None},
        {"id": 7, "llegada": 0, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 8, "llegada": 0, "duracion": 2, "inicio": None, "fin": None, "tipo": None},
        {"id": 9, "llegada": 0, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
        {"id": 10, "llegada": 0, "duracion": 8, "inicio": None, "fin": None, "tipo": None},
    ]
    return procesos


def generar_escenario_B():
    """Escenario B: Llegadas escalonadas (cada proceso llega en momentos distintos)."""
    procesos = [
        {"id": 1, "llegada": 0, "duracion": 6, "inicio": None, "fin": None, "tipo": None},
        {"id": 2, "llegada": 1, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 3, "llegada": 2, "duracion": 2, "inicio": None, "fin": None, "tipo": None},
        {"id": 4, "llegada": 3, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
        {"id": 5, "llegada": 4, "duracion": 7, "inicio": None, "fin": None, "tipo": None},
        {"id": 6, "llegada": 5, "duracion": 4, "inicio": None, "fin": None, "tipo": None},
        {"id": 7, "llegada": 6, "duracion": 8, "inicio": None, "fin": None, "tipo": None},
        {"id": 8, "llegada": 7, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 9, "llegada": 8, "duracion": 2, "inicio": None, "fin": None, "tipo": None},
        {"id": 10, "llegada": 9, "duracion": 9, "inicio": None, "fin": None, "tipo": None},
    ]
    return procesos


def generar_escenario_C_BAJA():
    """Escenario C_BAJA: Baja concurrencia (los procesos llegan muy separados en el tiempo)."""
    procesos = [
        {"id": 1, "llegada": 0, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
        {"id": 2, "llegada": 5, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 3, "llegada": 10, "duracion": 7, "inicio": None, "fin": None, "tipo": None},
        {"id": 4, "llegada": 15, "duracion": 4, "inicio": None, "fin": None, "tipo": None},
        {"id": 5, "llegada": 20, "duracion": 6, "inicio": None, "fin": None, "tipo": None},
        {"id": 6, "llegada": 25, "duracion": 8, "inicio": None, "fin": None, "tipo": None},
        {"id": 7, "llegada": 30, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 8, "llegada": 35, "duracion": 9, "inicio": None, "fin": None, "tipo": None},
        {"id": 9, "llegada": 40, "duracion": 2, "inicio": None, "fin": None, "tipo": None},
        {"id": 10, "llegada": 45, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
    ]
    return procesos


def generar_escenario_C_ALTA():
    """Escenario C_ALTA: Alta concurrencia (muchos procesos llegan casi al mismo tiempo)."""
    procesos = [
        {"id": 1, "llegada": 0, "duracion": 2, "inicio": None, "fin": None, "tipo": None},
        {"id": 2, "llegada": 0, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 3, "llegada": 0, "duracion": 4, "inicio": None, "fin": None, "tipo": None},
        {"id": 4, "llegada": 1, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
        {"id": 5, "llegada": 1, "duracion": 6, "inicio": None, "fin": None, "tipo": None},
        {"id": 6, "llegada": 1, "duracion": 7, "inicio": None, "fin": None, "tipo": None},
        {"id": 7, "llegada": 2, "duracion": 8, "inicio": None, "fin": None, "tipo": None},
        {"id": 8, "llegada": 2, "duracion": 9, "inicio": None, "fin": None, "tipo": None},
        {"id": 9, "llegada": 3, "duracion": 3, "inicio": None, "fin": None, "tipo": None},
        {"id": 10, "llegada": 3, "duracion": 5, "inicio": None, "fin": None, "tipo": None},
    ]
    return procesos

def reset_simulacion(escenario_actual):
    """Reinicia la simulación con el escenario especificado."""
    escenarios = {
        "A": ("Escenario A: Muchos procesos variados", generar_escenario_A),
        "B": ("Escenario B: Sistema aleatorio CPU/IO", generar_escenario_B),
        "C.1": ("Escenario C.1: Baja concurrencia", generar_escenario_C_BAJA),
        "C.2": ("Escenario C.2: Alta concurrencia", generar_escenario_C_ALTA)
    }
    
    nombre, generador = escenarios[escenario_actual]
    procesos = generador()
    
    pendientes = sorted(procesos, key=lambda x: (x["llegada"], procesos.index(x)))
    
    for i, p in enumerate(pendientes):
        p["orden_visual"] = i
    
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    
    print(f"\n--- {nombre} ---")
    for p in procesos:
        tipo_str = f", Tipo: {p['tipo']}" if p['tipo'] else ""
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}{tipo_str}")
    
    return nombre, procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global

def reset_personalizado(procesos_input):
    """Reinicia con procesos personalizados."""
    procesos = []
    for i, p in enumerate(procesos_input, start=1):
        procesos.append({
            "id": i,
            "llegada": p["llegada"],
            "duracion": p["duracion"],
            "tipo": p.get("tipo"),
            "inicio": None,
            "fin": None
        })
    
    pendientes = sorted(procesos, key=lambda x: x["llegada"])
    
    for i, p in enumerate(pendientes):
        p["orden_visual"] = i
    
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    
    print("\n--- Escenario Personalizado ---")
    for p in procesos:
        tipo_str = f", Tipo: {p['tipo']}" if p['tipo'] else ""
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}{tipo_str}")
    
    return "Escenario Personalizado", procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global

def calcular_metricas(procesos):
    """Calcula las métricas de rendimiento del algoritmo FCFS."""
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

    suma = sum(tiempos_espera)
    suma_cuadrados = sum(t**2 for t in tiempos_espera)
    if suma_cuadrados == 0:
        fairness = 1.0
    else:
        fairness = (suma**2) / (n * suma_cuadrados)

    return promedio_retorno, promedio_espera, promedio_respuesta, throughput, fairness

def dibujar_rectangulo_sombra(surface, color, rect, radio=8, sombra_offset=4):
    """Dibuja un rectángulo con sombra y brillo."""
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

def dibujar_input_box(ventana, rect, texto, activo, fuente, color_panel, color_acento):
    """Dibuja un campo de entrada de texto."""
    color = color_acento if activo else (100, 116, 139)
    pygame.draw.rect(ventana, color, rect, 2, border_radius=5)
    
    s = pygame.Surface((rect.width - 4, rect.height - 4), pygame.SRCALPHA)
    pygame.draw.rect(s, (*color_panel, 200), s.get_rect(), border_radius=4)
    ventana.blit(s, (rect.x + 2, rect.y + 2))
    
    texto_render = fuente.render(texto, True, (226, 232, 240))
    ventana.blit(texto_render, (rect.x + 8, rect.y + 6))

def simular_fcfs_visual():
    """Función principal de simulación visual FCFS."""
    pygame.init()
    ancho_max = 1400
    alto = 850
    ventana = pygame.display.set_mode((ancho_max, alto))
    pygame.display.set_caption("Algoritmo FCFS - First Come First Served")
    
    fuente = pygame.font.SysFont("Segoe UI", 12, bold=False)
    fuente_bold = pygame.font.SysFont("Segoe UI", 12, bold=True)
    fuente_titulo = pygame.font.SysFont("Segoe UI", 16, bold=True)
    fuente_tiempo = pygame.font.SysFont("Segoe UI", 20, bold=True)
    fuente_pequena = pygame.font.SysFont("Segoe UI", 10, bold=False)
    
    colores = [
        (255, 107, 107), (78, 205, 196), (255, 195, 113), (162, 155, 254),
        (255, 234, 167), (108, 92, 231), (255, 159, 243), (87, 242, 135)
    ]
    
    color_cpu = (255, 140, 50)
    color_io = (100, 200, 255)
    
    fondo_top = (26, 32, 44)
    fondo_bottom = (45, 55, 72)
    color_panel = (30, 41, 59)
    color_texto = (226, 232, 240)
    color_texto_secundario = (148, 163, 184)
    color_acento = (99, 102, 241)
    color_acento_hover = (79, 70, 229)
    color_linea_tiempo = (251, 146, 60)
    
    reloj = pygame.time.Clock()
    velocidad = 0.01

    boton_reiniciar = pygame.Rect(ancho_max - 130, 10, 115, 30)
    boton_regresar = pygame.Rect(ancho_max - 250, 10, 115, 30)
    boton_esc_a = pygame.Rect(20, alto - 50, 85, 35)
    boton_esc_b = pygame.Rect(115, alto - 50, 85, 35)
    boton_esc_c = pygame.Rect(210, alto - 50, 85, 35)
    boton_esc_d = pygame.Rect(305, alto - 50, 85, 35)
    boton_personalizado = pygame.Rect(400, alto - 50, 110, 35)
    
    botones_escenarios = [
        (boton_esc_a, "A", "Escenario A"),
        (boton_esc_b, "B", "Escenario B"),
        (boton_esc_c, "C.1", "Escenario C"),
        (boton_esc_d, "C.2", "Escenario C"),
        (boton_personalizado, "P", "Personalizado")
    ]

    modo_personalizado = False
    procesos_personalizados = []
    input_llegada = ""
    input_duracion = ""
    input_activo = None
    
    # Centrar panel personalizado
    panel_ancho = 580
    panel_inicio_x = (ancho_max - panel_ancho) // 2
    
    input_rect_llegada = pygame.Rect(panel_inicio_x + 30, alto // 2 - 140, 120, 35)
    input_rect_duracion = pygame.Rect(panel_inicio_x + 170, alto // 2 - 140, 120, 35)
    boton_agregar = pygame.Rect(panel_inicio_x + 310, alto // 2 - 140, 100, 35)
    boton_limpiar = pygame.Rect(panel_inicio_x + 430, alto // 2 - 140, 100, 35)
    boton_simular = pygame.Rect(panel_inicio_x + 190, alto // 2 + 120, 200, 40)
    boton_editar = pygame.Rect(ancho_max - 250, 10, 110, 30)

    escenario_actual = "A"
    nombre_escenario, procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion(escenario_actual)
    corriendo = True
    simulacion_terminada = False
    metricas_calculadas = False
    metricas = None
    
    proceso_seleccionado = None
    tiempo_seleccion = 0

    while corriendo:
        for y in range(alto):
            factor = y / alto
            r = int(fondo_top[0] + (fondo_bottom[0] - fondo_top[0]) * factor)
            g = int(fondo_top[1] + (fondo_bottom[1] - fondo_top[1]) * factor)
            b = int(fondo_top[2] + (fondo_bottom[2] - fondo_top[2]) * factor)
            pygame.draw.line(ventana, (r, g, b), (0, y), (ancho_max, y))

        mouse_pos = pygame.mouse.get_pos()
        
        # Botón reiniciar (solo en escenarios predefinidos)
        if not modo_personalizado:
            color_boton = color_acento if not boton_reiniciar.collidepoint(mouse_pos) else color_acento_hover
            sombra_boton = boton_reiniciar.copy()
            sombra_boton.y += 2
            pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_boton, border_radius=6)
            pygame.draw.rect(ventana, color_boton, boton_reiniciar, border_radius=6)
            texto_boton = fuente_bold.render("Reiniciar", True, (255, 255, 255))
            ventana.blit(texto_boton, (boton_reiniciar.x + 25, boton_reiniciar.y + 8))
        
        # Botón regresar
        color_regresar = (239, 68, 68) if not boton_regresar.collidepoint(mouse_pos) else (209, 58, 58)
        sombra_regresar = boton_regresar.copy()
        sombra_regresar.y += 2
        pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_regresar, border_radius=6)
        pygame.draw.rect(ventana, color_regresar, boton_regresar, border_radius=6)
        texto_regresar = fuente_bold.render("Regresar", True, (255, 255, 255))
        ventana.blit(texto_regresar, (boton_regresar.x + 20, boton_regresar.y + 8))
        
        # Botón editar (solo en modo personalizado después de simular)
        if modo_personalizado and simulacion_terminada:
            color_editar = color_acento if not boton_editar.collidepoint(mouse_pos) else color_acento_hover
            sombra_editar = boton_editar.copy()
            sombra_editar.y += 2
            pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_editar, border_radius=6)
            pygame.draw.rect(ventana, color_editar, boton_editar, border_radius=6)
            texto_editar = fuente_bold.render("Editar Procesos", True, (255, 255, 255))
            ventana.blit(texto_editar, (boton_editar.x + 8, boton_editar.y + 8))

        texto_escenario = fuente_titulo.render(nombre_escenario, True, color_texto)
        ventana.blit(texto_escenario, (ancho_max // 2 - texto_escenario.get_width() // 2, 15))

        if modo_personalizado and not simulacion_terminada:
            panel_input = pygame.Rect(panel_inicio_x, alto // 2 - 200, panel_ancho, 380)
            s_panel = pygame.Surface((panel_input.width, panel_input.height), pygame.SRCALPHA)
            pygame.draw.rect(s_panel, (*color_panel, 250), s_panel.get_rect(), border_radius=15)
            ventana.blit(s_panel, panel_input)
            
            titulo_input = fuente_titulo.render("Agregar Procesos Personalizados", True, color_texto)
            titulo_rect = titulo_input.get_rect(center=(ancho_max // 2, alto // 2 - 175))
            ventana.blit(titulo_input, titulo_rect)
            
            label_llegada = fuente_bold.render("Llegada:", True, color_texto)
            label_duracion = fuente_bold.render("Duración:", True, color_texto)
            ventana.blit(label_llegada, (input_rect_llegada.x, input_rect_llegada.y - 25))
            ventana.blit(label_duracion, (input_rect_duracion.x, input_rect_duracion.y - 25))
            
            dibujar_input_box(ventana, input_rect_llegada, input_llegada, input_activo == 'llegada', fuente, color_panel, color_acento)
            dibujar_input_box(ventana, input_rect_duracion, input_duracion, input_activo == 'duracion', fuente, color_panel, color_acento)
            
            color_agregar = color_acento if not boton_agregar.collidepoint(mouse_pos) else color_acento_hover
            pygame.draw.rect(ventana, color_agregar, boton_agregar, border_radius=8)
            texto_agregar = fuente_bold.render("Agregar", True, (255, 255, 255))
            texto_agregar_rect = texto_agregar.get_rect(center=boton_agregar.center)
            ventana.blit(texto_agregar, texto_agregar_rect)
            
            color_limpiar = (220, 38, 38) if not boton_limpiar.collidepoint(mouse_pos) else (185, 28, 28)
            pygame.draw.rect(ventana, color_limpiar, boton_limpiar, border_radius=8)
            texto_limpiar = fuente_bold.render("Limpiar", True, (255, 255, 255))
            texto_limpiar_rect = texto_limpiar.get_rect(center=boton_limpiar.center)
            ventana.blit(texto_limpiar, texto_limpiar_rect)
            
            # Línea separadora
            separador_y = alto // 2 - 90
            pygame.draw.line(ventana, color_texto_secundario, 
                           (panel_inicio_x + 20, separador_y), 
                           (panel_inicio_x + panel_ancho - 20, separador_y), 2)
            
            if procesos_personalizados:
                texto_lista = fuente_titulo.render(f"Procesos Agregados: {len(procesos_personalizados)}", True, color_texto)
                texto_lista_rect = texto_lista.get_rect(center=(ancho_max // 2, alto // 2 - 65))
                ventana.blit(texto_lista, texto_lista_rect)
                
                y_lista = alto // 2 - 35
                x_base = panel_inicio_x + 40
                col_spacing = 270
                
                for i, p in enumerate(procesos_personalizados):
                    col = i % 2
                    row = i // 2
                    
                    if row >= 5:  # Máximo 10 procesos visibles (5 filas x 2 columnas)
                        break
                    
                    x_pos = x_base + col * col_spacing
                    y_pos = y_lista + row * 25
                    
                    texto_p = fuente.render(
                        f"P{i+1}: L={p['llegada']}, D={p['duracion']}", 
                        True, color_texto_secundario
                    )
                    ventana.blit(texto_p, (x_pos, y_pos))
                
                if len(procesos_personalizados) > 10:
                    texto_mas = fuente_pequena.render(f"+ {len(procesos_personalizados) - 10} más...", True, color_texto_secundario)
                    ventana.blit(texto_mas, (panel_inicio_x + 40, y_lista + 130))
            else:
                texto_vacio = fuente.render("No hay procesos. Agrega al menos 2 para simular.", True, color_texto_secundario)
                texto_vacio_rect = texto_vacio.get_rect(center=(ancho_max // 2, alto // 2 - 20))
                ventana.blit(texto_vacio, texto_vacio_rect)
            
            # Botón simular (más grande y centrado abajo)
            puede_simular = len(procesos_personalizados) >= 2
            color_simular = (34, 197, 94) if puede_simular and not boton_simular.collidepoint(mouse_pos) else (22, 163, 74) if puede_simular else (100, 100, 100)
            pygame.draw.rect(ventana, color_simular, boton_simular, border_radius=10)
            texto_simular = fuente_titulo.render("Iniciar Simulación", True, (255, 255, 255))
            texto_simular_rect = texto_simular.get_rect(center=boton_simular.center)
            ventana.blit(texto_simular, texto_simular_rect)
            
            instruccion = fuente_pequena.render("Presiona TAB para cambiar de campo o ENTER para agregar rápidamente", True, color_texto_secundario)
            instruccion_rect = instruccion.get_rect(center=(ancho_max // 2, alto // 2 + 175))
            ventana.blit(instruccion, instruccion_rect)

        if not modo_personalizado or (modo_personalizado and simulacion_terminada):
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
                proceso_seleccionado = en_cola[0]
                tiempo_seleccion = time.time()
                proceso_seleccionado["pos_inicial"] = (220, 60)
            
            if proceso_seleccionado and time.time() - tiempo_seleccion > 0.8:
                ejecutando = proceso_seleccionado
                ejecutando["inicio"] = tiempo_global
                ejecutando["fin"] = tiempo_global + ejecutando["duracion"]
                en_cola.remove(ejecutando)
                proceso_seleccionado = None

            tiempo_max_actual = tiempo_global
            for p in terminados + ([ejecutando] if ejecutando else []):
                tiempo_max_actual = max(tiempo_max_actual, p["fin"])
            for p in en_cola:
                tiempo_max_actual = max(tiempo_max_actual, p["llegada"] + p["duracion"])
            for p in pendientes:
                tiempo_max_actual = max(tiempo_max_actual, p["llegada"] + p["duracion"])
            tiempo_max_actual = math.ceil(tiempo_max_actual)
            
            ancho_disponible = ancho_max - 250
            escala = min((ancho_disponible) / (tiempo_max_actual + 2), 40)

            panel_cola = pygame.Rect(20, 50, ancho_max - 170, 65)
            s_panel = pygame.Surface((panel_cola.width, panel_cola.height), pygame.SRCALPHA)
            pygame.draw.rect(s_panel, (*color_panel, 230), s_panel.get_rect(), border_radius=10)
            ventana.blit(s_panel, panel_cola)
            
            titulo_cola = fuente_titulo.render("Cola FCFS", True, color_texto)
            ventana.blit(titulo_cola, (35, 58))

            for i, p in enumerate(en_cola):
                if proceso_seleccionado and p["id"] == proceso_seleccionado["id"]:
                    continue
                    
                rect_x = 220 + i * 85
                rect_y = 60
                rect = pygame.Rect(rect_x, rect_y, 70, 48)
                
                if p.get("tipo") == "CPU":
                    color = color_cpu
                elif p.get("tipo") == "IO":
                    color = color_io
                else:
                    color = colores[p["id"] % len(colores)]
                
                dibujar_rectangulo_sombra(ventana, color, rect, radio=8)
                
                texto_id = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255))
                texto_dur = fuente_pequena.render(f"{p['duracion']}s", True, (255, 255, 255))
                ventana.blit(texto_id, (rect_x + 6, rect_y + 5))
                ventana.blit(texto_dur, (rect_x + 6, rect_y + 25))
                
                if p.get("tipo"):
                    texto_tipo = fuente_pequena.render(p["tipo"], True, (255, 255, 255))
                    ventana.blit(texto_tipo, (rect_x + 38, rect_y + 7))
            
            num_procesos = len(terminados) + (1 if ejecutando else 0) + len(en_cola) + len(pendientes)
            altura_disponible = alto - 490
            altura_proceso = max(15, min(35, altura_disponible // max(num_procesos, 1)))
            espacio_entre_procesos = altura_proceso + 3
            
            y_recta = alto - 320
            area_grafico = pygame.Rect(20, 120, ancho_max - 170, y_recta - 120)
            pygame.draw.rect(ventana, color_panel, area_grafico)
            
            for idx, p in enumerate(terminados + ([ejecutando] if ejecutando else [])):
                x_inicio = 100 + int(p["inicio"] * escala)
                ancho_rect = int(max(min(tiempo_global, p["fin"]) - p["inicio"], 0) * escala) if p is ejecutando else int((p["fin"] - p["inicio"]) * escala)
                
                y_proceso = y_recta - 10 - (idx + 1) * espacio_entre_procesos
                
                if p.get("tipo") == "CPU":
                    color = color_cpu
                elif p.get("tipo") == "IO":
                    color = color_io
                else:
                    color = colores[p["id"] % len(colores)]
                
                rect = pygame.Rect(x_inicio, y_proceso, ancho_rect, altura_proceso)
                
                if p is ejecutando:
                    alpha = int(128 + 127 * math.sin(tiempo_global * 3))
                    s = pygame.Surface((ancho_rect + 6, altura_proceso + 4), pygame.SRCALPHA)
                    pygame.draw.rect(s, (*color, alpha), pygame.Rect(3, 2, ancho_rect, altura_proceso), border_radius=6)
                    ventana.blit(s, (x_inicio - 3, y_proceso - 2))
                
                dibujar_rectangulo_sombra(ventana, color, rect, radio=6, sombra_offset=2)
                
                texto_p = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255))
                ventana.blit(texto_p, (x_inicio + 4, y_proceso + (altura_proceso - texto_p.get_height()) // 2))
                
                if ancho_rect > 50 and altura_proceso > 20:
                    texto_inicio = fuente_pequena.render(str(int(p["inicio"])), True, (255, 255, 255))
                    texto_fin = fuente_pequena.render(str(int(p["fin"] if p is not ejecutando else min(tiempo_global, p["fin"]))), True, (255, 255, 255))
                    ventana.blit(texto_inicio, (x_inicio + 2, y_proceso + altura_proceso - 12))
                    ventana.blit(texto_fin, (x_inicio + ancho_rect - texto_fin.get_width() - 2, y_proceso + altura_proceso - 12))
            
            pygame.draw.rect(ventana, color_texto_secundario, area_grafico, 2, border_radius=8)
            
            pygame.draw.line(ventana, color_texto, (100, y_recta), (100 + int(tiempo_max_actual * escala), y_recta), 3)
            
            num_marcadores = min(tiempo_max_actual + 1, 25)
            paso = max(1, tiempo_max_actual // num_marcadores)
            
            for t in range(0, tiempo_max_actual + 1, paso):
                x = 100 + int(t * escala)
                pygame.draw.line(ventana, color_texto, (x, y_recta - 8), (x, y_recta + 8), 3)
                texto_t = fuente_bold.render(str(t), True, color_texto)
                ventana.blit(texto_t, (x - texto_t.get_width()//2, y_recta + 15))
            
            if ejecutando and tiempo_global >= ejecutando["fin"]:
                terminados.append(ejecutando)
                ejecutando = None
            
            x_tiempo = 100 + int(tiempo_global * escala)
            x_tiempo = min(x_tiempo, 100 + int(tiempo_max_actual * escala))
            for offset in [5, 3, 2]:
                s_glow = pygame.Surface((offset*2, y_recta - 125), pygame.SRCALPHA)
                pygame.draw.line(s_glow, (*color_linea_tiempo, 40), (offset, 0), (offset, y_recta - 125), offset)
                ventana.blit(s_glow, (x_tiempo - offset, 125))
            pygame.draw.line(ventana, color_linea_tiempo, (x_tiempo, 125), (x_tiempo, y_recta), 2)
            pygame.draw.circle(ventana, color_linea_tiempo, (x_tiempo, y_recta), 6)
            pygame.draw.circle(ventana, (255, 255, 255), (x_tiempo, y_recta), 3)

            tiempo_texto = f"{int(tiempo_global)}s"
            texto_tiempo = fuente_tiempo.render(tiempo_texto, True, color_linea_tiempo)
            rect_tiempo = texto_tiempo.get_rect(center=(ancho_max//2, 125))
            
            fondo_tiempo = pygame.Rect(rect_tiempo.x - 12, rect_tiempo.y - 6, rect_tiempo.width + 24, rect_tiempo.height + 12)
            s_tiempo = pygame.Surface((fondo_tiempo.width, fondo_tiempo.height), pygame.SRCALPHA)
            pygame.draw.rect(s_tiempo, (*color_panel, 200), s_tiempo.get_rect(), border_radius=12)
            ventana.blit(s_tiempo, fondo_tiempo)
            ventana.blit(texto_tiempo, rect_tiempo)
            
            if proceso_seleccionado:
                progreso = (time.time() - tiempo_seleccion) / 0.8
                progreso = min(progreso, 1.0)
                
                if progreso < 0.5:
                    eased = 2 * progreso * progreso
                else:
                    eased = 1 - pow(-2 * progreso + 2, 2) / 2
                
                x_inicial, y_inicial = proceso_seleccionado["pos_inicial"]
                idx_proceso = len([p for p in terminados if p["inicio"] <= tiempo_global])
                y_final = y_recta - 10 - (idx_proceso + 1) * espacio_entre_procesos
                x_final = 100 + int(tiempo_global * escala)
                
                x_actual = x_inicial + (x_final - x_inicial) * eased
                arco = -70 * math.sin(eased * math.pi)
                y_actual = y_inicial + (y_final - y_inicial) * eased + arco
                
                escala_rect = 1.0 + 0.3 * math.sin(eased * math.pi)
                ancho_rect = int(70 * escala_rect)
                alto_rect = int(48 * escala_rect if eased < 0.5 else 48 * escala_rect * 0.7)
                
                rect_anim = pygame.Rect(int(x_actual), int(y_actual), ancho_rect, alto_rect)
                
                if proceso_seleccionado.get("tipo") == "CPU":
                    color = color_cpu
                elif proceso_seleccionado.get("tipo") == "IO":
                    color = color_io
                else:
                    color = colores[proceso_seleccionado["id"] % len(colores)]
                
                for offset in [12, 8, 4]:
                    s_glow = pygame.Surface((ancho_rect + offset*2, alto_rect + offset*2), pygame.SRCALPHA)
                    pygame.draw.rect(s_glow, (*color, int(20 * (1-progreso))), 
                                   pygame.Rect(offset, offset, ancho_rect, alto_rect), border_radius=8)
                    ventana.blit(s_glow, (int(x_actual) - offset, int(y_actual) - offset))
                
                dibujar_rectangulo_sombra(ventana, color, rect_anim, radio=8, sombra_offset=int(4 * escala_rect))
                
                texto_id = fuente_bold.render(f"P{proceso_seleccionado['id']}", True, (255, 255, 255))
                texto_dur = fuente_pequena.render(f"{proceso_seleccionado['duracion']}s", True, (255, 255, 255))
                ventana.blit(texto_id, (int(x_actual) + 6, int(y_actual) + 5))
                ventana.blit(texto_dur, (int(x_actual) + 6, int(y_actual) + 25))
                
                num_particulas = 6
                for j in range(num_particulas):
                    angulo = (j / num_particulas) * 2 * math.pi + progreso * 2
                    radio_particula = 25 + 15 * progreso
                    px = int(x_actual + ancho_rect/2 + math.cos(angulo) * radio_particula)
                    py = int(y_actual + alto_rect/2 + math.sin(angulo) * radio_particula)
                    tamanho = int(2 * (1 - progreso))
                    if tamanho > 0:
                        pygame.draw.circle(ventana, (*color, int(150 * (1-progreso))), (px, py), tamanho)

            if not pendientes and not en_cola and ejecutando is None and len(terminados) > 0:
                if not metricas_calculadas:
                    metricas_calculadas = True
                    retorno, espera, respuesta, throughput, fairness = calcular_metricas(terminados)
                    metricas = [
                        ("T. Retorno", f"{retorno:.2f}s"),
                        ("T. Espera", f"{espera:.2f}s"),
                        ("T. Respuesta", f"{respuesta:.2f}s"),
                        ("Throughput", f"{throughput:.3f}"),
                        ("Fairness", f"{fairness:.3f}")
                    ]

                panel_x = 40
                panel_y = alto - 225
                panel_w = ancho_max - 80
                panel_h = 110
                
                s_panel_metricas = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
                pygame.draw.rect(s_panel_metricas, (*color_panel, 240), s_panel_metricas.get_rect(), border_radius=12)
                ventana.blit(s_panel_metricas, (panel_x, panel_y))
                
                titulo_metricas = fuente_titulo.render("Métricas de Rendimiento", True, color_texto)
                ventana.blit(titulo_metricas, (panel_x + 20, panel_y + 15))
                
                card_y = panel_y + 50
                card_w = 240
                card_h = 48
                spacing = 15
                
                total_width = len(metricas) * card_w + (len(metricas) - 1) * spacing
                start_x = panel_x + (panel_w - total_width) // 2
                
                for i, (nombre, valor) in enumerate(metricas):
                    card_x = start_x + i * (card_w + spacing)
                    card_rect = pygame.Rect(card_x, card_y, card_w, card_h)
                    color_card = colores[i % len(colores)]
                    
                    sombra_card = card_rect.copy()
                    sombra_card.y += 2
                    s_sombra = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
                    pygame.draw.rect(s_sombra, (0, 0, 0, 60), s_sombra.get_rect(), border_radius=8)
                    ventana.blit(s_sombra, sombra_card)
                    
                    s_card = pygame.Surface((card_w, card_h), pygame.SRCALPHA)
                    for y in range(card_h):
                        alpha = 200 - int(50 * (y / card_h))
                        pygame.draw.line(s_card, (*color_card, alpha), (0, y), (card_w, y))
                    ventana.blit(s_card, card_rect)
                    pygame.draw.rect(ventana, color_card, card_rect, 2, border_radius=8)
                    
                    texto_nombre = fuente.render(nombre, True, (255, 255, 255))
                    texto_valor = fuente_bold.render(valor, True, (255, 255, 255))
                    
                    ventana.blit(texto_nombre, (card_x + 12, card_y + 8))
                    ventana.blit(texto_valor, (card_x + 12, card_y + 26))

        for boton, clave, texto in botones_escenarios:
            es_actual = (clave == escenario_actual if clave != "P" else modo_personalizado)
            color_b = (50, 205, 50) if es_actual else (color_acento if not boton.collidepoint(mouse_pos) else color_acento_hover)
            
            sombra = boton.copy()
            sombra.y += 2
            pygame.draw.rect(ventana, (0, 0, 0, 80), sombra, border_radius=6)
            pygame.draw.rect(ventana, color_b, boton, border_radius=6)
            
            texto_render = fuente_bold.render(texto, True, (255, 255, 255))
            texto_rect = texto_render.get_rect(center=boton.center)
            ventana.blit(texto_render, texto_rect)

        pygame.display.flip()
        reloj.tick(60)
        
        # Solo avanzar el tiempo si la simulación está corriendo y no ha terminado
        if (not modo_personalizado or (modo_personalizado and simulacion_terminada)) and not metricas_calculadas:
            if proceso_seleccionado is None:
                tiempo_global += 0.02
                if tiempo_global > tiempo_max_actual:
                    tiempo_global = tiempo_max_actual
            time.sleep(0.05 * velocidad)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Botón regresar al menú
                if boton_regresar.collidepoint(event.pos):
                    pygame.quit()
                    import subprocess
                    import sys
                    subprocess.Popen([sys.executable, "menu_principal.py"])
                    return
                
                # Botón reiniciar (solo para escenarios predefinidos)
                if not modo_personalizado and boton_reiniciar.collidepoint(event.pos):
                    nombre_escenario, procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion(escenario_actual)
                    simulacion_terminada = False
                    metricas_calculadas = False
                    metricas = None
                    proceso_seleccionado = None
                
                # Botón editar procesos (solo en modo personalizado)
                if boton_editar.collidepoint(event.pos) and modo_personalizado and simulacion_terminada:
                    simulacion_terminada = False
                    metricas_calculadas = False
                    metricas = None
                    simulacion_terminada = False
                    nombre_escenario = "Escenario Personalizado"
                    procesos = []
                    pendientes = []
                    terminados = []
                    en_cola = []
                    ejecutando = None
                    tiempo_global = 0
                    proceso_seleccionado = None
                
                for boton, clave, _ in botones_escenarios:
                    if boton.collidepoint(event.pos):
                        if clave == "P":
                            modo_personalizado = True
                            escenario_actual = "P"
                            procesos_personalizados = []
                            input_llegada = ""
                            input_duracion = ""
                            simulacion_terminada = False
                            metricas_calculadas = False
                            metricas = None
                        else:
                            modo_personalizado = False
                            escenario_actual = clave
                            nombre_escenario, procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_simulacion(escenario_actual)
                            simulacion_terminada = False
                            metricas_calculadas = False
                            metricas = None
                            proceso_seleccionado = None
                        break
                
                if modo_personalizado and not simulacion_terminada:
                    if input_rect_llegada.collidepoint(event.pos):
                        input_activo = 'llegada'
                    elif input_rect_duracion.collidepoint(event.pos):
                        input_activo = 'duracion'
                    else:
                        input_activo = None
                    
                    if boton_agregar.collidepoint(event.pos):
                        try:
                            llegada = int(input_llegada) if input_llegada else 0
                            duracion = int(input_duracion) if input_duracion else 1
                            
                            if llegada >= 0 and duracion > 0:
                                procesos_personalizados.append({
                                    "llegada": llegada,
                                    "duracion": duracion,
                                    "tipo": None
                                })
                                input_llegada = ""
                                input_duracion = ""
                                print(f"Proceso agregado: Llegada={llegada}, Duración={duracion}")
                        except ValueError:
                            pass
                    
                    elif boton_limpiar.collidepoint(event.pos):
                        procesos_personalizados = []
                        input_llegada = ""
                        input_duracion = ""
                        print("Lista limpiada")
                    
                    elif boton_simular.collidepoint(event.pos) and len(procesos_personalizados) >= 2:
                        nombre_escenario, procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global = reset_personalizado(procesos_personalizados)
                        simulacion_terminada = True
                        metricas_calculadas = False
                        metricas = None
                        proceso_seleccionado = None
            
            elif event.type == pygame.KEYDOWN and modo_personalizado and not simulacion_terminada:
                if input_activo == 'llegada':
                    if event.key == pygame.K_BACKSPACE:
                        input_llegada = input_llegada[:-1]
                    elif event.unicode.isdigit():
                        input_llegada += event.unicode
                    elif event.key == pygame.K_TAB:
                        input_activo = 'duracion'
                
                elif input_activo == 'duracion':
                    if event.key == pygame.K_BACKSPACE:
                        input_duracion = input_duracion[:-1]
                    elif event.unicode.isdigit():
                        input_duracion += event.unicode
                    elif event.key == pygame.K_TAB:
                        input_activo = 'llegada'
                
                if event.key == pygame.K_RETURN and input_activo:
                    try:
                        llegada = int(input_llegada) if input_llegada else 0
                        duracion = int(input_duracion) if input_duracion else 1
                        
                        if llegada >= 0 and duracion > 0:
                            procesos_personalizados.append({
                                "llegada": llegada,
                                "duracion": duracion,
                                "tipo": None
                            })
                            input_llegada = ""
                            input_duracion = ""
                            input_activo = 'llegada'
                            print(f"Proceso agregado: Llegada={llegada}, Duración={duracion}")
                    except ValueError:
                        pass

    pygame.quit()

if __name__ == "__main__":
    simular_fcfs_visual()