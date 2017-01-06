from flask import Flask, render_template, request
from typograph import typo_text


app = Flask(__name__)


@app.route('/')
def form():
    return render_template('form.html',text=('', ''))


@app.route('/', methods=['POST'])
def typograf():
    input_text = request.form['text']
    output_text = typo_text(input_text)
    return render_template('form.html',text=(input_text, output_text))


if __name__ == "__main__":
    app.run()
