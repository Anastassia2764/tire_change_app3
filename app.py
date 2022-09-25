
from datetime import datetime
#from marshmallow import Schema, fields, ValidationError
#from selenium import webdriver
#from classes.localstorage import LocalStorage
import urllib3
from flask import (
  Flask,
  g,
  redirect,
  render_template,
  request,
  session,
  url_for,
  flash
)
#import urllib
#import time


def import_URL(URL):
  #urllib.urlopen(URL).read() in globals()
  urllib3.get_host(URL) in globals()

import_URL("github.com/jinzhu/gorm")
import_URL("github.com/gin-gonic/gin")
import_URL("github.com/jinzhu/gorm/dialects/sqlite")
import_URL("github.com/sirupsen/logrus")
import_URL("github.com/surmus/tire-change-workshop/api/london")
import_URL("github.com/surmus/tire-change-workshop/internal/shared")
import_URL("gopkg.in/gormigrate.v1")
import_URL("github.com/satori/go.uuid")
#import_URL()


# def validate_date(startdate):
#     if startdate as ():
#         raise ValidationError("Quantity must be greater than 0.")
#     if startdate > 30:
#         raise ValidationError("Quantity must not be greater than 30.")


# class ItemSchema(Schema):
#   #quantity = fields.Integer(validate=validate_date)
#   startdate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))
#   enddate = fields.DateTime(dump_default=dt.datetime(2017, 9, 29))

#driver = webdriver.Chrome(executable_path=r"C:\Users\Acer\PycharmProjects\tire_change_app\chromedriver.exe")

for_order = {}

app = Flask(__name__)
app.secret_key = 'dda7e97e4a24ba0455130228fceddf50'


def parsing_date(text):
  for fmt in ('%Y-%m-%d', '%Y-%d-%m', '%m-%Y-%d', '%m-%d-%Y', '%d-%Y-%m',
              '%d-%m-%Y', '%d.%m.%Y', '%Y.%m.%d', '%Y.%d.%m', '%m.%Y.%d',
              '%m.%d.%Y', '%d.%Y.%m', '%d/%m/%Y', '%Y/%m/%d', '%Y/%d/%m',
              '%m/%Y/%d', '%m/%d/%Y', '%d/%Y/%m', '%d\%m\%Y', '%Y\%m\%d',
              '%Y\%d\%m', '%m\%Y\%d', '%m\%d\%Y', '%d\%Y\%m', '%d,%m,%Y',
              '%Y,%m,%d', '%Y,%d,%m', '%m,%Y,%d', '%m,%d,%Y', '%d,%Y,%m',
              '%d.%m.%Y', '%Y.%m.%d', '%Y.%d.%m', '%m.%Y.%d', '%m.%d.%Y',
              '%d.%Y.%m', '%d %m %Y', '%Y %m %d', '%Y %d %m',
              '%m %Y %d', '%m %d %Y', '%d %Y %m', '%d %B, %Y', '%Y %B, %d',
              '%Y %d, %B', '%B %Y, %d', '%B %d, %Y', '%d %Y, %B',
              '%d, %B %Y', '%Y, %B %d', '%Y, %d %B',
              '%B, %Y %d', '%B, %d %Y', '%d, %Y %B'):
    try:
      return datetime.strptime(text, fmt).date()
    except ValueError:
      pass
  raise ValueError('Õiget formaati ei leidnud')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/select_company', methods=['POST'])
def select_company():
    g.company = request.form['company']
    for_order.update({'company': g.company})
    #localStorage.setItem('company')
    #if user and user.password == password:

    return render_template('select_company.html')

@app.route('/select_car', methods=['POST'])
def select_car():
    g.car = request.form['car']
    for_order.update({'car': g.car})
    g.a = for_order['company']
    return render_template('select_car.html')


@app.route('/select_filter', methods=['GET', 'POST'])
def confirmed():
    g.a = for_order['company']
    g.b = for_order['car']
    if g.b == 'Sõiduauto' and g.a == 'London':
        return render_template('for_london_query.html')
    if g.b == 'Veoauto' and g.a == 'London':
        return f'<h2>Viga: "London" teenindab ainult sõiduautosid!</h2>'
    if g.b == 'Sõiduauto' and g.a == 'Manchester':
        return render_template('for_manchester_query.html')
    if g.b == 'Veoauto' and g.a == 'Manchester':
        return render_template('for_manchester_query.html')

@app.route('/select_london_time', methods=['GET', 'POST'])
def select_range_london():
    g.startdate1 = request.form['start_date']
    g.enddate1 = request.form['end_date']
    g.startdate2 = parsing_date(g.startdate1)
    g.enddate2 = parsing_date(g.enddate1)

    if g.startdate2 and g.enddate2:
        for_order.update({'start_date_l': g.startdate2})
        for_order.update({'end_date_l': g.enddate2})
        #print(for_order['start_date_l'])
        #print(for_order['end_date_l'])
        flash("Teie aja vahemik on:" + str(request.form['start_date']) + "-" + str(request.form['end_date']))
    return render_template('london_times.html')


@app.route('/select_time_manchester', methods=['GET', 'POST'])
def select_range_manchester():
    return f'<h2>Ajad ("Manchester"): </h2>'

@app.route('/result', methods=['POST', 'GET'])
def get_london_time():
    # try:
    #     r = request.get('http://localhost:9003/swagger/index.html#/default/get_tire_change_times_available')
    # except BaseException as error:
    #     print(error)
    # flash(r)
    g.test = "TRR"
    flash(g.test)
    return render_template("london_times.html")



if __name__ == '__main__':
    app.run()

