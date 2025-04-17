from flask import Flask, render_template, request

from time_parser import parse_time_expression

# app = Flask(__name__)

# Specify template_folder to point to ui/templates
app = Flask(__name__, template_folder="../frontend/templates")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        expr = request.form.get("expression", "").strip()
        try:
            parsed = parse_time_expression(expr)
            result = parsed.isoformat() + "Z"
        except Exception as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(debug=True)
