from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENCODE_API_KEY'),
    base_url='https://opencode.ai/zen/go/v1',
    )

def get_car_ai_bio(model, brand, year):

    prompt = f'''
    Crie uma descrição de venda para o veículo
    {brand} {model} {year}.

    Requisitos:
    - máximo de 250 caracteres;
    - destaque especificações técnicas desse modelo;
    - use linguagem comercial;
    - não invente características.
    '''

    prompt = prompt.format(brand, model, year)
    response = client.chat.completions.create(
        model = 'kimi-k3',
        messages=[
            {
                'role':'user',
                'content':prompt
            }
        ],
        max_tokens=1000,
        reasoning_effort='low',
    )
    descricao = response.choices[0].message.content
    return descricao[:250]