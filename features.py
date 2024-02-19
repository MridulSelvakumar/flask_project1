from flask import Flask


FAI=Flask(__name__)

@FAI.route('/flask')
def flask():
    return 'hlo mridul'


if __name__=='__main__':
    FAI.run(debug=True)
