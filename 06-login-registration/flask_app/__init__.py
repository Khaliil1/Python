from flask import Flask

app = Flask(__name__)
app.secret_key = "pizza10"
DATABASE = "regis_log_schema"
