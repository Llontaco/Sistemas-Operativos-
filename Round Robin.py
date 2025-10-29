import pygame
import time
import random
import math

ESCENARIOS = {
    "A": [
        {"id": 1, "llegada": 0, "duracion": 6, "inicio": None, "fin": None},
        {"id": 2, "llegada": 0, "duracion": 8, "inicio": None, "fin": None},
        {"id": 3, "llegada": 0, "duracion": 4, "inicio": None, "fin": None},
        {"id": 4, "llegada": 0, "duracion": 7, "inicio": None, "fin": None},
        {"id": 5, "llegada": 0, "duracion": 5, "inicio": None, "fin": None},
        {"id": 6, "llegada": 0, "duracion": 9, "inicio": None, "fin": None},
        {"id": 7, "llegada": 0, "duracion": 3, "inicio": None, "fin": None},
        {"id": 8, "llegada": 0, "duracion": 2, "inicio": None, "fin": None},
        {"id": 9, "llegada": 0, "duracion": 5, "inicio": None, "fin": None},
        {"id": 10, "llegada": 0, "duracion": 8, "inicio": None, "fin": None}
    ],
    
    "B": [
        {"id": 1, "llegada": 0, "duracion": 6, "inicio": None, "fin": None},
        {"id": 2, "llegada": 1, "duracion": 3, "inicio": None, "fin": None},
        {"id": 3, "llegada": 2, "duracion": 2, "inicio": None, "fin": None},
        {"id": 4, "llegada": 3, "duracion": 5, "inicio": None, "fin": None},
        {"id": 5, "llegada": 4, "duracion": 7, "inicio": None, "fin": None},
        {"id": 6, "llegada": 5, "duracion": 4, "inicio": None, "fin": None},
        {"id": 7, "llegada": 6, "duracion": 8, "inicio": None, "fin": None},
        {"id": 8, "llegada": 7, "duracion": 3, "inicio": None, "fin": None},
        {"id": 9, "llegada": 8, "duracion": 2, "inicio": None, "fin": None},
        {"id": 10, "llegada": 9, "duracion": 9, "inicio": None, "fin": None}
    ],
    
    "C_BAJA": [  # Baja concurrencia → llegadas separadas
        {"id": 1, "llegada": 0, "duracion": 5, "inicio": None, "fin": None},
        {"id": 2, "llegada": 5, "duracion": 3, "inicio": None, "fin": None},
        {"id": 3, "llegada": 10, "duracion": 7, "inicio": None, "fin": None},
        {"id": 4, "llegada": 15, "duracion": 4, "inicio": None, "fin": None},
        {"id": 5, "llegada": 20, "duracion": 6, "inicio": None, "fin": None},
        {"id": 6, "llegada": 25, "duracion": 8, "inicio": None, "fin": None},
        {"id": 7, "llegada": 30, "duracion": 3, "inicio": None, "fin": None},
        {"id": 8, "llegada": 35, "duracion": 9, "inicio": None, "fin": None},
        {"id": 9, "llegada": 40, "duracion": 2, "inicio": None, "fin": None},
        {"id": 10, "llegada": 45, "duracion": 5, "inicio": None, "fin": None}
    ],
    
    "C_ALTA": [  # Alta concurrencia → muchos llegan casi juntos
        {"id": 1, "llegada": 0, "duracion": 2, "inicio": None, "fin": None},
        {"id": 2, "llegada": 0, "duracion": 3, "inicio": None, "fin": None},
        {"id": 3, "llegada": 0, "duracion": 4, "inicio": None, "fin": None},
        {"id": 4, "llegada": 1, "duracion": 5, "inicio": None, "fin": None},
        {"id": 5, "llegada": 1, "duracion": 6, "inicio": None, "fin": None},
        {"id": 6, "llegada": 1, "duracion": 7, "inicio": None, "fin": None},
        {"id": 7, "llegada": 2, "duracion": 8, "inicio": None, "fin": None},
        {"id": 8, "llegada": 2, "duracion": 9, "inicio": None, "fin": None},
        {"id": 9, "llegada": 3, "duracion": 3, "inicio": None, "fin": None},
        {"id": 10, "llegada": 3, "duracion": 5, "inicio": None, "fin": None}
    ]
}


def generar_procesos(n=10, llegada_max=5, duracion_max=8):
    """
    Genera una lista de procesos con tiempos de llegada y duración aleatorios.
    
    Parámetros:
        n: Número de procesos a generar
        llegada_max: Tiempo máximo de llegada
        duracion_max: Duración máxima de un proceso
    
    Retorna:
        Lista de diccionarios con la información de cada proceso
    """
    procesos = []
    for i in range(1, n+1):
        llegada = random.randint(0, llegada_max)
        duracion = random.randint(1, duracion_max)
        procesos.append({
            "id": i, 
            "llegada": llegada, 
            "duracion": duracion, 
            "restante": duracion,
            "inicio": None, 
            "fin": None,
            "respuesta": None
        })
    return procesos

def crear_procesos_personalizado():
    """
    Interfaz para crear procesos personalizados manualmente.
    Permite ingresar llegada y duración de cada proceso.
    
    Retorna:
        Lista de procesos personalizados
    """
    pygame.init()
    ventana = pygame.display.set_mode((1700, 950))
    pygame.display.set_caption("Crear Procesos Personalizados")
    
    fuente = pygame.font.SysFont("Segoe UI", 16)
    fuente_titulo = pygame.font.SysFont("Segoe UI", 22, bold=True)
    fuente_input = pygame.font.SysFont("Segoe UI", 18)
    fuente_small = pygame.font.SysFont("Segoe UI", 14)
    
    color_fondo = (26, 32, 44)
    color_panel = (30, 41, 59)
    color_texto = (226, 232, 240)
    color_acento = (99, 102, 241)
    color_acento_hover = (79, 70, 229)
    color_input = (45, 55, 72)
    color_input_activo = (51, 65, 85)
    color_eliminar = (239, 68, 68)
    color_eliminar_hover = (220, 38, 38)
    
    procesos = []
    input_activo = None
    input_llegada = ""
    input_duracion = ""
    scroll_offset = 0
    max_scroll = 0
    
    # Botones
    boton_agregar = pygame.Rect(50, 720, 200, 50)
    boton_finalizar = pygame.Rect(450, 720, 200, 50)
    
    # Campos de input
    input_llegada_rect = pygame.Rect(250, 100, 150, 40)
    input_duracion_rect = pygame.Rect(250, 160, 150, 40)
    
    # Área de scroll para la lista de procesos
    lista_rect = pygame.Rect(50, 230, 600, 450)
    scroll_bar_rect = pygame.Rect(660, 230, 20, 450)
    
    arrastrando_scroll = False
    
    corriendo = True
    reloj = pygame.time.Clock()
    
    while corriendo:
        ventana.fill(color_fondo)
        
        # Título
        titulo = fuente_titulo.render("Crear Procesos Personalizados", True, color_texto)
        ventana.blit(titulo, (150, 30))
        
        # Labels
        label_llegada = fuente.render("Tiempo de llegada:", True, color_texto)
        ventana.blit(label_llegada, (50, 110))
        
        label_duracion = fuente.render("Duración:", True, color_texto)
        ventana.blit(label_duracion, (50, 170))
        
        # Campos de input
        color_llegada = color_input_activo if input_activo == "llegada" else color_input
        pygame.draw.rect(ventana, color_llegada, input_llegada_rect, border_radius=5)
        pygame.draw.rect(ventana, color_texto, input_llegada_rect, 2, border_radius=5)
        texto_llegada = fuente_input.render(input_llegada, True, color_texto)
        ventana.blit(texto_llegada, (input_llegada_rect.x + 10, input_llegada_rect.y + 10))
        
        color_duracion = color_input_activo if input_activo == "duracion" else color_input
        pygame.draw.rect(ventana, color_duracion, input_duracion_rect, border_radius=5)
        pygame.draw.rect(ventana, color_texto, input_duracion_rect, 2, border_radius=5)
        texto_duracion = fuente_input.render(input_duracion, True, color_texto)
        ventana.blit(texto_duracion, (input_duracion_rect.x + 10, input_duracion_rect.y + 10))
        
        # Panel de lista de procesos
        pygame.draw.rect(ventana, color_panel, lista_rect, border_radius=10)
        
        # Título de la lista
        label_lista = fuente.render(f"Procesos agregados ({len(procesos)}):", True, color_texto)
        ventana.blit(label_lista, (60, 235))
        
        # Crear superficie con scroll
        if len(procesos) > 0:
            # Calcular altura total necesaria
            altura_item = 35
            altura_total = len(procesos) * altura_item
            max_scroll = max(0, altura_total - (lista_rect.height - 50))
            
            # Crear superficie de contenido con scroll
            superficie_scroll = pygame.Surface((lista_rect.width - 40, altura_total))
            superficie_scroll.fill(color_panel)
            
            mouse_pos = pygame.mouse.get_pos()
            
            # Dibujar cada proceso con botón de eliminar
            for i, p in enumerate(procesos):
                y_item = i * altura_item
                
                # Rectángulo del proceso
                proceso_rect = pygame.Rect(10, y_item, superficie_scroll.get_width() - 90, 30)
                
                # Botón eliminar
                boton_eliminar = pygame.Rect(superficie_scroll.get_width() - 70, y_item, 60, 30)
                
                # Ajustar posición del mouse considerando scroll
                mouse_ajustado = (mouse_pos[0] - lista_rect.x - 10, mouse_pos[1] - lista_rect.y - 40 + scroll_offset)
                
                # Dibujar proceso
                color_proceso = (45, 55, 72)
                pygame.draw.rect(superficie_scroll, color_proceso, proceso_rect, border_radius=5)
                
                texto_proceso = fuente.render(f"P{p['id']}: Llegada={p['llegada']}, Duración={p['duracion']}", True, color_texto)
                superficie_scroll.blit(texto_proceso, (20, y_item + 5))
                
                # Dibujar botón eliminar
                color_btn_elim = color_eliminar_hover if boton_eliminar.collidepoint(mouse_ajustado) else color_eliminar
                pygame.draw.rect(superficie_scroll, color_btn_elim, boton_eliminar, border_radius=5)
                texto_elim = fuente_small.render("X", True, (255, 255, 255))
                superficie_scroll.blit(texto_elim, (boton_eliminar.x + 23, boton_eliminar.y + 5))
                
                # Guardar posición para detectar clicks (ajustado por scroll)
                p['_boton_eliminar'] = pygame.Rect(
                    lista_rect.x + boton_eliminar.x + 10,
                    lista_rect.y + boton_eliminar.y + 40 - scroll_offset,
                    boton_eliminar.width,
                    boton_eliminar.height
                )
            
            # Dibujar solo la parte visible
            ventana.blit(superficie_scroll, (lista_rect.x + 10, lista_rect.y + 40), 
                        (0, scroll_offset, lista_rect.width - 40, lista_rect.height - 50))
            
            # Barra de scroll
            if max_scroll > 0:
                # Fondo de la barra
                pygame.draw.rect(ventana, (60, 60, 80), scroll_bar_rect, border_radius=10)
                
                # Calcular tamaño y posición del thumb
                thumb_height = max(30, (lista_rect.height - 50) * (lista_rect.height - 50) / altura_total)
                thumb_y = scroll_bar_rect.y + (scroll_offset / max_scroll) * (scroll_bar_rect.height - thumb_height)
                thumb_rect = pygame.Rect(scroll_bar_rect.x, thumb_y, scroll_bar_rect.width, thumb_height)
                
                # Dibujar thumb
                color_thumb = (100, 116, 139) if not thumb_rect.collidepoint(mouse_pos) else (148, 163, 184)
                pygame.draw.rect(ventana, color_thumb, thumb_rect, border_radius=10)
        
        # Botones
        mouse_pos = pygame.mouse.get_pos()
        
        color_btn_agregar = color_acento if not boton_agregar.collidepoint(mouse_pos) else color_acento_hover
        pygame.draw.rect(ventana, color_btn_agregar, boton_agregar, border_radius=10)
        texto_agregar = fuente_titulo.render("Agregar", True, (255, 255, 255))
        ventana.blit(texto_agregar, (boton_agregar.x + 50, boton_agregar.y + 12))
        
        color_btn_fin = (34, 197, 94) if not boton_finalizar.collidepoint(mouse_pos) else (22, 163, 74)
        pygame.draw.rect(ventana, color_btn_fin, boton_finalizar, border_radius=10)
        texto_fin = fuente_titulo.render("Finalizar", True, (255, 255, 255))
        ventana.blit(texto_fin, (boton_finalizar.x + 45, boton_finalizar.y + 12))
        
        pygame.display.flip()
        reloj.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Click izquierdo
                    if input_llegada_rect.collidepoint(event.pos):
                        input_activo = "llegada"
                    elif input_duracion_rect.collidepoint(event.pos):
                        input_activo = "duracion"
                    elif lista_rect.collidepoint(event.pos):
                        input_activo = None
                        # Verificar si se clickeó un botón eliminar
                        for p in procesos:
                            if '_boton_eliminar' in p and p['_boton_eliminar'].collidepoint(event.pos):
                                procesos.remove(p)
                                # Reindexar IDs
                                for idx, proceso in enumerate(procesos):
                                    proceso['id'] = idx + 1
                                # Ajustar scroll si es necesario
                                altura_item = 35
                                altura_total = len(procesos) * altura_item
                                max_scroll = max(0, altura_total - (lista_rect.height - 50))
                                scroll_offset = min(scroll_offset, max_scroll)
                                break
                    elif scroll_bar_rect.collidepoint(event.pos) and max_scroll > 0:
                        arrastrando_scroll = True
                    else:
                        input_activo = None
                    
                    if boton_agregar.collidepoint(event.pos):
                        try:
                            llegada = int(input_llegada) if input_llegada else 0
                            duracion = int(input_duracion) if input_duracion else 1
                            if duracion > 0:
                                procesos.append({
                                    "id": len(procesos) + 1,
                                    "llegada": llegada,
                                    "duracion": duracion,
                                    "restante": duracion,
                                    "inicio": None,
                                    "fin": None,
                                    "respuesta": None
                                })
                                input_llegada = ""
                                input_duracion = ""
                                input_activo = "llegada"
                        except ValueError:
                            pass
                    
                    elif boton_finalizar.collidepoint(event.pos):
                        if len(procesos) > 0:
                            corriendo = False
                        else:
                            # Si no hay procesos, agregar uno por defecto
                            procesos.append({
                                "id": 1,
                                "llegada": 0,
                                "duracion": 5,
                                "restante": 5,
                                "inicio": None,
                                "fin": None,
                                "respuesta": None
                            })
                            corriendo = False
                
                elif event.button == 4:  # Scroll up
                    if lista_rect.collidepoint(event.pos):
                        scroll_offset = max(0, scroll_offset - 30)
                
                elif event.button == 5:  # Scroll down
                    if lista_rect.collidepoint(event.pos):
                        scroll_offset = min(max_scroll, scroll_offset + 30)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    arrastrando_scroll = False
            
            elif event.type == pygame.MOUSEMOTION:
                if arrastrando_scroll and max_scroll > 0:
                    # Calcular nueva posición del scroll
                    altura_item = 35
                    altura_total = len(procesos) * altura_item
                    thumb_height = max(30, (lista_rect.height - 50) * (lista_rect.height - 50) / altura_total)
                    
                    rel_y = event.pos[1] - scroll_bar_rect.y
                    scroll_ratio = rel_y / (scroll_bar_rect.height - thumb_height)
                    scroll_offset = max(0, min(max_scroll, scroll_ratio * max_scroll))
            
            elif event.type == pygame.KEYDOWN:
                if input_activo == "llegada":
                    if event.key == pygame.K_BACKSPACE:
                        input_llegada = input_llegada[:-1]
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_TAB:
                        input_activo = "duracion"
                    elif event.unicode.isdigit():
                        input_llegada += event.unicode
                
                elif input_activo == "duracion":
                    if event.key == pygame.K_BACKSPACE:
                        input_duracion = input_duracion[:-1]
                    elif event.key == pygame.K_RETURN:
                        try:
                            llegada = int(input_llegada) if input_llegada else 0
                            duracion = int(input_duracion) if input_duracion else 1
                            if duracion > 0:
                                procesos.append({
                                    "id": len(procesos) + 1,
                                    "llegada": llegada,
                                    "duracion": duracion,
                                    "restante": duracion,
                                    "inicio": None,
                                    "fin": None,
                                    "respuesta": None
                                })
                                input_llegada = ""
                                input_duracion = ""
                                input_activo = "llegada"
                        except ValueError:
                            pass
                    elif event.unicode.isdigit():
                        input_duracion += event.unicode
    
    return procesos

def cargar_escenario(escenario_key):
    """
    Carga un escenario predefinido.
    
    Parámetros:
        escenario_key: Clave del escenario ("A", "B", "C_BAJA", "C_ALTA")
    
    Retorna:
        Lista de procesos del escenario con campos adicionales
    """
    procesos = []
    for p in ESCENARIOS[escenario_key]:
        proceso = p.copy()
        proceso["restante"] = proceso["duracion"]
        proceso["respuesta"] = None
        procesos.append(proceso)
    return procesos

def reset_simulacion(quantum=3, escenario="A"):  # Cambia este valor para ajustar el quantum
    """
    Reinicia la simulación generando nuevos procesos y resetando el estado del sistema.
    
    Retorna:
        Tupla con todos los elementos necesarios para el estado inicial de la simulación
    """
    if escenario == "PERSONALIZADO":
        procesos = crear_procesos_personalizado()
        if procesos is None:
            procesos = cargar_escenario("A")
            escenario = "A"
    else:
        procesos = cargar_escenario(escenario)
    
    pendientes = sorted(procesos, key=lambda x: x["llegada"])
    terminados = []
    en_cola = []
    ejecutando = None
    tiempo_global = 0
    tiempo_ejecucion_inicio = 0
    timeline = []
    
    print("\n--- Nuevos procesos generados ---")
    print(f"Escenario: {escenario}")
    print(f"Quantum configurado: {quantum}")
    for p in procesos:
        print(f"ID: {p['id']}, Llegada: {p['llegada']}, Duración: {p['duracion']}")
    
    return procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario

def calcular_metricas(procesos):
    """
    Calcula las métricas de rendimiento del algoritmo Round Robin.
    
    Métricas calculadas:
        - Tiempo de retorno: Tiempo total desde que llega hasta que termina
        - Tiempo de espera: Tiempo que espera en cola
        - Tiempo de respuesta: Tiempo hasta que comienza su primera ejecución
        - Throughput: Número de procesos completados por unidad de tiempo
        - Fairness (índice de Jain): Mide la equidad en la distribución de tiempos de espera
    
    Parámetros:
        procesos: Lista de procesos completados con sus tiempos registrados
    
    Retorna:
        Tupla con las 5 métricas calculadas
    """
    n = len(procesos)
    retorno_total = 0
    espera_total = 0
    respuesta_total = 0
    tiempos_espera = []

    for p in procesos:
        retorno = p['fin'] - p['llegada']
        duracion_original = p['duracion']
        espera = retorno - duracion_original
        respuesta = p['respuesta'] if p['respuesta'] is not None else 0
        
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
    """
    Dibuja un rectángulo con efecto de sombra y brillo para simular profundidad.
    """
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

def simular_round_robin_visual():
    """
    Función principal que ejecuta la simulación visual del algoritmo Round Robin.
    
    Implementa el algoritmo Round Robin con visualización en tiempo real 
    del diagrama de Gantt y métricas de rendimiento.
    """
    pygame.init()
    ancho_max = 1700
    alto = 950
    ventana = pygame.display.set_mode((ancho_max, alto))
    pygame.display.set_caption("Algoritmo Round Robin")
    
    fuente = pygame.font.SysFont("Segoe UI", 18, bold=False)
    fuente_bold = pygame.font.SysFont("Segoe UI", 18, bold=True)
    fuente_titulo = pygame.font.SysFont("Segoe UI", 24, bold=True)
    fuente_tiempo = pygame.font.SysFont("Segoe UI", 32, bold=True)
    fuente_quantum = pygame.font.SysFont("Segoe UI", 18, bold=True)
    
    colores = [
        (255, 107, 107),  # Rojo coral
        (78, 205, 196),   # Turquesa
        (255, 195, 113),  # Naranja suave
        (162, 155, 254),  # Púrpura claro
        (255, 234, 167),  # Amarillo pastel
        (108, 92, 231),   # Índigo
        (255, 159, 243),  # Rosa
        (87, 242, 135)    # Verde menta
    ]
    
    fondo_top = (26, 32, 44)
    fondo_bottom = (45, 55, 72)
    
    color_panel = (30, 41, 59)
    color_texto = (226, 232, 240)
    color_texto_secundario = (148, 163, 184)
    color_acento = (99, 102, 241)
    color_acento_hover = (79, 70, 229)
    color_linea_tiempo = (251, 146, 60)
    color_quantum = (236, 72, 153)
    
    reloj = pygame.time.Clock()
    velocidad = 0.01

    boton_rect = pygame.Rect(ancho_max - 190, 20, 170, 45)
    
    # Botones de escenarios en la parte inferior
    boton_ancho = 220
    boton_alto = 50
    espacio_entre = 20
    total_ancho_botones = 4 * boton_ancho + 3 * espacio_entre
    inicio_x = (ancho_max - total_ancho_botones) // 2
    botones_y = alto - 80
    
    boton_escenario_a = pygame.Rect(inicio_x, botones_y, boton_ancho, boton_alto)
    boton_escenario_b = pygame.Rect(inicio_x + boton_ancho + espacio_entre, botones_y, boton_ancho, boton_alto)
    boton_escenario_c = pygame.Rect(inicio_x + 2 * (boton_ancho + espacio_entre), botones_y, boton_ancho, boton_alto)
    boton_personalizado = pygame.Rect(inicio_x + 3 * (boton_ancho + espacio_entre), botones_y, boton_ancho, boton_alto)
    boton_regresar = pygame.Rect(ancho_max - 230, alto - 80, 210, 50)
    
    # Submenú para Escenario C
    submenu_c_visible = False
    boton_c_baja = pygame.Rect(boton_escenario_c.x, boton_escenario_c.y - 70, 100, 30)
    boton_c_alta = pygame.Rect(boton_escenario_c.x + 110, boton_escenario_c.y - 70, 100, 30)

    # Inicialización con quantum personalizable
    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion()
    corriendo = True
    simulacion_terminada = False
    
    proceso_seleccionado = None
    tiempo_seleccion = 0
    
    # Variables para escala fija
    tiempo_max_escala = 10  # Empieza con una escala inicial
    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
    tiempo_max_actual = 0  # Inicializar aquí para evitar errores

    while corriendo:
        # Gradiente de fondo
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
        
        # Botón regresar
        color_regresar = (239, 68, 68) if not boton_regresar.collidepoint(mouse_pos) else (209, 58, 58)
        sombra_regresar = boton_regresar.copy()
        sombra_regresar.y += 3
        pygame.draw.rect(ventana, (0, 0, 0, 80), sombra_regresar, border_radius=8)
        pygame.draw.rect(ventana, color_regresar, boton_regresar, border_radius=8)
        texto_regresar = fuente_bold.render("Regresar", True, (255, 255, 255))
        ventana.blit(texto_regresar, (boton_regresar.x + 40, boton_regresar.y + 12))

        # Lógica Round Robin: Llegada de procesos
        if proceso_seleccionado is None and ejecutando is None:
            nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
            for p in nuevos:
                if p not in en_cola:
                    en_cola.append(p)
                    pendientes.remove(p)

            # Avance si no hay procesos listos
            if not en_cola and pendientes:
                tiempo_global = round(pendientes[0]["llegada"])
                nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                for p in nuevos:
                    if p not in en_cola:
                        en_cola.append(p)
                        pendientes.remove(p)

        # Selección del siguiente proceso (FIFO en Round Robin)
        if ejecutando is None and en_cola and proceso_seleccionado is None:
            proceso_seleccionado = en_cola[0]
            tiempo_seleccion = time.time()
            idx_en_cola = 0
            proceso_seleccionado["pos_inicial"] = (250 + idx_en_cola * 130, 20)
        
        # Después de animación, mover a ejecución
        if proceso_seleccionado and time.time() - tiempo_seleccion > 0.8:
            ejecutando = proceso_seleccionado
            if ejecutando["inicio"] is None:
                ejecutando["inicio"] = round(tiempo_global)
                ejecutando["respuesta"] = ejecutando["inicio"] - ejecutando["llegada"]
            tiempo_ejecucion_inicio = round(tiempo_global)
            en_cola.remove(ejecutando)
            proceso_seleccionado = None

        # Cálculo de escala dinámica - solo se reajusta cuando es necesario
        # Verificar si la barra de tiempo está cerca del borde (80% del ancho disponible)
        x_tiempo_actual = 100 + tiempo_global * escala
        ancho_disponible = ancho_max - 150
        
        # Calcular tiempo_max_actual siempre para evitar errores
        tiempo_max_actual = tiempo_global
        for bloque in timeline:
            tiempo_max_actual = max(tiempo_max_actual, bloque["inicio"] + bloque["duracion"])
        
        if ejecutando:
            tiempo_max_actual = max(tiempo_max_actual, tiempo_ejecucion_inicio + (tiempo_global - tiempo_ejecucion_inicio))
        
        if proceso_seleccionado:
            tiempo_estimado_seleccion = tiempo_global + min(quantum, proceso_seleccionado["restante"])
            tiempo_max_actual = max(tiempo_max_actual, tiempo_estimado_seleccion)
        
        if pendientes or en_cola:
            tiempo_estimado = tiempo_global
            procesos_restantes = len(en_cola) + len(pendientes)
            if procesos_restantes > 0:
                tiempo_estimado += quantum * procesos_restantes
            tiempo_max_actual = max(tiempo_max_actual, tiempo_estimado)
        
        # Si la barra está al 80% o más del espacio disponible, reajustar escala
        if x_tiempo_actual > ancho_disponible * 0.8 or (timeline and max((b["inicio"] + b["duracion"] for b in timeline), default=0) > tiempo_max_escala):
            # Agregar margen de expansión (20% más)
            tiempo_max_escala = math.ceil(tiempo_max_actual * 1.2)
            escala = (ancho_max - 150) / (tiempo_max_escala + 2)

        # Panel de cola de espera (más estrecho para evitar solapamiento)
        panel_cola = pygame.Rect(30, 10, ancho_max - 620, 85)
        s_panel = pygame.Surface((panel_cola.width, panel_cola.height), pygame.SRCALPHA)
        pygame.draw.rect(s_panel, (*color_panel, 230), s_panel.get_rect(), border_radius=12)
        ventana.blit(s_panel, panel_cola)
        
        titulo_cola = fuente_titulo.render("Cola de Espera", True, color_texto)
        ventana.blit(titulo_cola, (50, 25))

        # Panel de quantum (posición fija a la izquierda del botón)
        panel_quantum = pygame.Rect(ancho_max - 400, 10, 190, 85)
        s_panel_q = pygame.Surface((panel_quantum.width, panel_quantum.height), pygame.SRCALPHA)
        pygame.draw.rect(s_panel_q, (*color_panel, 230), s_panel_q.get_rect(), border_radius=12)
        ventana.blit(s_panel_q, panel_quantum)
        
        quantum_texto = f"Quantum: {quantum}s"
        texto_quantum = fuente_titulo.render(quantum_texto, True, color_quantum)
        ventana.blit(texto_quantum, (ancho_max - 380, 35))

        # Dibuja procesos en cola (limita el número visible para evitar desborde)
        procesos_visibles = min(len(en_cola), 7)  # Máximo 7 procesos visibles
        for i in range(procesos_visibles):
            p = en_cola[i]
            if proceso_seleccionado and p["id"] == proceso_seleccionado["id"]:
                continue
                
            rect_x = 250 + i * 130
            rect_y = 20
            rect = pygame.Rect(rect_x, rect_y, 110, 65)
            
            color = colores[p["id"] % len(colores)]
            dibujar_rectangulo_sombra(ventana, color, rect, radio=10)
            
            texto_id = fuente_bold.render(f"P{p['id']}", True, (255, 255, 255))
            # Redondear hacia arriba para mostrar correctamente el tiempo restante
            tiempo_restante = math.ceil(p['restante'])
            texto_rest = fuente.render(f"{tiempo_restante}/{p['duracion']}s", True, (255, 255, 255))
            ventana.blit(texto_id, (rect_x + 10, rect_y + 8))
            ventana.blit(texto_rest, (rect_x + 10, rect_y + 35))
        
        # Indicador de más procesos si hay overflow
        if len(en_cola) > procesos_visibles:
            mas_texto = fuente_bold.render(f"+{len(en_cola) - procesos_visibles}", True, color_texto_secundario)
            ventana.blit(mas_texto, (250 + procesos_visibles * 130, 40))
        
        # Animación del proceso seleccionado
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
            tiempo_restante = math.ceil(proceso_seleccionado['restante'])
            texto_rest = fuente.render(f"{tiempo_restante}s", True, (255, 255, 255))
            ventana.blit(texto_id, (int(x_actual) + 10, int(y_actual) + 8))
            ventana.blit(texto_rest, (int(x_actual) + 10, int(y_actual) + 35))

        # Diagrama de Gantt con bloques del timeline
        for bloque in timeline:
            fila = bloque['id'] - 1
            y_proceso = 130 + fila * 55
            x_inicio = 100 + bloque["inicio"] * escala
            # La duración se escala proporcionalmente
            ancho_rect = bloque["duracion"] * escala
            
            color = colores[bloque["id"] % len(colores)]
            rect = pygame.Rect(int(x_inicio), y_proceso, int(ancho_rect), 45)
            
            dibujar_rectangulo_sombra(ventana, color, rect, radio=10, sombra_offset=3)
            
            if ancho_rect > 30:
                texto_p = fuente_bold.render(f"P{bloque['id']}", True, (255, 255, 255))
                ventana.blit(texto_p, (int(x_inicio) + 10, y_proceso + 12))

        # Proceso en ejecución con efecto de pulso
        if ejecutando:
            fila = ejecutando['id'] - 1
            y_proceso = 130 + fila * 55
            x_inicio = 100 + tiempo_ejecucion_inicio * escala
            tiempo_ejecutado = tiempo_global - tiempo_ejecucion_inicio
            # El ancho es proporcional al tiempo ejecutado
            ancho_rect = tiempo_ejecutado * escala
            
            color = colores[ejecutando["id"] % len(colores)]
            rect = pygame.Rect(int(x_inicio), y_proceso, max(int(ancho_rect), 1), 45)
            
            alpha = int(128 + 127 * math.sin(tiempo_global * 3))
            s = pygame.Surface((max(int(ancho_rect), 1) + 8, 49), pygame.SRCALPHA)
            pygame.draw.rect(s, (*color, alpha), pygame.Rect(4, 2, max(int(ancho_rect), 1), 45), border_radius=10)
            ventana.blit(s, (int(x_inicio) - 4, y_proceso - 2))
            
            dibujar_rectangulo_sombra(ventana, color, rect, radio=10, sombra_offset=3)
            
            if ancho_rect > 30:
                texto_p = fuente_bold.render(f"P{ejecutando['id']}", True, (255, 255, 255))
                ventana.blit(texto_p, (int(x_inicio) + 10, y_proceso + 12))
        
        # Control de quantum y finalización
        if ejecutando:
            tiempo_ejecutado = tiempo_global - tiempo_ejecucion_inicio
            tiempo_restante_proceso = ejecutando["restante"]
            
            # Determinar cuánto tiempo debe ejecutarse (mínimo entre quantum y tiempo restante)
            tiempo_a_ejecutar = min(quantum, tiempo_restante_proceso)
            
            # Quantum expirado o proceso terminado
            if tiempo_ejecutado >= tiempo_a_ejecutar:
                # Redondear para evitar imprecisiones de punto flotante
                duracion_bloque = round(tiempo_ejecutado, 1)
                
                timeline.append({
                    "id": ejecutando["id"],
                    "inicio": tiempo_ejecucion_inicio,
                    "duracion": duracion_bloque
                })
                
                ejecutando["restante"] -= duracion_bloque
                
                # Usar un pequeño margen de tolerancia para considerar proceso terminado
                if ejecutando["restante"] < 0.1:
                    ejecutando["restante"] = 0
                    ejecutando["fin"] = round(tiempo_global)
                    terminados.append(ejecutando)
                else:
                    # Agregar procesos que llegaron durante la ejecución
                    nuevos = [p for p in pendientes if p["llegada"] <= tiempo_global]
                    for p in nuevos:
                        if p not in en_cola:
                            en_cola.append(p)
                            pendientes.remove(p)
                    
                    en_cola.append(ejecutando)
                
                ejecutando = None
                tiempo_global = round(tiempo_global)

        # Línea de tiempo
        y_linea = alto - 230
        pygame.draw.line(ventana, color_texto_secundario, (100, y_linea), (ancho_max - 50, y_linea), 3)
        
        # Dibujar marcadores solo hasta tiempo_max_escala
        for t in range(int(tiempo_max_escala) + 1):
            x = 100 + t * escala
            if x < ancho_max - 50:  # Solo dibujar si está dentro del área visible
                pygame.draw.line(ventana, color_texto_secundario, (int(x), y_linea-8), (int(x), y_linea+8), 2)
                texto_t = fuente.render(str(t), True, color_texto)
                ventana.blit(texto_t, (int(x)-8, y_linea+12))
        
        # Indicador de tiempo actual
        x_tiempo = 100 + tiempo_global * escala
        for offset in [6, 4, 2]:
            s_glow = pygame.Surface((offset*2, y_linea - 100), pygame.SRCALPHA)
            pygame.draw.line(s_glow, (*color_linea_tiempo, 40), (offset, 0), (offset, y_linea - 100), offset)
            ventana.blit(s_glow, (int(x_tiempo) - offset, 120))
        pygame.draw.line(ventana, color_linea_tiempo, (int(x_tiempo), 120), (int(x_tiempo), y_linea), 3)
        
        pygame.draw.circle(ventana, color_linea_tiempo, (int(x_tiempo), y_linea), 8)
        pygame.draw.circle(ventana, (255, 255, 255), (int(x_tiempo), y_linea), 4)

        # Display del tiempo
        tiempo_texto = f"{int(tiempo_global)}s"
        texto_tiempo = fuente_tiempo.render(tiempo_texto, True, color_linea_tiempo)
        rect_tiempo = texto_tiempo.get_rect(center=(ancho_max//2, 110))
        
        fondo_tiempo = pygame.Rect(rect_tiempo.x - 20, rect_tiempo.y - 10, rect_tiempo.width + 40, rect_tiempo.height + 20)
        s_tiempo = pygame.Surface((fondo_tiempo.width, fondo_tiempo.height), pygame.SRCALPHA)
        pygame.draw.rect(s_tiempo, (*color_panel, 200), s_tiempo.get_rect(), border_radius=15)
        ventana.blit(s_tiempo, fondo_tiempo)
        ventana.blit(texto_tiempo, rect_tiempo)

        # Panel de métricas
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
            
            titulo_metricas = fuente_titulo.render("Métricas de Rendimiento", True, color_texto)
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
        
        # Dibujar botones de escenarios en la parte inferior
        if not (not pendientes and not en_cola and ejecutando is None):
            mouse_pos = pygame.mouse.get_pos()
            
            # Botón Escenario A
            color_btn_a = color_acento if not boton_escenario_a.collidepoint(mouse_pos) else color_acento_hover
            if escenario_actual == "A":
                color_btn_a = (34, 197, 94)  # Verde si está activo
            pygame.draw.rect(ventana, color_btn_a, boton_escenario_a, border_radius=10)
            texto_btn_a = fuente_bold.render("Escenario A", True, (255, 255, 255))
            ventana.blit(texto_btn_a, (boton_escenario_a.x + 50, boton_escenario_a.y + 15))
            
            # Botón Escenario B
            color_btn_b = color_acento if not boton_escenario_b.collidepoint(mouse_pos) else color_acento_hover
            if escenario_actual == "B":
                color_btn_b = (34, 197, 94)
            pygame.draw.rect(ventana, color_btn_b, boton_escenario_b, border_radius=10)
            texto_btn_b = fuente_bold.render("Escenario B", True, (255, 255, 255))
            ventana.blit(texto_btn_b, (boton_escenario_b.x + 50, boton_escenario_b.y + 15))
            
            # Botón Escenario C
            color_btn_c = color_acento if not boton_escenario_c.collidepoint(mouse_pos) else color_acento_hover
            if escenario_actual in ["C_BAJA", "C_ALTA"]:
                color_btn_c = (34, 197, 94)
            pygame.draw.rect(ventana, color_btn_c, boton_escenario_c, border_radius=10)
            texto_btn_c = fuente_bold.render("Escenario C", True, (255, 255, 255))
            ventana.blit(texto_btn_c, (boton_escenario_c.x + 50, boton_escenario_c.y + 15))
            
            # Submenú de Escenario C
            if submenu_c_visible:
                # C Baja
                color_c_baja = (100, 116, 139) if not boton_c_baja.collidepoint(mouse_pos) else (71, 85, 105)
                pygame.draw.rect(ventana, color_c_baja, boton_c_baja, border_radius=8)
                texto_c_baja = fuente.render("C Baja", True, (255, 255, 255))
                ventana.blit(texto_c_baja, (boton_c_baja.x + 20, boton_c_baja.y + 7))
                
                # C Alta
                color_c_alta = (100, 116, 139) if not boton_c_alta.collidepoint(mouse_pos) else (71, 85, 105)
                pygame.draw.rect(ventana, color_c_alta, boton_c_alta, border_radius=8)
                texto_c_alta = fuente.render("C Alta", True, (255, 255, 255))
                ventana.blit(texto_c_alta, (boton_c_alta.x + 20, boton_c_alta.y + 7))
            
            # Botón Personalizado
            color_btn_per = color_acento if not boton_personalizado.collidepoint(mouse_pos) else color_acento_hover
            if escenario_actual == "PERSONALIZADO":
                color_btn_per = (34, 197, 94)
            pygame.draw.rect(ventana, color_btn_per, boton_personalizado, border_radius=10)
            texto_btn_per = fuente_bold.render("Personalizado", True, (255, 255, 255))
            ventana.blit(texto_btn_per, (boton_personalizado.x + 45, boton_personalizado.y + 15))
            
            # Botón Regresar
            color_btn_reg = (239, 68, 68) if not boton_regresar.collidepoint(mouse_pos) else (209, 58, 58)
            pygame.draw.rect(ventana, color_btn_reg, boton_regresar, border_radius=10)
            texto_btn_reg = fuente_bold.render("Regresar", True, (255, 255, 255))
            ventana.blit(texto_btn_reg, (boton_regresar.x + 50, boton_regresar.y + 12))

        pygame.display.flip()
        reloj.tick(60)
        
        # Avance del tiempo continuo
        if proceso_seleccionado is None:
            tiempo_global += 0.02
            if tiempo_global > tiempo_max_actual and not pendientes and not en_cola and ejecutando is None:
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
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, escenario_actual)
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    # Resetear la escala
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False
                
                # Botones de escenarios
                elif boton_escenario_a.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, "A")
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False
                
                elif boton_escenario_b.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, "B")
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False
                
                elif boton_escenario_c.collidepoint(event.pos):
                    # Toggle del submenú
                    submenu_c_visible = not submenu_c_visible
                
                elif submenu_c_visible and boton_c_baja.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, "C_BAJA")
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False
                
                elif submenu_c_visible and boton_c_alta.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, "C_ALTA")
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False
                
                elif boton_personalizado.collidepoint(event.pos):
                    procesos, pendientes, terminados, en_cola, ejecutando, tiempo_global, tiempo_ejecucion_inicio, timeline, quantum, escenario_actual = reset_simulacion(quantum, "PERSONALIZADO")
                    simulacion_terminada = False
                    proceso_seleccionado = None
                    tiempo_max_escala = 10
                    escala = (ancho_max - 150) / (tiempo_max_escala + 2)
                    submenu_c_visible = False

    pygame.quit()

if __name__ == "__main__":
    simular_round_robin_visual()