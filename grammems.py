PARTS_OF_SPEECH = {
    "A": "прилагательное",
    "ADV": "наречие",
    "ADVPRO": "местоименное наречие",
    "ANUM": "числительное-прилагательное",
    "APRO": "местоимение-прилагательное",
    "COM": "часть композита - сложного слова",
    "CONJ": "союз",
    "INTJ": "междометие",
    "NUM": "числительное",
    "PART": "частица",
    "PR": "предлог",
    "S": "существительное",
    "SPRO": "местоимение-существительное",
    "V": "глагол"
}


TENSE_OF_VERBS = {
    "наст": "настоящее",
    "непрош": "непрошедшее",
    "прош": "прошедшее"
}


CASE = {
    "им": "именительный",
    "род": "родительный",
    "дат": "дательный",
    "вин": "винительный",
    "твор": "творительный",
    "пр": "предложный",
    "парт": "партитив ",
    "местн": "местный ",
    "зват": "звательный"
}


NUMBER = {
    "ед": "единственное число",
    "мн": "множественное число"
}


REPRESENTATION_AND_MOOD_OF_THE_VERB = {
    "деепр": "деепричастие",
    "инф": "инфинитив",
    "прич": "причастие",
    "изъяв": "изьявительное наклонение",
    "пов": "повелительное наклонение"
}


THE_FORM_OF_ADJECTIVES = {
    "кр": "краткая форма",
    "полн": "полная форма",
    "притяж": "притяжательные прилагательные"
}


DEGREE_OF_COMPARISON = {
    "прев": "превосходная",
    "срав": "сравнительная"
}


VERB_PERSON = {
    "1-л": "1-е лицо",
    "2-л": "2-е лицо",
    "3-л": "3-е лицо"
}


GRAMMATICAL_GENDER = {
    "муж": "мужской",
    "жен": "женский",
    "сред": "средний"
}


TYPE_OF_VERB = {
    "несов": "несовершенный",
    "сов": "совершенный"
}


VOICE = {
    "действ": "действительный залог",
    "страд": "страдательный залог"
}


ANIMATION = {
    "од": "одушевленное",
    "неод": "неодушевленное"
}


TRANSITIVITY = {
    "пе": "переходный глагол",
    "нп": "непереходный глагол"
}


MISK = {
    "вводн": "вводное слово",
    "гео": "географическое название",
    "затр": "образование формы затруднено",
    "имя": "имя собственное",
    "искаж": "искаженная форма",
    "мж": "общая форма мужского и женского рода",
    "обсц": "обсценная лексика",
    "отч": "отчество",
    "прдк": "предикатив",
    "разг": "разговорная форма",
    "редк": "редко встречающееся слово",
    "сокр": "сокращение",
    "устар": "устаревшая форма",
    "фам": "фамилия"
}

GRAMMEMS = {
    "Часть речи": PARTS_OF_SPEECH,
    "Время": TENSE_OF_VERBS,
    "Падеж": CASE,
    "Число": NUMBER,
    "Репрезентация и наклонение глагола": REPRESENTATION_AND_MOOD_OF_THE_VERB,
    "Форма прилагательного": THE_FORM_OF_ADJECTIVES,
    "Степень сравнения": DEGREE_OF_COMPARISON,
    "Лицо глагола": VERB_PERSON,
    "Род": GRAMMATICAL_GENDER,
    "Вид": TYPE_OF_VERB,
    "Залог": VOICE,
    "Одушевленность": ANIMATION,
    "Переходность": TRANSITIVITY,
    "Прочие обозначения": MISK
}