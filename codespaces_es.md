# Lanzar un Codespace

**GitHub Codespaces** es un entorno de desarrollo en el navegador que puedes usar para realizar los ejercicios de esta charla sin necesidad de instalar nada en tu máquina local. Este documento `codespaces_es.md` explica cómo lanzar y configurar el entorno de Codespaces.

Para lanzar un Codespace, haz clic en el botón verde **"Code"** en la parte superior derecha del repositorio (a la izquierda de la barra lateral derecha). Luego ve a la pestaña **Codespaces** (si no está seleccionada) y haz clic en el ícono **+**.

![1 — Lanzar Codespace](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/1-launch-codespace.png)

Esto abrirá una nueva pestaña con una interfaz similar a VSCode. Puede tardar hasta un minuto en cargarse completamente, durante ese tiempo verás "Opening Remote…" en la esquina inferior izquierda.

![2 — Cargando Codespace](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/2-loading-codespace.png)

Una vez cargado, el Codespace mostrará el archivo `README` del repositorio en los dos tercios superiores de la pantalla.

Hay dos cosas que deberías hacer antes de comenzar: abrir la interfaz Web (Web UI) y abrir algunas terminales de trabajo.

---

### Abrir más Terminales de Trabajo

Para abrir terminales de trabajo adicionales, regresa a la pestaña del Codespace y haz clic en **"TERMINAL"**.

![7 — Pestaña Terminal](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/7-terminal-tab.png)

Deberías ver la opción **"bash"** en la barra lateral derecha. Haz clic en **"bash"** para abrir una terminal de trabajo:

![8 — Terminal Bash](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/8-bash-terminal.png)

Para crear más terminales (normalmente necesitarás 2 o 3), haz clic en la flecha desplegable al lado del ícono **“+”** (encima donde dice “bash”), y en el menú desplegable selecciona **"Split Terminal"** y luego **"bash (Default)"**.

![9 — Dividir Terminal](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/9-split-terminal.png)

Repite este proceso hasta tener el número de terminales que necesites:

![10 — Terminales de Trabajo](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/10-working-terminals.png)

---

Tu Codespace se detendrá automáticamente 30 minutos después de cerrar la pestaña del navegador. Esto evita el uso excesivo de recursos. Puedes reanudarlo desde la misma interfaz de GitHub, siempre y cuando no hayan pasado más de 30 días desde la última vez que lo usaste.

![12 — Reanudar Codespace](https://raw.githubusercontent.com/temporalio/temporal-learning/refs/heads/main/static/courses/common/codespaces/12-resume-codespace.png)

---

### Eliminar tus Codespaces

Una vez termines la charla o los ejercicios, elimina manualmente tus Codespaces. Mantener Codespaces guardados tiene un costo, por lo que es recomendable borrar los que ya no necesites. Sigue estos pasos:

1. Visita tu página de Codespaces: [github.com/codespaces](https://github.com/codespaces)
2. A la derecha del Codespace que deseas eliminar, haz clic en los tres puntos `⋯` y luego selecciona `Delete`:

![Eliminar Codespace](https://learn.temporal.io/courses/common/codespaces/13-delete-codespaces.png "Eliminar Codespace")