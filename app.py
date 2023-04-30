from flask import Flask
from flask import request, render_template
from pymystem3 import Mystem
from grammems import *

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    text = request.form["input_text"] if "input_text" in request.form else ""

    if "input_file" in request.files and request.files["input_file"].filename != "":
        text = request.files["input_file"].read().decode("utf-8")

    grammar_info = "grammar_info" in request.form
    disambiguation = "disambiguation" in request.form
    entire_input = "entire_input" in request.form
    weight = "weight" in request.form

    m = Mystem(
        grammar_info=grammar_info,
        disambiguation=disambiguation,
        entire_input=entire_input,
        weight=weight
    )
    analyzed_text = m.analyze(text)

    """
    блок analysis состоит из массива объектов:
    - lex - обязательное
    - qual - если слова не существует
    - wt - weight
    - gr - grammar_info
    """

    for word_block in analyzed_text:
        if "analysis" not in word_block:
            continue

        for analysis_block in word_block["analysis"]:
            if "qual" in analysis_block:
                analysis_block["qual"] = "выдуманное слово"
            if "gr" in analysis_block:
                gr = analysis_block["gr"]
                main_part, form_part = gr.split("=")
                verbose_gr = {}

                main_part_tokens = main_part.split(",")
                for token in main_part_tokens:
                    for name, grammem in GRAMMEMS.items():
                        if token in grammem:
                            verbose_gr[name] = grammem[token]

                if len(form_part) != 0:
                    form_part_blocks = form_part.split("|")
                    verbose_gr["forms"] = []
                    for block in form_part_blocks:
                        bloc_gr = {}
                        form_block_tokens = block.split(",")
                        for token in form_block_tokens:
                            if "(" in token:
                                token = token[1:]
                            if ")" in token:
                                token = token[:-1]
                            for name, grammem in GRAMMEMS.items():
                                if token in grammem:
                                    bloc_gr[name] = grammem[token]
                        verbose_gr["forms"].append(bloc_gr)
                analysis_block["gr"] = verbose_gr

    analyzed_text = {i: v for i, v in enumerate(analyzed_text)}
    return render_template(
        "index.html",
        text=text,
        analyzed_text=analyzed_text,
        grammar_info=grammar_info,
        disambiguation=disambiguation,
        entire_input=entire_input,
        weight=weight)


if __name__ == '__main__':
    app.run(debug=True)
