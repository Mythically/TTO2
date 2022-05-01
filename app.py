from flask import Flask, render_template, jsonify, request, json, redirect
import challonge, pprint, siteDB

my_user = "TheMythh"
my_api_key = "KpgOkCV50nJ4nWrIPEwj5dwT71yRVvWcM7SueADm"
challonge.set_credentials(my_user, my_api_key)

app = Flask(__name__, static_folder='static', template_folder="templates")


@app.route("/matches")
def get_matches():
    get_matches = challonge.matches.index(11108882)
    pprint.pprint(get_matches)
    return jsonify(get_matches)


@app.route("/get_participants")
def get_participants():
    get_participants = challonge.participants.index(11108882)
    pprint.pprint(get_participants)
    return jsonify(get_participants)


@app.route('/get_tourn')
def get_tourn():  # put application's code here
    tourneys = challonge.tournaments.index()
    pprint.pprint(tourneys)
    # pprint.pprint(tourneys)
    return jsonify(tourneys)


# @app.route("/setcookie", methods=['POST'])
# def setcookie():


@app.route("/login", methods=['POST'])
def loggedIn():
    username = request.form.get('userame')
    password = request.form.get('password')
    print(username, password)
    if siteDB.checkLogin(username, password):
        return redirect('/')
    else:
        return render_template("login.html")


@app.route("/register", methods=['GET, POST'])
def register():
    username = request.form.get('userame')
    password = request.form.get('password')
    print(username, password)
    if siteDB.insertLogin(username, password):
        return redirect('/')
    else:
        return render_template("login.html")

a
@app.route('/')
def return_index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
