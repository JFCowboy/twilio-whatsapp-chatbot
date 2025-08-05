# twilio-whatsapp-chatbot

# 🚀 FastAPI + Twilio + OpenAI en GitHub Codespaces

Este proyecto es un ejemplo del uso del API de whatsapp por medio de **Twilio**, esta construida con **FastAPI**, que se ejecuta fácilmente en **GitHub Codespaces**, e integra funcionalidades de **Twilio** (para enviar mensajes por whatsapp) y **OpenAI** (para consultas a modelos GPT).

---

## 🧰 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [Twilio SDK](https://www.twilio.com/docs/whatsapp/quickstart/python)
- [OpenAI API](https://platform.openai.com/)
- [GitHub Codespaces](https://github.com/features/codespaces)
- Python 3.7+

---

## 🚀 ¿Cómo empezar?

### 1. Crea un Codespace

Haz clic en el botón verde **"Code"** y selecciona **"Create codespace on main"**.

> Esto descargará e instalará automáticamente las dependencias gracias a la configuración de `.devcontainer`.

### 2. Ejecuta el servidor

Una vez dentro del Codespace, corre el siguiente comando en la terminal:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

