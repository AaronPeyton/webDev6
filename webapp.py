from flask import Flask, url_for, render_template, request

app = Flask(__name__)
#__name__ = "__main__" if this is the file that was run.
#Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index.html')

@app.route("/add")
def render_add():
    return render_template('addition.html')

@app.route("/mult")
def render_mult():
    return render_template('multiplication.html')

@app.route("/hex")
def render_hex():
    return render_template('toHex.html')


@app.route("/response")
def render_response():
    if 'add1' in request.args and 'add2' in request.args:
        if request.args['add1'] != null and  request.args['add2'] != null:
            reply = float(request.args['add1']) + float(request.args['add2'])
        else:
            reply = "null"
    elif 'mult1' in request.args and 'mult2' in request.args
        if request.args['mult1'] != null and  request.args['mult2'] != null:
            reply = float(request.args['mult1']) * float(request.args['mult2'])
        else:
            reply = "null"
    elif 'hex' in request.args:
        if request.args['hex'] != null:
            reply = format(int(request.args['hex']),'x')
        else:
            reply = "null"
    else:
      reply = "i really dunno dude"
    # reply = "ahhhhhh. work!"
    return render_template('response.html', response = reply)

if __name__=="__main__":
    app.run(debug=False, port=54321)
