from flask import Flask, request, render_template, redirect, url_for
 
app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Firstname = request.form['Firstname']
        return redirect(url_for('thank',Firstname=Firstname))
    else:
        return render_template('login.html')
@app.route('/<Firstname>',methods=['GET'])
def thank(Firstname):
    request.args.get=Firstname
    return render_template('thank.html')

 
if __name__ == '__main__':
    app.run(debug=True)