from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return redirect ('/4')

@app.route('/4')
def ajedrez4_8():
    return render_template('index.html', x=4, y=8, color1="red", color2="beige")


@app.route('/<int:cantidad>/<int:cantidad2>')
def ajedrez_x_y(cantidad, cantidad2):

    return render_template(f'index.html', x = cantidad, y = cantidad2, color1 = "red", color2 = "blue")

@app.route('/<int:cantidad>/<int:cantidad2>/<color1>/<color2>')
def ajedrez_x_y_color(cantidad,cantidad2,color1,color2):
    return render_template(f'index.html',x=cantidad, y=cantidad2, color1=color1, color2=color2)



if __name__=="__main__":
    app.run(debug=True)