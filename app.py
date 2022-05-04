from flask import Flask, render_template, jsonify, request, json, redirect, session
import challonge, pprint, siteDB, queryAPI

my_user = "TheMythh"
my_api_key = "KpgOkCV50nJ4nWrIPEwj5dwT71yRVvWcM7SueADm"
challonge.set_credentials(my_user, my_api_key)
app = Flask(__name__, static_folder='static', template_folder="templates")
loggedIn = "False"


@app.route("/create")
def create_trounament():
    return render_template("create.html")


@app.route("/brackets", methods=['POST'])
def drawBrackets():
    idt = request.form.get('show')
    data = queryAPI.getMatches(idt)
    titles = queryAPI.titles
    return render_template("brackets.jinja2", data=data, titles=titles)


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
    info = []
    tournaments = challonge.tournaments.index()

    for tournament in tournaments:
        # print(tournament['id'])
        info.append({
            'id': tournament['id'],
            'name': tournament['name'],
            'participants': tournament['participants_count'],
            'description': tournament['description']
        })
    # print(info)
    # print(jsonify(info))
    return jsonify(info)


@app.route("/logout")
def logout():
    global loggedIn
    loggedIn = "False"
    return redirect("/login")


@app.route("/login", methods=['GET', 'POST'])
def loggedIn():
    global loggedIn
    if loggedIn == "True":
        return redirect("/")
    # print(request.form.get('username'), request.form.get('password'))
    if request.form.get('username') and request.form.get('password'):
        username = request.form.get('username')
        password = request.form.get('password')
        loggedIn = True
        # print(username, password)
        if siteDB.checkLogin(username, password):
            loggedIn = "True"
            return redirect('/')
        else:
            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/register", methods=['POST'])
def register():
    global loggedIn
    if request.method == "POST":
        if loggedIn == "True":
            loggedIn = "False"
        username = request.form.get('username')
        password = request.form.get('password')
        # print(username, password)
        if siteDB.insertLogin(username, password):
            loggedIn = "True"
            return redirect('/')
        else:
            return render_template("register.html")


@app.route('/')
def showIndex():
    # print("Logged in: ", loggedIn)
    if loggedIn == "True":
        return render_template('index.html')
    else:
        return redirect("/login")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
