# Pong con `turtle` — cuaderno y juego

Versión extremadamente básica del **Pong** con la librería estándar `turtle`
de Python, pensada para clase.

- **`pong-turtle.ipynb`** — cuaderno explicativo paso a paso (ventana, palas,
  pelota y velocidad, controles, bucle principal y colisiones) con el código
  completo al final y retos de ampliación. Ábrelo directamente en Colab:

  [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/maximofernandezriera/pong-turtle/blob/main/pong-turtle.ipynb)

- **`pong.py`** — el juego completo (~100 líneas comentadas en castellano).

> `turtle` abre una ventana real: el juego se ejecuta en tu equipo
> (IDLE, Thonny, VS Code o terminal: `python3 pong.py`), no dentro de Colab.
> El cuaderno es la guía de lectura; el juego se copia y se ejecuta en local.

## Ejecutarlo en el navegador (sin instalar nada)

**Guía completa paso a paso:** [`GUIA-DE-USO.md`](GUIA-DE-USO.md)
(incluye solución de problemas y el checklist de despliegue del docente).
Resumen rápido:

### Opción A — GitHub Codespaces con escritorio web

Este repo incluye `.devcontainer/devcontainer.json` con escritorio Linux
accesible desde el navegador (noVNC):

1. En GitHub: **Code → Codespaces → Create codespace on main**
   (la primera vez tarda unos 3-5 min en construirse).
2. Cuando abra VS Code web, ve a la pestaña **PORTS**, busca el puerto
   **6080** ("Escritorio web") y abre la URL en otra pestaña.
3. En esa pestaña verás un escritorio Linux: contraseña **`vscode`**.
4. De vuelta en el terminal de VS Code, ejecuta:

   ```bash
   DISPLAY=:0 python3 pong.py
   ```

   La ventana del juego aparece **dentro del escritorio web** de la
   pestaña del puerto 6080. El teclado funciona ahí directamente.

### Opción B — Trinket (cero preparación)

1. Abre https://trinket.io → **New Trinket → Python**.
2. Pega el contenido de `pong.py` y pulsa **Run**: `turtle` corre en el
   propio navegador, ideal para alumnos sin cuenta de GitHub.

## Controles

- Jugador izquierdo: **W** (subir) / **S** (bajar)
- Jugador derecho: **↑** / **↓**

![Pong en ejecución](pong-captura.png)
