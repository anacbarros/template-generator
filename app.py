from flask import Flask, render_template, request
import pdfkit
from io import BytesIO
from flask import send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generate', methods=['POST'])
def generate():
    nome = request.form.get('nome')
    cargo = request.form.get('cargo')
    etapa = request.form.get('etapa')

    template_content = f"""
    Prezado(a) {nome},

    Agradecemos seu interesse na posição de {cargo}. Queremos informar que você está na etapa de {etapa}.
    
    Atenciosamente,
    Equipe de Recrutamento
    """

    pdf = pdfkit.from_string(template_content, False)
    return send_file(BytesIO(pdf), download_name="template.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
