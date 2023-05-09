from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('formulaire.html')

@app.route('/test')
def fonction_test():  # put application's code here
    return 'Hello test'

@app.route('/variable/<prenom>')
def fonction_variable(prenom):  # put application's code here
    return 'Hello %s' %prenom

@app.route('/variables', methods = ['GET'])
def fonction_variables():  # put application's code here
    resultat = request.args
    monprenom = resultat['prenom']
    monnom = resultat['nom']
    return 'Hello {}-{}'.format(monprenom, monnom)

@app.route('/formulaire', methods = ['POST'])
def fonction_formulaire():  # put application's code here
    monprenom = request.form.get("prenom")
    monnom = request.form.get("nom")
    return render_template('reponse_formulaire.html',nom=monnom,prenom=monprenom)

if __name__ == '__main__':
    app.run()
