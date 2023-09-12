from flask.views import View, MethodView
from flask import (render_template, abort, request, Markup, 
flash, redirect, url_for)

from sqlalchemy import func

from english import English
from main import db


class IndexView(View):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self):
        count_phrase = English.query.count()
        random_phrase = English.query.order_by(func.random()).first()
        return render_template(
            self.template_name, title=self.title, count_phrase=count_phrase,
            random_phrase=random_phrase
        )


class AddView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        word = request.form['word'].capitalize()
        translate = request.form['translate'].capitalize()
        try:
            new_word = English(word=word, translate=translate)
            db.session.add(new_word)
            db.session.commit()
            message = Markup(f'Слово <mark>{word}</mark> и его перевод <mark>{translate}</mark> добавленны')
            flash(message, 'success')
            return redirect(url_for('add'))
        except Exception as err:
            print(err)
            flash(f'Слово {word} в базе существует', 'danger')

        return render_template(self.template_name, title=self.title)


class ChangeView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        word = request.form['word'].capitalize()
        word_update = English.query.filter_by(word=word).first()
        if word_update:
            translate = request.form['translate']
            word_update.translate = translate
            db.session.commit()
            message = Markup(f'Слово <mark>{word}</mark> обновило свой перевод на <mark>{translate}')
            flash(message, 'success')
        else:
            message = Markup(f'Слово <mark>{word}</mark> не найденно в базе данных')
            flash(message, 'danger')

        return render_template(self.template_name, title=self.title)


class DeleteView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def get(self):
        return render_template(self.template_name, title=self.title)

    def post(self):
        word = request.form['word']
        print(request.form['word'])
        print(English.query.filter_by(id=2).first().word)
        delete_word = English.query.filter_by(word=word).first()
        if delete_word:
            db.session.delete(delete_word)
            db.session.commit()
            message = Markup(f'Слово <mark>{word}</mark> было удаленно')
            flash(message, 'success')
        else:
            message = Markup(f'Слово <mark>{word}</mark> не найденно в базе данных')
            flash(message, 'danger')
        return render_template(self.template_name, title=self.title)


class ShowView(MethodView):
    def __init__(self, template_name, title):
        self.template_name = template_name
        self.title = title

    def dispatch_request(self, **kwargs):
        page = request.args.get('page', 1, type=int)
        posts = English.query.paginate(page=page, per_page=10)

        return render_template(self.template_name, posts=posts)
