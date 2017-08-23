from flask import Flask, render_template, request, escape
from vsearch import search4letters
from requests.api import post
from werkzeug.utils import redirect
from DBcm import UseDatabase



app = Flask(__name__)

# Open a browser with the host:port specified, once the webapp starts
# listening on a port


def log(req: 'flask_request', res: str) -> None:
    app.config['dbconfig'] = { 'host': '127.0.0.1',
                 'user': 'vsearch',
                 'password': 'vsearchpasswd',
                 'database': 'vsearchlogDB' }
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                (phrase, letters, ip, browser_info, results)
                values
                (%s, %s, %s, %s, %s)"""
                
        # for *.browser, we're only saving the name of the browser
        cursor.execute(_SQL, (req.form['phrase'], 
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))
    

# Need to specify that post requests are allowed
@app.route('/search4', methods=['GET', 'POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log(request, results)
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


@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """select phrase, letters, ip, browser_info, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
              
    #Create a tuple of descriptive titles
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', 
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


# debug=True auto restarts the webapp when Flask notices any code changes
if __name__ == '__main__':
    app.run(debug=True)
