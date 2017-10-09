from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response")
def render_response():
    color = request.args['color'] # color is a key in args. it is the value set by name
    #args is request object. it is a dictionary but it can have multiple same keys; it is visible in url 
    if color == 'pink': # this is just color as a random ass variable name in python
        reply = "that's a good one; it's my pants' color"
    else
        reply = "your color sucks man"
    return render_template('response.html', response = reply)
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
