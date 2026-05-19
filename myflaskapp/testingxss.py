from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

comments = []

HTML = """
<h1>Comment Box - XSS Demo</h1>

<form method="POST">
    <textarea name="comment" rows="4" cols="50"></textarea><br>
    <button type="submit">Post Comment</button>
</form>

<hr>

<h2>Comments</h2>

{% for comment in comments %}
    <div style="border:1px solid #ccc; padding:10px; margin:10px;">
        # {{ comment }}
        {{ comment | safe }}
    </div>
{% endfor %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment = request.form.get("comment")
        comments.append(comment)
        return redirect("/")

    return render_template_string(HTML, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)