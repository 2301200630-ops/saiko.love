import os
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
# Ya no necesitamos cookies ni session, así que quitamos la clave secreta inestable

# --- TUS VERSOS ---
versos = [
    "Se me antoja estar contigo siempre y en cualquier momento.",
    "Se me antoja que se te antoje quererme tanto.",
    "Se me antoja recordar tus ojos viendo tu retrato.",
    "Se me antojan tantas cosas, ya no sé que es lo que quiero.",
    "Te regalo mi corazón, mejor no porque me muero.",
    "Se me antoja estar enamorado y llevarte en mi mente, sumergirte en este mar de besos y caricias.",
    "Solo te pido una noche, compárteme tus caricias."
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Gael 💕</title>
    <style>
        body {
            background-color: #fce4ec;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background-color: #fff5f7;
            border: 2px solid #ffb3c6;
            border-radius: 20px;
            padding: 40px 20px;
            width: 85%;
            max-width: 500px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(255, 179, 198, 0.3);
        }
        .ribbon {
            font-size: 35px;
            margin-bottom: 10px;
            color: #ff4d6d;
        }
        .title {
            color: #ff4d6d;
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 25px;
        }
        .verse-container {
            border: 1px dashed #ffb3c6;
            border-radius: 12px;
            padding: 30px 15px;
            margin-bottom: 25px;
            background-color: #fffdfd;
            min-height: 60px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .verse {
            color: #c9184a;
            font-size: 16px;
            line-height: 1.5;
            margin: 0;
        }
        .gif-container {
            margin-top: 15px;
        }
        .gif-container img {
            max-width: 150px;
            height: auto;
        }
        .btn {
            background-color: #ff4d6d;
            color: white;
            border: none;
            border-radius: 25px;
            padding: 12px 35px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 2px 5px rgba(255, 77, 109, 0.2);
            transition: background 0.2s;
            margin: 10px auto;
            display: block;
        }
        .btn:hover {
            background-color: #ff758f;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="ribbon">🎀</div>
        <div class="title">✨ Se me antoja - Kodigo 36 ✨</div>
        <div class="verse-container">
            <p class="verse">{{ verso }}</p>
            {% if es_ultimo %}
            <div class="gif-container">
                <img src="https://media.tenor.com/7S8fbeXo_68AAAAi/hello-kitty-crying.gif" alt="Hello Kitty Crying">
            </div>
            {% endif %}
        </div>
        
        {% if not es_ultimo %}
        <form action="{{ url_for('index') }}" method="GET">
            <input type="hidden" name="p" value="{{ siguiente_id }}">
            <button type="submit" class="btn">Siguiente ✨</button>
        </form>
        {% endif %}

        {% if es_ultimo %}
        <form action="{{ url_for('cerrar') }}" method="POST">
            <button type="submit" class="btn" onclick="window.close();">cerrar ❤️</button>
        </form>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    # Lee el número de página directamente desde el enlace
    try:
        current_index = int(request.args.get('p', 0))
    except ValueError:
        current_index = 0
        
    if current_index >= len(versos) or current_index < 0:
        current_index = 0
        
    verso_actual = versos[current_index]
    es_ultimo = (current_index == len(versos) - 1)
    siguiente_id = current_index + 1
    
    return render_template_string(
        HTML_TEMPLATE, 
        verso=verso_actual, 
        es_ultimo=es_ultimo, 
        siguiente_id=siguiente_id
    )

@app.route('/cerrar', methods=['POST'])
def cerrar():
    return """
    <script>
        window.close();
        document.write('<h2 style="color: #ff4d6d; text-align: center; font-family: sans-serif; margin-top: 50px;">¡Gracias por leer! Ya puedes cerrar esta pestañita, Te Amo Mi Amor. 💕</h2>');
    </script>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
