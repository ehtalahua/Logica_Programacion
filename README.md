# 🏓 Atari Pong — Recreación en Python con Pygame

## 📌 Nombre del Proyecto

**Atari Pong — Recreación Clásica en Python**

Versión funcional del mítico juego Pong de Atari (1972), desarrollada en Python usando la librería Pygame. El jugador controla una paleta con las teclas `W` y `S` y compite contra una CPU que sigue automáticamente la pelota.

---

## 👥 Integrantes

| Nombre completo | Rol |
|---|---|
| _(Tu nombre aquí)_ | Desarrollador Principal |
| _(Integrante 2)_ | _(Rol)_ |
| _(Integrante 3)_ | _(Rol)_ |

---

## 🎯 Objetivo del Sistema

Recrear el juego clásico Pong de forma funcional en Python, aplicando los fundamentos de programación con Pygame: manejo de eventos, detección de colisiones, movimiento de objetos, renderizado en pantalla y control del bucle de juego a 60 FPS.

### Objetivos específicos

- Implementar el movimiento de la pelota con rebote en paredes y paletas
- Controlar una paleta mediante teclado (`W` / `S`)
- Implementar una IA básica para la CPU que siga la posición de la pelota
- Mostrar el marcador en pantalla y actualizar puntos al anotar
- Mantener el juego a 60 FPS con `pygame.time.Clock`

---

## ⚙️ Descripción de Funcionalidades

| Funcionalidad | Descripción |
|---|---|
| **Movimiento del jugador** | Paleta izquierda controlada con `W` (arriba) y `S` (abajo) |
| **IA de la CPU** | Paleta derecha sigue automáticamente la posición de la pelota |
| **Física de la pelota** | Rebota en paredes superior/inferior y en ambas paletas |
| **Sistema de puntos** | Suma un punto al jugador o CPU cuando la pelota sale por los bordes |
| **Reinicio de pelota** | Al anotar un punto, la pelota regresa al centro de la pantalla |
| **Marcador en pantalla** | Se muestra el puntaje de Jugador y CPU centrado en la parte superior |
| **60 FPS** | El bucle está limitado a 60 fotogramas por segundo |

### Controles

| Tecla | Acción |
|---|---|
| `W` | Mover paleta hacia arriba |
| `S` | Mover paleta hacia abajo |
| Cerrar ventana | Salir del juego |

### Librería utilizada

```
pygame  →  Motor gráfico: ventana, eventos, dibujo y reloj del juego
sys     →  Salida del programa al cerrar la ventana
```

---

## 🏗️ Diagrama de Arquitectura

```
┌──────────────────────────────────────────┐
│             BUCLE PRINCIPAL              │
│              (60 FPS)                    │
│                                          │
│  ┌──────────┐   ┌──────────┐            │
│  │ Eventos  │   │ Teclado  │            │
│  │ (QUIT)   │   │ W / S    │            │
│  └────┬─────┘   └────┬─────┘            │
│       │              │                  │
│       ▼              ▼                  │
│  ┌─────────────────────────────────┐    │
│  │         LÓGICA DEL JUEGO        │    │
│  │                                 │    │
│  │  Paleta J  ←  Teclado           │    │
│  │  Paleta CPU ← posición pelota   │    │
│  │  Pelota    ← velocidad (vel_x,  │    │
│  │                         vel_y)  │    │
│  │                                 │    │
│  │  Colisiones:                    │    │
│  │    · Pared superior/inferior    │    │
│  │    · Paleta jugador             │    │
│  │    · Paleta CPU                 │    │
│  │                                 │    │
│  │  Puntuación:                    │    │
│  │    · bola_x <= 0  → CPU anota   │    │
│  │    · bola_x >= W  → J anota     │    │
│  └─────────────┬───────────────────┘    │
│                │                        │
│                ▼                        │
│  ┌─────────────────────────────────┐    │
│  │          RENDERIZADO            │    │
│  │  ventana.fill(NEGRO)            │    │
│  │  draw.rect  → paleta J          │    │
│  │  draw.rect  → paleta CPU        │    │
│  │  draw.circle → pelota           │    │
│  │  fuente.render → marcador       │    │
│  │  pygame.display.flip()          │    │
│  └─────────────────────────────────┘    │
└──────────────────────────────────────────┘
```

---

## 🔄 Diagrama de Flujo

```
        [Inicio]
            │
            ▼
    pygame.init() + ventana
            │
            ▼
    ┌───────────────┐
    │  BUCLE WHILE  │◄──────────────────────┐
    └───────┬───────┘                       │
            │                               │
            ▼                               │
    ¿Evento QUIT? ──── SÍ ──► pygame.quit() + sys.exit()
            │ NO
            ▼
    Leer teclas W/S → mover paleta_j
            │
            ▼
    CPU sigue pelota → paleta_cpu = bola_y
            │
            ▼
    Mover pelota (bola_x += vel_x, bola_y += vel_y)
            │
            ▼
    ¿Rebote en pared? ── SÍ ──► vel_y *= -1
            │ NO
            ▼
    ¿Rebote en paleta J? ── SÍ ──► vel_x *= -1
            │ NO
            ▼
    ¿Rebote en paleta CPU? ── SÍ ──► vel_x *= -1
            │ NO
            ▼
    ¿bola_x <= 0? ── SÍ ──► puntos_cpu += 1 → reiniciar pelota
            │ NO
            ▼
    ¿bola_x >= ANCHO? ── SÍ ──► puntos_j += 1 → reiniciar pelota
            │ NO
            ▼
    Dibujar todo en ventana
            │
            ▼
    pygame.display.flip()
            │
            ▼
    clock.tick(60) ──────────────────────────┘
```

---

## 🚀 Instalación y Ejecución

### Requisitos

- Python 3.8 o superior
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU_USUARIO/atari-pong.git
cd atari-pong

# 2. Instalar pygame
pip install pygame

# 3. Ejecutar el juego
python pong.py
```

---

## 📁 Estructura del Repositorio

```
atari-pong/
│
├── pong.py                  # Código fuente principal del juego
├── README.md                # Este archivo
│
└── diagramas/
    ├── arquitectura.png     # Diagrama de arquitectura del sistema
    └── flujo.png            # Diagrama de flujo del juego
```

---

## 🔮 Mejoras Futuras — Escalabilidad

El código actual es un punto de partida sólido. A continuación se listan las mejoras que se pueden implementar de forma progresiva:

### ✅ Corto plazo (bajo esfuerzo)

| Mejora | Descripción |
|---|---|
| **Ingreso de nombre** | Añadir un campo de texto en el menú para que el jugador escriba su nombre |
| **Pantalla de inicio** | Menú principal con instrucciones antes de comenzar |
| **Pantalla de fin** | Mostrar ganador cuando se llegue a X puntos |
| **Pausa** | Permitir pausar el juego con `ESC` |
| **Sonidos** | Usar `pygame.mixer` para efectos de rebote y punto |

### 🔧 Mediano plazo (refactorización)

| Mejora | Descripción |
|---|---|
| **Clases** | Convertir pelota y paletas en clases (`Pelota`, `Paleta`) para mejor organización |
| **Diccionario de config** | Centralizar velocidades, tamaños y colores en un `dict` o archivo `.json` |
| **Dificultad ajustable** | Niveles Fácil / Medio / Difícil cambiando la velocidad de la CPU |
| **Modo 2 jugadores** | Segundo jugador con teclas de flechas `↑` / `↓` |
| **Historial de partidas** | Guardar resultados en un archivo `scores.json` |

### 🚀 Largo plazo (funcionalidades avanzadas)

| Mejora | Descripción |
|---|---|
| **Base de datos** | Tabla de líderes persistente con SQLite |
| **Power-ups** | Objetos en pantalla que cambian tamaño de paleta o velocidad |
| **Efectos visuales** | Partículas al anotar, paletas con gradiente, fondo animado |
| **Modo online** | Multijugador en red con el módulo `socket` de Python |
| **Configuración visual** | Menú en pantalla para cambiar opciones sin editar el código |

---

## 📅 Fecha

| | |
|---|---|
| **Inicio del proyecto** | Mayo 14 2026 |
| **Versión actual** | v1.0 |
| **Última actualización** | Junio 28 2026 |

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT — libre para usar, modificar y distribuir con atribución.

---

> Proyecto académico de programación con Python y Pygame.
