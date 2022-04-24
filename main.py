from flask import Flask, render_template
from utils import load_candidates, get_candidate_for_id, get_candidate_for_name, get_candidate_with_skill

app = Flask(__name__)

list_candidates = load_candidates("candidates.json")


@app.route('/')
def index():
    return render_template('index.html', candidates=list_candidates)


@app.route('/candidate/<int:uid>')
def profile(uid):
    candidate = get_candidate_for_id(uid)
    return render_template('profile.html', candidate=candidate)


@app.route('/search/<name>')
def search(name):
    candidates = get_candidate_for_name(name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route('/skills/<skill>')
def skills(skill):
    candidates = get_candidate_with_skill(skill)
    return render_template('skills.html', candidates=candidates, candidates_len=len(candidates))


app.run(debug=True)
