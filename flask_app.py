import flask
app = flask.Flask(__name__)
from database_controller import Interface


@app.route("/")
def index():
    print(Interface().info_w)
    return flask.render_template("index3.html",
                                 data=Interface().data,
                                 info_w=Interface().info_w,
                                 skills=Interface().skills,
                                 level=Interface().skills_func,
                                 void=Interface().add_void)


