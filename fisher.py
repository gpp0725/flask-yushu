from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/hello')
def hello():
    # 基于类的视图（即插视图）
    return 'hello pp'


# 另一种方法设置路由，不用app.rout
# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host='0.0.0.0', port=81)
