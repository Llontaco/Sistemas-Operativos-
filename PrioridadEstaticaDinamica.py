import pygame
import time
import random
import math

# --- 1. DEFINICIÓN DE ESCENARIOS (ACTUALIZADO) ---
ESCENARIOS = {
    "A": [
        {"id": 1, "llegada": 0, "duracion": 6, "prioridad": 1},
        {"id": 2, "llegada": 0, "duracion": 8, "prioridad": 6},
        {"id": 3, "llegada": 0, "duracion": 4, "prioridad": 3},
        {"id": 4, "llegada": 0, "duracion": 7, "prioridad": 2},
        {"id": 5, "llegada": 0, "duracion": 5, "prioridad": 4},
        {"id": 6, "llegada": 0, "duracion": 9, "prioridad": 0},
        {"id": 7, "llegada": 0, "duracion": 3, "prioridad": 1},
        {"id": 8, "llegada": 0, "duracion": 2, "prioridad": 2},
        {"id": 9, "llegada": 0, "duracion": 5, "prioridad": 0},
        {"id": 10, "llegada": 0, "duracion": 8, "prioridad": 5}
    ],
    "B": [
        {"id": 1, "llegada": 0, "duracion": 6, "prioridad": 8},
        {"id": 2, "llegada": 0, "duracion": 3, "prioridad": 15},
        {"id": 3, "llegada": 0, "duracion": 2, "prioridad": 4},
        {"id": 4, "llegada": 0, "duracion": 5, "prioridad": 0},
        {"id": 5, "llegada": 0, "duracion": 7, "prioridad": 0},
        {"id": 6, "llegada": 0, "duracion": 4, "prioridad": 3},
        {"id": 7, "llegada": 0, "duracion": 8, "prioridad": 8},
        {"id": 8, "llegada": 0, "duracion": 3, "prioridad": 2},
        {"id": 9, "llegada": 0, "duracion": 2, "prioridad": 1},
        {"id": 10, "llegada": 0, "duracion": 9, "prioridad": 4}
    ],
    "C_BAJA": [ # Nuevo escenario
        {"id": 1, "llegada": 0, "duracion": 5, "prioridad": 1},
        {"id": 2, "llegada": 0, "duracion": 3, "prioridad": 8},
        {"id": 3, "llegada": 0, "duracion": 7, "prioridad": 3},
        {"id": 4, "llegada": 0, "duracion": 4, "prioridad": 9},
        {"id": 5, "llegada": 0, "duracion": 6, "prioridad": 1},
        {"id": 6, "llegada": 0, "duracion": 8, "prioridad": 4},
        {"id": 7, "llegada": 0, "duracion": 3, "prioridad": 0},
        {"id": 8, "llegada": 0, "duracion": 9, "prioridad": 8},
        {"id": 9, "llegada": 0, "duracion": 2, "prioridad": 2},
        {"id": 10, "llegada": 0, "duracion": 5, "prioridad": 10}
    ],
    "C_ALTA": [ # Nuevo escenario
        {"id": 1, "llegada": 0, "duracion": 2, "prioridad": 5},
        {"id": 2, "llegada": 0, "duracion": 3, "prioridad": 6},
        {"id": 3, "llegada": 0, "duracion": 4, "prioridad": 5},
        {"id": 4, "llegada": 0, "duracion": 5, "prioridad": 7},
        {"id": 5, "llegada": 0, "duracion": 6, "prioridad": 6},
        {"id": 6, "llegada": 0, "duracion": 7, "prioridad": 8},
        {"id": 7, "llegada": 0, "duracion": 8, "prioridad": 7},
        {"id": 8, "llegada": 0, "duracion": 9, "prioridad": 8},
        {"id": 9, "llegada": 0, "duracion": 3, "prioridad": 9},
        {"id": 10, "llegada": 0, "duracion": 5, "prioridad": 9}
    ]
    # "PERSONALIZADO_TEMP" se creará dinámicamente
}

# --- 2. FUNCIÓN DE GENERACIÓN MODIFICADA ---
def generar_procesos(escenario_id="A"):
    """
    Carga un escenario manual. El aleatorio ahora se maneja por el formulario.
    """
    procesos_base = []
    
    if escenario_id in ESCENARIOS:
        # Cargar escenario manual
        print(f"\n--- Cargando escenario manual: {escenario_id} ---")
        procesos_base = [p.copy() for p in ESCENARIOS[escenario_id]]
    else:
        # Fallback por si acaso, aunque no debería usarse
        print(f"--- ¡Error! Escenario '{escenario_id}' no encontrado. Cargando A. ---")
        procesos_base = [p.copy() for p in ESCENARIOS["A"]]

    # Completar la estructura de datos para la simulación
    procesos_completos = []
    for p in procesos_base:
        duracion = p["duracion"]
        prioridad = p["prioridad"]
        procesos_completos.append({
            "id": p["id"],
            "llegada": p["llegada"],
            "duracion": duracion,
            "restante": duracion,
            "prioridad_estatica": prioridad,
            "prioridad_dinamica": prioridad,
            "tiempo_espera": 0,
            "inicio": None,
            "fin": None,
            "respuesta": None
        })
    return procesos_completos

# --- 3. NUEVA FUNCIÓN PARA PARSEAR EL FORMULARIO ---
def parsear_input_a_escenario(input_data):
    """
    Convierte los datos de texto del formulario en un escenario y lo guarda.
    """
    escenario_temp = []
    for i in range(10):
        try:
            # Si el string está vacío, usar 1
            dur_str = input_data[i]["duracion"]
            dur = int(dur_str) if dur_str else 1
        except ValueError:
            dur = 1 # Default
            
        try:
            # Si el string está vacío, usar 10
            pri_str = input_data[i]["prioridad"]
            pri = int(pri_str) if pri_str else 10
        except ValueError:
            pri = 10 # Default
            
        escenario_temp.append({
            "id": i + 1,
            "llegada": 0, # Llegada siempre 0 para el formulario
            "duracion": max(1, dur), # Mínimo 1
            "prioridad": max(0, min(10, pri)) # Rango 0-10
        })
    # Guarda el escenario generado en el diccionario global
    ESCENARIOS["PERSONALIZADO_TEMP"] = escenario_temp
    return "PERSONALIZADO_TEMP"

# --- 4. FUNCIÓN DE RESET (Sin cambios) ---
def reset_simulacion(algoritmo='dinamica', factor_envejecimiento=1, escenario_id="A"):
    """
    Reinicia la simulación con un escenario específico.
    """
    procesos = generar_procesos(escenario_id)
    pendientes = sorted(procesos, key=lambda x: x["llegada"])
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    tiempo_ejecucion_inicio = 0
    timeline = []
    
    print(f"Algoritmo: {algoritmo.upper()}")
    print(f"Factor de envejecimiento: {factor_envejecimiento}")
    for p in procesos:
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}, Prioridad: {p['prioridad_estatica']}")
    
    return (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
            tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, escenario_id)


def calcular_metricas(procesos):
    """Calcula métricas de rendimiento"""
    n = len(procesos)
    if n == 0: return 0, 0, 0, 0
    
    retorno_total = 0
    espera_total = 0
    respuesta_total = 0
    
    for p in procesos:
        retorno = p['fin'] - p['llegada']
        espera = p['tiempo_espera']
        respuesta = p['respuesta'] if p['respuesta'] is not None else 0
        retorno_total += retorno
        espera_total += espera
        respuesta_total += respuesta
        
    promedio_retorno = retorno_total / n
    promedio_espera = espera_total / n
    promedio_respuesta = respuesta_total / n
    
    tiempo_total = max(p['fin'] for p in procesos) - min(p['llegada'] for p in procesos)
    throughput = n / tiempo_total if tiempo_total > 0 else 0
    
    return promedio_retorno, promedio_espera, promedio_respuesta, throughput

# --- 5. FUNCIÓN DE COLOR MODIFICADA (0-10) ---
def obtener_color_prioridad(prioridad):
    """Retorna un color basado en la prioridad (0=rojo urgente, 10=verde bajo)"""
    factor = max(0, min(1, prioridad / 10.0))
    r = int(255 * (1 - factor) + 87 * factor)
    g = int(107 * (1 - factor) + 242 * factor)
    b = int(107 * (1 - factor) + 135 * factor)
    return (r, g, b)

def dibujar_rectangulo_sombra(surface, color, rect, radio=8, sombra_offset=4):
    """Dibuja un rectángulo con efecto de sombra y brillo"""
    sombra_rect = rect.copy()
    sombra_rect.x += sombra_offset
    sombra_rect.y += sombra_offset
    pygame.draw.rect(surface, (0, 0, 0, 50), sombra_rect, border_radius=radio)
    pygame.draw.rect(surface, color, rect, border_radius=radio)
    
    brillo_color = tuple(min(c + 40, 255) for c in color[:3])
    brillo_rect = pygame.Rect(rect.x, rect.y, rect.width, rect.height // 3)
    s = pygame.Surface((brillo_rect.width, brillo_rect.height), pygame.SRCALPHA)
    pygame.draw.rect(s, (*brillo_color, 60), s.get_rect(), border_radius=12)
    surface.blit(s, brillo_rect)

def seleccionar_proceso_prioritario(cola, algoritmo):
    """Selecciona el proceso con mayor prioridad (menor número)"""
    if not cola:
        return None
    
    if algoritmo == 'estatica':
        return min(cola, key=lambda p: (p['prioridad_estatica'], p['llegada']))
    else:  # dinámica
        return min(cola, key=lambda p: (p['prioridad_dinamica'], p['llegada']))

# --- 6. SIMULACIÓN PRINCIPAL (CON GRANDES CAMBIOS) ---
def simular_prioridades_visual():
    """Función principal que ejecuta la simulación visual"""
    pygame.init()
    ancho_max = 1700
    alto = 950
    ventana = pygame.display.set_mode((ancho_max, alto))
    pygame.display.set_caption("Algoritmo de Prioridades (Estática/Dinámica)")
    
    # Fuentes
    fuente = pygame.font.SysFont("Segoe UI", 18, bold=False)
    fuente_bold = pygame.font.SysFont("Segoe UI", 18, bold=True)
    fuente_titulo = pygame.font.SysFont("Segoe UI", 24, bold=True)
    fuente_tiempo = pygame.font.SysFont("Segoe UI", 32, bold=True)
    fuente_small = pygame.font.SysFont("Segoe UI", 14, bold=False)
    fuente_boton_esc = pygame.font.SysFont("Segoe UI", 16, bold=True)
    
    # Colores
    fondo_top = (26, 32, 44)
    fondo_bottom = (45, 55, 72)
    color_panel = (30, 41, 59)
    color_texto = (226, 232, 240)
    color_texto_secundario = (148, 163, 184)
    color_acento = (99, 102, 241)
    color_acento_hover = (79, 70, 229)
    color_linea_tiempo = (251, 146, 60)
    color_prioridad_alta = (239, 68, 68)
    color_prioridad_baja = (34, 197, 94)
    color_boton_activo = (251, 146, 60)
    color_boton_inactivo = (75, 85, 99)
    color_input_activo = (251, 146, 60)
    
    reloj = pygame.time.Clock()
    velocidad = 0.01
    
    # Botones (Arriba)
    boton_reiniciar = pygame.Rect(ancho_max - 190, 20, 170, 45)
    boton_cambiar = pygame.Rect(ancho_max - 190, 75, 170, 45)
    boton_regresar = pygame.Rect(ancho_max - 190, 130, 170, 45)
    
    # --- NUEVO: 5 Botones de Escenarios (Abajo) ---
    y_botones_esc = alto - 60 # Movidos más abajo
    ancho_boton_esc = 160
    espacio_boton_esc = 20
    # Centrar los 5 botones
    ancho_total_botones = 5 * ancho_boton_esc + 4 * espacio_boton_esc
    x_inicio_botones = (ancho_max - ancho_total_botones) // 2
    
    boton_esc_a = pygame.Rect(x_inicio_botones, y_botones_esc, ancho_boton_esc, 45)
    boton_esc_b = pygame.Rect(x_inicio_botones + (ancho_boton_esc + espacio_boton_esc) * 1, y_botones_esc, ancho_boton_esc, 45)
    boton_esc_cbaja = pygame.Rect(x_inicio_botones + (ancho_boton_esc + espacio_boton_esc) * 2, y_botones_esc, ancho_boton_esc, 45)
    boton_esc_calta = pygame.Rect(x_inicio_botones + (ancho_boton_esc + espacio_boton_esc) * 3, y_botones_esc, ancho_boton_esc, 45)
    boton_esc_input = pygame.Rect(x_inicio_botones + (ancho_boton_esc + espacio_boton_esc) * 4, y_botones_esc, ancho_boton_esc, 45)

    # --- NUEVO: Estado del juego y Lógica del Formulario ---
    estado_juego = "SIMULACION" # "SIMULACION" o "INPUT_FORM"
    
    # Estructura para los datos del formulario
    input_data = [{"duracion": "1", "prioridad": "10"} for _ in range(10)]
    # Rects para cliquear en los inputs (se llenarán en el bucle)
    input_rects = {} 
    # (fila, tipo_columna) ej: (0, "duracion")
    active_input_box = None 
    boton_comenzar_form = pygame.Rect(ancho_max // 2 - 150, alto - 100, 300, 50)
    
    # Inicialización de estado
    (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
     tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, 
     escenario_actual) = reset_simulacion(algoritmo='dinamica', escenario_id="A")
    
    corriendo = True
    simulacion_terminada = False
    proceso_seleccionado = None
    tiempo_seleccion = 0
    
    # Ajuste de altura de fila para 10 procesos
    altura_fila_gantt = 40
    altura_barra_gantt = 35
    
    while corriendo:
        
        # --- NUEVO: Lógica de estado principal ---
        # El bucle de eventos se manejará de forma diferente
        
        mouse_pos = pygame.mouse.get_pos()
        
        # --- A. Bucle de Eventos (Manejado primero) ---
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                corriendo = False
            
            # --- A.1 Eventos del Formulario de Input ---
            if estado_juego == "INPUT_FORM":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # ¿Clic en el botón "Comenzar"?
                    if boton_comenzar_form.collidepoint(event.pos):
                        nuevo_esc_id = parsear_input_a_escenario(input_data)
                        (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
                         tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, 
                         escenario_actual) = reset_simulacion(algoritmo, factor_envejecimiento, nuevo_esc_id)
                        simulacion_terminada = False
                        proceso_seleccionado = None
                        estado_juego = "SIMULACION" # Volver a la simulación
                        active_input_box = None
                    else:
                        # ¿Clic en una caja de texto?
                        active_input_box = None # Desactivar por defecto
                        for (i, key), rect in input_rects.items():
                            if rect.collidepoint(event.pos):
                                active_input_box = (i, key)
                                break
                                
                if event.type == pygame.KEYDOWN:
                    if active_input_box:
                        i, key = active_input_box
                        current_text = input_data[i][key]
                        
                        if event.key == pygame.K_BACKSPACE:
                            input_data[i][key] = current_text[:-1]
                        elif event.unicode.isdigit() and len(current_text) < 2:
                            input_data[i][key] = current_text + event.unicode
                        elif event.key == pygame.K_TAB:
                            # Moverse con Tab (lógica simple)
                            idx, k = active_input_box
                            if k == "duracion":
                                active_input_box = (idx, "prioridad")
                            else:
                                if idx < 9:
                                    active_input_box = (idx + 1, "duracion")
                                else:
                                    active_input_box = (0, "duracion") # Volver al inicio
            
            # --- A.2 Eventos de la Simulación ---
            elif estado_juego == "SIMULACION":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    nuevo_escenario = None
                    # Botones superiores
                    if boton_reiniciar.collidepoint(event.pos):
                        (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
                         tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, 
                         escenario_actual) = reset_simulacion(algoritmo, factor_envejecimiento, escenario_actual)
                        simulacion_terminada = False
                        proceso_seleccionado = None
                        
                    elif boton_cambiar.collidepoint(event.pos):
                        nuevo_algoritmo = 'dinamica' if algoritmo == 'estatica' else 'estatica'
                        (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
                         tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, 
                         escenario_actual) = reset_simulacion(nuevo_algoritmo, factor_envejecimiento, escenario_actual)
                        simulacion_terminada = False
                        proceso_seleccionado = None
                    
                    elif boton_regresar.collidepoint(event.pos):
                        # Regresar al menú principal
                        pygame.quit()
                        import subprocess
                        import sys
                        subprocess.Popen([sys.executable, "menu_principal.py"])
                        return
                    
                    # Botones inferiores (Escenarios)
                    elif boton_esc_a.collidepoint(event.pos):
                        nuevo_escenario = "A"
                    elif boton_esc_b.collidepoint(event.pos):
                        nuevo_escenario = "B"
                    elif boton_esc_cbaja.collidepoint(event.pos):
                        nuevo_escenario = "C_BAJA"
                    elif boton_esc_calta.collidepoint(event.pos):
                        nuevo_escenario = "C_ALTA"
                    elif boton_esc_input.collidepoint(event.pos):
                        estado_juego = "INPUT_FORM" # Cambiar a la pantalla de formulario
                        active_input_box = (0, "duracion") # Activar la primera caja
                    
                    if nuevo_escenario:
                        (procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global,
                         tiempo_ejecucion_inicio, timeline, algoritmo, factor_envejecimiento, 
                         escenario_actual) = reset_simulacion(algoritmo, factor_envejecimiento, nuevo_escenario)
                        simulacion_terminada = False
                        proceso_seleccionado = None

        # --- B. Lógica de Dibujo ---
        
        # Gradiente de fondo (siempre se dibuja)
        for y in range(alto):
            factor = y / alto
            r = int(fondo_top[0] + (fondo_bottom[0] - fondo_top[0]) * factor)
            g = int(fondo_top[1] + (fondo_bottom[1] - fondo_top[1]) * factor)
            b = int(fondo_top[2] + (fondo_bottom[2] - fondo_top[2]) * factor)
            pygame.draw.line(ventana, (r, g, b), (0, y), (ancho_max, y))
            
        # --- B.1 Dibujar la Simulación ---
        if estado_juego == "SIMULACION":
            
            # Dibujar Botones Superiores
            color_boton = color_acento if not boton_reiniciar.collidepoint(mouse_pos) else color_acento_hover
            pygame.draw.rect(ventana, color_boton, boton_reiniciar, border_radius=8)
            texto_boton = fuente_bold.render("Reiniciar", True, (255, 255, 255))
            ventana.blit(texto_boton, (boton_reiniciar.x + 45, boton_reiniciar.y + 12))
            
            color_boton2 = color_acento if not boton_cambiar.collidepoint(mouse_pos) else color_acento_hover
            pygame.draw.rect(ventana, color_boton2, boton_cambiar, border_radius=8)
            texto_boton2 = fuente_bold.render("Cambiar Alg.", True, (255, 255, 255))
            ventana.blit(texto_boton2, (boton_cambiar.x + 30, boton_cambiar.y + 12))
            
            color_boton3 = (239, 68, 68) if not boton_regresar.collidepoint(mouse_pos) else (209, 58, 58)
            pygame.draw.rect(ventana, color_boton3, boton_regresar, border_radius=8)
            texto_boton3 = fuente_bold.render("Regresar", True, (255, 255, 255))
            ventana.blit(texto_boton3, (boton_regresar.x + 40, boton_regresar.y + 12))

            # Dibujar Botones de Escenarios (Inferiores)
            botones_esc = [
                {"rect": boton_esc_a, "id": "A", "texto": "Escenario A"},
                {"rect": boton_esc_b, "id": "B", "texto": "Escenario B"},
                {"rect": boton_esc_cbaja, "id": "C_BAJA", "texto": "Esc. C (Baja)"},
                {"rect": boton_esc_calta, "id": "C_ALTA", "texto": "Esc. C (Alta)"},
                {"rect": boton_esc_input, "id": "INPUT", "texto": "Personalizado"},
            ]
            
            for boton in botones_esc:
                # Comprobar si el ID es el personalizado temporal
                es_activo = (escenario_actual == boton["id"]) or \
                            (escenario_actual == "PERSONALIZADO_TEMP" and boton["id"] == "INPUT")
                            
                color_base = color_boton_activo if es_activo else color_boton_inactivo
                color = color_base
                if not es_activo and boton["rect"].collidepoint(mouse_pos):
                    color = color_acento_hover
                
                sombra = boton["rect"].copy(); sombra.y += 3
                pygame.draw.rect(ventana, (0, 0, 0, 80), sombra, border_radius=8)
                pygame.draw.rect(ventana, color, boton["rect"], border_radius=8)
                texto = fuente_boton_esc.render(boton["texto"], True, (255, 255, 255))
                ventana.blit(texto, (boton["rect"].x + (boton["rect"].width - texto.get_width()) // 2, boton["rect"].y + 13))

            # --- Lógica de Planificación (solo si no está en formulario) ---
            if proceso_seleccionado is None and ejecutando is None:
                nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                for p in nuevos:
                    if p not in en_cola: en_cola.append(p); pendientes.remove(p)
                
                if not en_cola and pendientes:
                    tiempo_global = round(pendientes[0]["llegada"])
                    nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                    for p in nuevos:
                        if p not in en_cola: en_cola.append(p); pendientes.remove(p)
            
            if ejecutando is None and en_cola and proceso_seleccionado is None:
                proceso_seleccionado = seleccionar_proceso_prioritario(en_cola, algoritmo)
                if proceso_seleccionado:
                    tiempo_seleccion = time.time()
                    idx = en_cola.index(proceso_seleccionado)
                    proceso_seleccionado["pos_inicial"] = (250 + idx * 130, 20)
            
            if proceso_seleccionado and time.time() - tiempo_seleccion > 0.8:
                ejecutando = proceso_seleccionado
                if ejecutando["inicio"] is None:
                    ejecutando["inicio"] = round(tiempo_global)
                    ejecutando["respuesta"] = ejecutando["inicio"] - ejecutando["llegada"]
                tiempo_ejecucion_inicio = round(tiempo_global)
                en_cola.remove(ejecutando)
                proceso_seleccionado = None
            
            # --- Dibujo de Paneles, Cola y Gantt ---
            tiempo_max_actual = 0
            for bloque in timeline: tiempo_max_actual = max(tiempo_max_actual, bloque["inicio"] + bloque["duracion"])
            if ejecutando: tiempo_max_actual = max(tiempo_max_actual, tiempo_ejecucion_inicio + (tiempo_global - tiempo_ejecucion_inicio))
            if proceso_seleccionado: tiempo_max_actual = max(tiempo_max_actual, tiempo_global + proceso_seleccionado["restante"])
            if pendientes or en_cola: tiempo_max_actual = max(tiempo_max_actual, tiempo_global + sum(p["restante"] for p in en_cola))
            if not pendientes and not en_cola and not ejecutando: tiempo_max_actual = max(tiempo_max_actual, tiempo_global)
            
            tiempo_max_actual = max(30, math.ceil(tiempo_max_actual)) 
            escala = (ancho_max - 150) / (tiempo_max_actual + 2)
            
            # Panel de cola de espera
            panel_cola = pygame.Rect(30, 10, ancho_max - 620, 130)
            s_panel = pygame.Surface((panel_cola.width, panel_cola.height), pygame.SRCALPHA); pygame.draw.rect(s_panel, (*color_panel, 230), s_panel.get_rect(), border_radius=12); ventana.blit(s_panel, panel_cola)
            titulo_cola = fuente_titulo.render("Cola de Listos", True, color_texto); ventana.blit(titulo_cola, (50, 25))
            
            # Panel de algoritmo
            panel_alg = pygame.Rect(ancho_max - 400, 10, 190, 110)
            s_panel_alg = pygame.Surface((panel_alg.width, panel_alg.height), pygame.SRCALPHA); pygame.draw.rect(s_panel_alg, (*color_panel, 230), s_panel_alg.get_rect(), border_radius=12); ventana.blit(s_panel_alg, panel_alg)
            alg_texto = f"Modo: {algoritmo.upper()}"; texto_alg = fuente_titulo.render(alg_texto, True, color_prioridad_alta if algoritmo == 'estatica' else color_prioridad_baja); ventana.blit(texto_alg, (ancho_max - 380, 25))
            if algoritmo == 'dinamica':
                env_texto = f"Envej.: {factor_envejecimiento}"; texto_env = fuente_small.render(env_texto, True, color_texto_secundario); ventana.blit(texto_env, (ancho_max - 380, 60))
            
            # Dibuja procesos en cola
            procesos_visibles = min(len(en_cola), 6)
            for i in range(procesos_visibles):
                p = en_cola[i]
                if proceso_seleccionado and p["id"] == proceso_seleccionado["id"]: continue
                rect_x = 250 + i * 130; rect_y = 20; rect = pygame.Rect(rect_x, rect_y, 110, 110)
                prioridad = p['prioridad_dinamica'] if algoritmo == 'dinamica' else p['prioridad_estatica']; color = obtener_color_prioridad(prioridad); dibujar_rectangulo_sombra(ventana, color, rect, radio=10)
                texto_id = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255)); tiempo_restante = math.ceil(p['restante']); texto_rest = fuente.render(f"{tiempo_restante}/{p['duracion']}s", True, (255, 255, 255)); texto_prior = fuente_small.render(f"Prior: {int(prioridad)}", True, (255, 255, 255)); texto_espera = fuente_small.render(f"Esp: {round(p['tiempo_espera'], 1)}", True, (255, 255, 255))
                ventana.blit(texto_id, (rect_x + 10, rect_y + 8)); ventana.blit(texto_rest, (rect_x + 10, rect_y + 35)); ventana.blit(texto_prior, (rect_x + 10, rect_y + 60)); ventana.blit(texto_espera, (rect_x + 10, rect_y + 85))
            if len(en_cola) > procesos_visibles:
                mas_texto = fuente_bold.render(f"+{len(en_cola) - procesos_visibles}", True, color_texto_secundario); ventana.blit(mas_texto, (250 + procesos_visibles * 130, 60))
            
            # Animación del proceso seleccionado (Ajuste de altura)
            if proceso_seleccionado:
                progreso = min((time.time() - tiempo_seleccion) / 0.8, 1.0)
                if progreso < 0.5: eased = 2 * progreso * progreso
                else: eased = 1 - pow(-2 * progreso + 2, 2) / 2
                x_inicial, y_inicial = proceso_seleccionado["pos_inicial"]; fila = proceso_seleccionado['id'] - 1; y_final = 180 + fila * altura_fila_gantt; x_final = 100 + int(tiempo_global * escala)
                x_actual = x_inicial + (x_final - x_inicial) * eased; arco = -100 * math.sin(eased * math.pi); y_actual = y_inicial + (y_final - y_inicial) * eased + arco
                escala_rect = 1.0 + 0.3 * math.sin(eased * math.pi); ancho_rect = int(110 * escala_rect); alto_rect = int(110 * escala_rect if eased < 0.5 else 110 * escala_rect * 0.5); rect_anim = pygame.Rect(int(x_actual), int(y_actual), ancho_rect, alto_rect)
                prioridad = proceso_seleccionado['prioridad_dinamica'] if algoritmo == 'dinamica' else proceso_seleccionado['prioridad_estatica']; color = obtener_color_prioridad(prioridad)
                for offset in [15, 10, 5]:
                    s_glow = pygame.Surface((ancho_rect + offset*2, alto_rect + offset*2), pygame.SRCALPHA); pygame.draw.rect(s_glow, (*color, int(20 * (1-progreso))), pygame.Rect(offset, offset, ancho_rect, alto_rect), border_radius=10); ventana.blit(s_glow, (int(x_actual) - offset, int(y_actual) - offset))
                dibujar_rectangulo_sombra(ventana, color, rect_anim, radio=10, sombra_offset=int(5 * escala_rect))
                texto_id = fuente_bold.render(f"P{proceso_seleccionado['id']}", True, (255, 255, 255)); ventana.blit(texto_id, (int(x_actual) + 10, int(y_actual) + 8))
            
            # Diagrama de Gantt (Ajuste de altura)
            y_gantt_start = 180
            for bloque in timeline:
                fila = bloque['id'] - 1; y_proceso = y_gantt_start + fila * altura_fila_gantt; x_inicio = 100 + bloque["inicio"] * escala; ancho_rect = bloque["duracion"] * escala; prioridad = bloque.get('prioridad', 5); color = obtener_color_prioridad(prioridad)
                rect = pygame.Rect(int(x_inicio), y_proceso, int(ancho_rect), altura_barra_gantt); dibujar_rectangulo_sombra(ventana, color, rect, radio=10, sombra_offset=3)
                if ancho_rect > 30:
                    texto_p = fuente_bold.render(f"P{bloque['id']}", True, (255, 255, 255)); ventana.blit(texto_p, (int(x_inicio) + 10, y_proceso + (altura_barra_gantt // 2) - 10))
                    texto_prior = fuente_small.render(f"Prior: {int(prioridad)}", True, (255, 255, 255)); ventana.blit(texto_prior, (int(x_inicio) + 10, y_proceso + (altura_barra_gantt // 2) + 5))
            
            # Proceso en ejecución (Ajuste de altura)
            if ejecutando:
                fila = ejecutando['id'] - 1; y_proceso = y_gantt_start + fila * altura_fila_gantt; x_inicio = 100 + tiempo_ejecucion_inicio * escala; tiempo_ejecutado = tiempo_global - tiempo_ejecucion_inicio; ancho_rect = tiempo_ejecutado * escala; prioridad = ejecutando['prioridad_dinamica'] if algoritmo == 'dinamica' else ejecutando['prioridad_estatica']; color = obtener_color_prioridad(prioridad)
                rect = pygame.Rect(int(x_inicio), y_proceso, max(int(ancho_rect), 1), altura_barra_gantt)
                alpha = int(128 + 127 * math.sin(tiempo_global * 3)); s_glow_surf_height = altura_barra_gantt + 4; s = pygame.Surface((max(int(ancho_rect), 1) + 8, s_glow_surf_height), pygame.SRCALPHA); pygame.draw.rect(s, (*color, alpha), pygame.Rect(4, 2, max(int(ancho_rect), 1), altura_barra_gantt), border_radius=10); ventana.blit(s, (int(x_inicio) - 4, y_proceso - 2))
                dibujar_rectangulo_sombra(ventana, color, rect, radio=10, sombra_offset=3)
                if ancho_rect > 30:
                    texto_p = fuente_bold.render(f"P{ejecutando['id']}", True, (255, 255, 255)); ventana.blit(texto_p, (int(x_inicio) + 10, y_proceso + (altura_barra_gantt // 2) - 10))
                    texto_prior = fuente_small.render(f"Prior: {int(prioridad)}", True, (255, 255, 255)); ventana.blit(texto_prior, (int(x_inicio) + 10, y_proceso + (altura_barra_gantt // 2) + 5))
            
            # Control de finalización de proceso
            if ejecutando:
                tiempo_ejecutado = tiempo_global - tiempo_ejecucion_inicio
                if tiempo_ejecutado >= 1.0:
                    prioridad_guardada = ejecutando['prioridad_dinamica'] if algoritmo == 'dinamica' else ejecutando['prioridad_estatica']
                    timeline.append({"id": ejecutando["id"], "inicio": tiempo_ejecucion_inicio, "duracion": round(tiempo_ejecutado, 1), "prioridad": prioridad_guardada})
                    ejecutando["restante"] -= round(tiempo_ejecutado, 1)
                    if ejecutando["restante"] < 0.1:
                        ejecutando["restante"] = 0; ejecutando["fin"] = round(tiempo_global); terminados.append(ejecutando); ejecutando = None
                    else:
                        nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                        for p in nuevos:
                            if p not in en_cola: en_cola.append(p); pendientes.remove(p)
                        if en_cola:
                            mejor_en_cola = seleccionar_proceso_prioritario(en_cola, algoritmo)
                            if algoritmo == 'estatica': debe_preemptar = mejor_en_cola['prioridad_estatica'] < ejecutando['prioridad_estatica']
                            else: debe_preemptar = mejor_en_cola['prioridad_dinamica'] < ejecutando['prioridad_dinamica']
                            if debe_preemptar:
                                en_cola.append(ejecutando); ejecutando = None
                            else: tiempo_ejecucion_inicio = round(tiempo_global)
                        else: tiempo_ejecucion_inicio = round(tiempo_global)
                    tiempo_global = round(tiempo_global)
            
            # Envejecimiento y actualización de tiempos de espera
            tick_visual = 0.02
            if proceso_seleccionado is None:
                if algoritmo == 'dinamica':
                    for p in en_cola: p['prioridad_dinamica'] = max(0, p['prioridad_dinamica'] - factor_envejecimiento * tick_visual); p['tiempo_espera'] += tick_visual
                else:
                    for p in en_cola: p['tiempo_espera'] += tick_visual
            
            # Línea de tiempo
            y_linea_tiempo = y_gantt_start + 10 * altura_fila_gantt + 20 # Mover línea de tiempo hacia abajo
            pygame.draw.line(ventana, color_texto_secundario, (100, y_linea_tiempo), (ancho_max - 50, y_linea_tiempo), 3)
            
            for t in range(int(tiempo_max_actual) + 1):
                if tiempo_max_actual > 60 and t % 5 != 0: continue
                if tiempo_max_actual > 30 and t % 2 != 0: continue
                x = 100 + t * escala
                pygame.draw.line(ventana, color_texto_secundario, (int(x), y_linea_tiempo-8), (int(x), y_linea_tiempo+8), 2)
                texto_t = fuente_small.render(str(t), True, color_texto); ventana.blit(texto_t, (int(x)-8, y_linea_tiempo+12))
            
            # Indicador de tiempo actual
            x_tiempo = 100 + tiempo_global * escala
            for offset in [6, 4, 2]:
                s_glow = pygame.Surface((offset*2, y_linea_tiempo - 140), pygame.SRCALPHA); pygame.draw.line(s_glow, (*color_linea_tiempo, 40), (offset, 0), (offset, y_linea_tiempo - 140), offset); ventana.blit(s_glow, (int(x_tiempo) - offset, 160))
            pygame.draw.line(ventana, color_linea_tiempo, (int(x_tiempo), 160), (int(x_tiempo), y_linea_tiempo), 3)
            pygame.draw.circle(ventana, color_linea_tiempo, (int(x_tiempo), y_linea_tiempo), 8); pygame.draw.circle(ventana, (255, 255, 255), (int(x_tiempo), y_linea_tiempo), 4)
            
            # Display del tiempo
            tiempo_texto = f"{round(tiempo_global, 1)}s"; texto_tiempo = fuente_tiempo.render(tiempo_texto, True, color_linea_tiempo); rect_tiempo = texto_tiempo.get_rect(center=(ancho_max//2, 150)); fondo_tiempo = rect_tiempo.inflate(40, 20)
            s_tiempo = pygame.Surface(fondo_tiempo.size, pygame.SRCALPHA); pygame.draw.rect(s_tiempo, (*color_panel, 200), s_tiempo.get_rect(), border_radius=15); ventana.blit(s_tiempo, fondo_tiempo); ventana.blit(texto_tiempo, rect_tiempo)
            
            # Panel de métricas
            if not pendientes and not en_cola and ejecutando is None:
                if not simulacion_terminada:
                    simulacion_terminada = True
                    if terminados: retorno, espera, respuesta, throughput = calcular_metricas(terminados)
                    else: retorno, espera, respuesta, throughput = 0, 0, 0, 0
                
                panel_x = 50
                panel_y = alto - 190 # Mover panel de métricas hacia arriba
                panel_w = 1600; panel_h = 110 # Hacerlo más pequeño
                s_panel_metricas = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA); pygame.draw.rect(s_panel_metricas, (*color_panel, 240), s_panel_metricas.get_rect(), border_radius=15); ventana.blit(s_panel_metricas, (panel_x, panel_y))
                titulo_metricas = fuente_titulo.render("Métricas de Rendimiento", True, color_texto); ventana.blit(titulo_metricas, (panel_x + 20, panel_y + 10))
                
                metricas = [("Prom. Retorno", f"{retorno:.2f}s"), ("Prom. Espera", f"{espera:.2f}s"), ("Prom. Respuesta", f"{respuesta:.2f}s"), ("Throughput", f"{throughput:.2f} p/s")]
                card_y = panel_y + 50; card_w = 360; card_h = 45; spacing = 30 # Tarjetas más pequeñas
                colores_card = [(255, 107, 107), (78, 205, 196), (255, 195, 113), (162, 155, 254)]
                
                for i, (nombre, valor) in enumerate(metricas):
                    card_x = panel_x + 30 + i * (card_w + spacing); card_rect = pygame.Rect(card_x, card_y, card_w, card_h)
                    pygame.draw.rect(ventana, colores_card[i], card_rect, 2, border_radius=8)
                    texto_nombre = fuente.render(nombre, True, color_texto_secundario); texto_valor = fuente_bold.render(valor, True, (255, 255, 255))
                    ventana.blit(texto_nombre, (card_x + 15, card_y + 12)); ventana.blit(texto_valor, (card_x + 160, card_y + 12))
            
            # Avance del tiempo continuo
            if proceso_seleccionado is None:
                if ejecutando: tiempo_global += tick_visual
                elif not ejecutando and not en_cola and pendientes:
                    if pendientes[0]['llegada'] > tiempo_global: tiempo_global += tick_visual
                    else: tiempo_global = pendientes[0]['llegada']
                elif not ejecutando and not en_cola and not pendientes:
                    if terminados: tiempo_global = max(p['fin'] for p in terminados)
                else: tiempo_global += tick_visual

        # --- B.2 Dibujar el Formulario de Input ---
        elif estado_juego == "INPUT_FORM":
            # Panel de fondo
            panel_form = pygame.Rect(50, 20, ancho_max - 100, alto - 40)
            s_form = pygame.Surface(panel_form.size, pygame.SRCALPHA)
            pygame.draw.rect(s_form, (*color_panel, 240), s_form.get_rect(), border_radius=15)
            ventana.blit(s_form, panel_form)
            
            titulo_form = fuente_titulo.render("Configurar Escenario Personalizado (Llegada = 0)", True, color_texto)
            ventana.blit(titulo_form, (panel_form.x + 40, panel_form.y + 30))
            
            # Headers
            header_dur = fuente_bold.render("Duración (1-99)", True, color_texto_secundario)
            header_pri = fuente_bold.render("Prioridad (0-10)", True, color_texto_secundario)
            ventana.blit(header_dur, (panel_form.x + 250, panel_form.y + 90))
            ventana.blit(header_pri, (panel_form.x + 450, panel_form.y + 90))

            input_rects.clear() # Limpiar rects para detección de clics
            y_fila = panel_form.y + 130
            for i in range(10):
                # Label Proceso
                texto_proc = fuente_bold.render(f"Proceso {i+1}:", True, color_texto)
                ventana.blit(texto_proc, (panel_form.x + 100, y_fila))
                
                # Input Duración
                rect_dur = pygame.Rect(panel_form.x + 250, y_fila - 5, 150, 40)
                input_rects[(i, "duracion")] = rect_dur
                
                # Input Prioridad
                rect_pri = pygame.Rect(panel_form.x + 450, y_fila - 5, 150, 40)
                input_rects[(i, "prioridad")] = rect_pri
                
                # Dibujar cajas
                for key, rect in [("duracion", rect_dur), ("prioridad", rect_pri)]:
                    es_activo = (active_input_box == (i, key))
                    color_borde = color_input_activo if es_activo else color_boton_inactivo
                    pygame.draw.rect(ventana, color_borde, rect, 2, border_radius=5)
                    
                    texto_input = fuente.render(input_data[i][key], True, color_texto)
                    ventana.blit(texto_input, (rect.x + 10, rect.y + 8))
                    
                    # Cursor parpadeante
                    if es_activo and int(time.time() * 2) % 2 == 0:
                        cursor_x = rect.x + texto_input.get_width() + 12
                        pygame.draw.line(ventana, color_texto, (cursor_x, rect.y + 8), (cursor_x, rect.y + 32), 2)
                
                y_fila += 55 # Siguiente fila
            
            # Dibujar Botón "Comenzar"
            color_comenzar = color_acento if not boton_comenzar_form.collidepoint(mouse_pos) else color_acento_hover
            pygame.draw.rect(ventana, color_comenzar, boton_comenzar_form, border_radius=8)
            texto_comenzar = fuente_titulo.render("Comenzar Simulación", True, (255, 255, 255))
            ventana.blit(texto_comenzar, (boton_comenzar_form.x + (boton_comenzar_form.width - texto_comenzar.get_width())//2, boton_comenzar_form.y + 10))

        # --- C. Actualizar Pantalla ---
        pygame.display.flip()
        reloj.tick(60)
        
        # Pausar la simulación de tiempo si estamos en el formulario
        if estado_juego == "SIMULACION":
            time.sleep(0.05 * velocidad)
    
    pygame.quit()

if __name__ == "__main__":
    simular_prioridades_visual() 