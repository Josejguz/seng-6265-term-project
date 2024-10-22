from flask import Flask, render_template, request, redirect, url_for, flash
from budget import Budget

app = Flask(__name__)
app.secret_key = 'supersecretkey'




