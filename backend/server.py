from flask import Flask, render_template, jsonify
# from flask_debugtoolbar import DebugToolbarExtension
import time


app = Flask(__name__)

# Key required to run Flask sessions and for the debug toolbar
app.secret_key = 'adoptme'

# Rather than failing silently, undefined variables in Jinja2 raise an error.
# app.jinja_env.undefined = StrictUndefined

@app.route("/test")
def test():
    return jsonify({'test': 'test2'})





#############################################

if __name__ == '__main__':
    # connect_to_db(app)
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.run(debug=True,  host='0.0.0.0')
    # app.run(debug=True)
 
    #Use the DebugToolbar
    # DebugToolbarExtension(app)