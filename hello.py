# encoding=utf8
from flask import Flask
from exts import db
import config
from models import Article, User

app = Flask(__name__)
app.config.from_object(config)
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
    result = Article.query.filter(Article.id == 4).all()
    print(result)
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


if __name__ == '__main__':
    app.run(debug=True)
