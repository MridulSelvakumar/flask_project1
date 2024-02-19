from flask import Flask,render_template


FAI=Flask(__name__)

@FAI.route('/flask')
def flask():
    return render_template('flask.html',name='Dhoni')


@FAI.route('/flask_html')
def flask_html():
    return render_template('flask_html.html')    


if __name__=='__main__':
    FAI.run(debug=True)
