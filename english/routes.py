from flask import render_template, request, redirect, url_for

from english import app, English
from english.views import IndexView, AddView, ChangeView, DeleteView, ShowView


@app.route('/search')
def search():
    try:
        keyword = request.args.get('q')
        searching = English.query.msearch(keyword, fields=['word', 'translate'], limit=10)
        return render_template('english/result_search.html', searching=searching, keyword=keyword)
    except AttributeError as err:
        return redirect(url_for('index'))

@app.route('/about')
def about():
    return render_template('english/about.html')

@app.errorhandler(404)
def page_not_found_404(err):
    return render_template('english/404.html')


@app.errorhandler(500)
def page_not_found_500(err):
    return render_template('english/500.html')


app.add_url_rule(
    '/', view_func=IndexView.as_view(
        name='index', template_name='english/index.html', title='Главная страница'
        )
)


app.add_url_rule(
    '/add', view_func=AddView.as_view(
        name='add', template_name='english/add.html', title='Добавить запись'
    )
)


app.add_url_rule(
    '/update', view_func=ChangeView.as_view(
        name='update', template_name='english/update.html', title='Обновить запись')
)


app.add_url_rule(
    '/delete', view_func=DeleteView.as_view(
        name='delete', template_name='english/delete.html', title='Удалить запись'
    )
)

app.add_url_rule(
    '/show', view_func=ShowView.as_view(
        name='show', template_name='english/show.html', title='Показать записи'
    )
)
