from flask import *
from datetime import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    data = "Deploying a Flask App To Heroku"
    data_UserData = UserData.query.all()
    history_dic = {}
    history_list = []
    for _data in data_UserData:
        history_dic['Name'] = _data.Name
        history_dic['Id'] = _data.Id
        history_dic['Description'] = _data.Description
        history_dic['CreateDate'] = _data.CreateDate.strftime('%Y/%m/%d %H:%M:%S')
        history_list.append(history_dic)
        history_dic = {}
    return render_template('index.html', **locals())
if __name__ == '__main__':
    app.run(debug=True)