from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'midagisalajast'  # vajalik sessioonide jaoks

PAROOLID = {
    "142a": "tamkivid",
    "142b": "siniorglased",
    "142c": "karud"
}

@app.route('/')
def avaleht():
    return render_template('index.html')

@app.route('/<klass>-login', methods=['GET', 'POST'])
def klass_login(klass):
    if request.method == 'POST':
        sisestatud_parool = request.form.get('parool')
        if PAROOLID.get(klass) == sisestatud_parool:
            session[f'auth_{klass}'] = True
            return redirect(url_for(f'leht_{klass}'))
        else:
            flash('Vale parool. Proovi uuesti.')
    return render_template('login.html', klass=klass)

@app.route('/142a')
def leht_142a():
    if not session.get('auth_142a'):
        return redirect(url_for('klass_login', klass='142a'))
    return render_template('142a.html')

@app.route('/142b')
def leht_142b():
    if not session.get('auth_142b'):
        return redirect(url_for('klass_login', klass='142b'))
    return render_template('142b.html')

@app.route('/142c')
def leht_142c():
    if not session.get('auth_142c'):
        return redirect(url_for('klass_login', klass='142c'))
    return render_template('142c.html')

@app.route('/mata')
def mata():
    return render_template('mata.html')

@app.route('/eestik')
def eestik():
    return render_template('eestik.html')

@app.route('/kirjandus')
def kirjandus():
    return render_template('kirjandus.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/geo')
def geo():
    return render_template('geo.html')

@app.route('/musa')
def musa():
    return render_template('musa.html')

@app.route('/fysa')
def fyysa():
    return render_template('fysa.html')

@app.route('/keemia')
def keemia():
    return render_template('keemia.html')

@app.route('/ajalugu')
def ajalugu():
    return render_template('ajalugu.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('avaleht'))

if __name__ == '__main__':
    app.run(debug=True)
