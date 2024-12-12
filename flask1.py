from flask import *

app=Flask(__name__)
app.config['SECRET_KEY']='secretkey'
@app.route('/')
def index():
    return render_template('template1.html')
@app.route('/register',methods=['POST','GET'])
def reg():
    if request.method == 'POST':
        session['Firstname']=request.form.get('Firstname')
        session['Lastname']=request.form.get('Lastname')
        print('redirecting to thank')
        return redirect(url_for('thank'))
    else:
        return render_template('template2.html')

@app.route('/thank',methods=['GET'])
def thank():
    print('thankyou')
    return render_template('thank.html')
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8000)
    