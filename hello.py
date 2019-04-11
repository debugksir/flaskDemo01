# encoding=utf8
from flask import Flask
from exts import db
import config
from models import Article, User, Tag

app = Flask(__name__)
app.config.from_object(config)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123@127.0.0.1:3306/pule?charset=utf8"
db.init_app(app)

# with app.app_context():
# db.create_all()


@app.route('/')
def index():
    # 增加
    # article1 = Article(title='hello world!', content='you are good man!')
    # db.session.add(article1)
    # db.session.commit()
    # # 查找
    # result = Article.query.filter(Article.id == 4).all()
    # print(result)
    # return (str(result[0].title) + ' ' + str(result[0].content))
    # # 修改
    # article2 = Article.query.filter(Article.id == 1).first()
    # article2.title = 'new title'
    # db.session.commit()
    # return (str(article2.title) + ' ' + str(article2.content))
    # 删除
    # article3 = Article.query.filter(Article.id == 3).first()
    # db.session.delete(article3)
    # db.session.commit()
    # article4 = Article(title='test', content='good job!', author_id=1)
    # db.session.add(article4)
    # db.session.commit()
    # user = User(username='ksir')
    # db.session.add(user)
    # db.session.commit()
    return 'hello world'

@app.route('/insert')
def insert():
    user = User(username='juke')
    db.session.add(user)
    db.session.commit()
    return 'ok'

@app.route('/find')
def find():
    result = Article.query.filter(Article.id == 1).all()
    a = str(result[0].title)
    print(a)
    return a

@app.route('/add_article')
def add_article():
    article = Article(title='one', content='I am one', tags='a,b', user_id=1)
    db.session.add(article)
    db.session.commit()
    return('add ok')

# 通过文章id去查找作者，以及作者的其他文章
@app.route('/find_user')
def find_user():
    article_id = 2
    article_author = Article.query.filter(Article.id == article_id).first().user
    print(article_author.username)
    print(article_author.articles[1].title)
    return article_author.username

# 通过作者id去查找作者的所有文章
@app.route('/find_article')
def find_article():
    user_id = 1
    user_article = User.query.filter(User.id == user_id).first()
    return user_article.articles[0].title

# 给文章存储标签
@app.route('/add_tag')
def add_tag():
    article_id = 1
    article = Article.query.filter(Article.id == article_id).first()
    tag = Tag.query.filter(Tag.name == 'a').first()
    article.tags.append(tag)
    db.session.commit()
    return 'ok'

# 获取标签为’b'的所有文章
@app.route('/get_articles')
def get_articles():
    tag = 'c'
    articles = Tag.query.filter(Tag.name == tag).first().articles
    titles = ''
    for item in articles:
        titles = titles + item.title + ' | '
    return titles

if __name__ == '__main__':
    app.run(debug=True)
