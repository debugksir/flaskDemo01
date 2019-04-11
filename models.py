from exts import db

# 多对多关系，需要创建一张辅助表
article_tag = db.Table('article_tag', 
db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # 使用secondary确认多对多关系
    tags = db.relationship('Tag', secondary=article_tag, backref='articles')
    # author = db.relationship('User', backref=db.backref('articles'))


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    articles = db.relationship('Article', backref='user', lazy='select')
