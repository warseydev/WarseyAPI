from flask import Flask, request, redirect, send_file, render_template
from waitress import serve
import io, os
import designer

app = Flask(__name__)

if os.path.exists("./tmp") != True:
    os.mkdir("./tmp") 

@app.route("/api/design/tshirt")
def tshirt():
    text = request.args.get('text')
    template = request.args.get('template')
    rgb1 = request.args.get('rgb1')
    rgb2 = request.args.get('rgb2')
    rgb3 = request.args.get('rgb3')
    if text == None or template == None:
        return send_file("errors/error.webp")
    if "." in template or "/" in template: 
        return send_file("errors/error.webp")
    if len(text) > 16:
        return send_file("errors/max.webp")
    formattedtext = text.replace(' ', '')
    formattedtext = formattedtext.replace('.', '')
    if formattedtext.isalpha() != True:
        return send_file("errors/alpha.webp")
    try:
        filename = tdesign.create(template, text, rgb1, rgb2, rgb3)
    except:
       return send_file("errors/error.webp")
    return send_file(f"tmp/{filename}.jpg", mimetype='image/jpeg', download_name="warsey-tshirt.jpg", as_attachment=True)
    

@app.errorhandler(404)
def not_found(e):
    return """<meta http-equiv="Refresh" content="0; url='https://warsey.com'"/>"""

@app.errorhandler(500)
def internal_error(error):
    return send_file("errors/500.webp")

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)