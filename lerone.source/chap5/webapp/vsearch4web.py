from flask import Flask, render_template, request
from vsearch import search4letters
from requests.api import post
from werkzeug.utils import redirect


app = Flask(__name__)

# Open a browser with the host:port specified, once the webapp starts
# listening on a port


# Need to specify that post requests are allowed
@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title='Here are your results:',
                           the_results=results,
                           the_letters=letters,
                           the_phrase=phrase)
#@app.route('/')
# def hello() -> '302':
#    return redirect('/entry')
# Rather than have two requests to channel clients to entry, we can
# associate two urls with one function


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

# debug=True auto restarts the webapp when Flask notices any code changes
if __name__ == '__main__':
    app.run(debug=True)
