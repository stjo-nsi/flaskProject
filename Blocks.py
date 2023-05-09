@app.route('/variables'methods = ['GET'])
def fonction_variables():  # put application's code here
    resultat = request.args
    monprenom = resultat['prenom']
    monnom = resultat['nom']
    reponse = monprenom + "" + monnom
    return 'Hello %s' %reponse
