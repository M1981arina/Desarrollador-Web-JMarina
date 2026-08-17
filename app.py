from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")
# route for alcaldia
@app.route('/alcaldia')
def alcaldia():
    return render_template("alcaldia.html")
# route for municipio
@app.route('/municipio')    
def municipio():
    return render_template("municipio.html")   
# route for obras
@app.route('/obras')
def obras():
    return render_template("obras.html")
# route for obras por registrar 
@app.route('/obras_por_registrar') 
def obras_por_registrar():
    return render_template("obras_por_registrar.html")
# route for noticias
@app.route('/noticias')         
def noticias():
    return render_template("noticias.html")
# route for tramites
@app.route('/tramites')
def tramites():
    return render_template("tramites.html")
# route for servicios                                   
@app.route('/servicios')
def servicios():
    return render_template("servicios.html")
# route for turismo
@app.route('/turismo')
def turismo():
    return render_template("turismo.html")
# route for contactos
@app.route('/contactos')
def contactos():
    return render_template("contactos.html")
if __name__ == '__main__':
    app.run(debug=True)
