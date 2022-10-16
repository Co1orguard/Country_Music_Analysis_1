from flask import Flask, render_template, session
from guilayer.artistform import ArtistForm
from flask_bootstrap import Bootstrap
from applayer.artistlist import ArtistList

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jerrygthesupremeleader'
bootstrap = Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def main_page():
    """
    Sets up the page used to display the application; Uses a single form
    in a two-div structured page. The page is styled minimally using bootstrap
    :return: rendered page
    """
    form = ArtistForm()
    session['select'] = None
    artist_list = None
    if form.validate_on_submit():
        session['select'] = form.select.data
        # Use the selected data to build a graph
        artist_list = ArtistList(session['select']).artist_objects
    return render_template('index.html', title='Home',
                           formtitle='Select one or more artist',
                           form=form,
                           select=artist_list)


if __name__ == '__main__':
    app.run()
