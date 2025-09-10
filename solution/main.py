from fastapi import FastAPI, Form, Request
import openai
from decouple import config

from utils import send_message, logger


app = FastAPI()
# Set up the OpenAI API client
openai_client = openai.OpenAI(api_key=config("OPENAI_API_KEY"))


menu = '''
👋🏽 ¡Qué más pues, ve! Bienvenido a Las delicias de Juan Manuel, Sazón Caleña 🇨🇴🍽️

¡Qué alegría tenerte por aquí! Te habla Juan Manuel, el rincón donde la buena comida y la alegría del Valle se juntan pa' consentirte el paladar. 💃🏽🎶

Te dejo nuestro Menú pa' que escojas lo que se te antoje.

🥘 Platos Fuertes
 1. Sancocho de gallina – con arroz, yuca y aguacate 🥑
 2. Chuleta valluna – con arroz, tajadas y ensalada 🐖
 3. Arroz atollado – con pollo, cerdo y chorizo 🐓🐷
🥟 Picaditas
 4. Empanadas vallunas – con ají casero
 5. Marranitas – plátano verde relleno de chicharrón
 6. Aborrajados – plátano maduro con queso

🍹 Bebidas
 7. Lulada bien fría 🍋
 8. Champús caleño 🍍
 9. Jugo de borojó con leche 💪🏽

🍮 Postres
 10. Manjar blanco con brevas
 11. Arroz con leche y canela
 12. Gelatina de pata
'''

@app.get("/")
async def index():
    return {"msg": "up & running"}

@app.post("/menus")
async def send_menu(request: Request, Body: str = Form()):
    logger.info(f"message received: {Body}")
    form_data = await request.form()
    to_number = form_data['From'].replace('whatsapp:', '')
    send_message(to_number, menu)
    return {"msg": "Menu sent"}

@app.post("/helps")
async def comunicate_with_waiter(request: Request, Body: str = Form()):
    form_data = await request.form()
    to_number = form_data['From'].replace('whatsapp:', '')
    
    # Call the OpenAI API to generate text with ChatGPT
    messages = [{"role": "user", "content": Body},
                {"role": "system", "content": "Eres un asistente 'caleño' de servicio al cliente que ayuda a los clientes a comunicarse con el restaurante. Responde de manera concisa, divertida y muy caleña."}]
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
     
    # The generated text
    chat_response = response.choices[0].message.content.strip()
    logger.info(f"ChatGPT response: {chat_response}")
    send_message(to_number, chat_response)
    # send_message(to_number, "Un cliente ha solicitado la ayuda de un mesero. Por favor, atiéndelo lo antes posible.")