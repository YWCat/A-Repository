from flask import Flask, render_template, request, session, redirect
app = Flask('app')
app.secret_key = '12345678987654321'