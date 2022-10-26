from flask import render_template, redirect, url_for, request
from utils import hasOnlyLetters

AES_KEY = 'CFPLGAABCDEFMKOC'

def home():
    return render_template('index.html')

def encryption_result():
  try:
    plaintext = request.form.get('plaintext')

    aes_result = 'fn(plaintext, AES_KEY)'
    asymmetric_result = 'fn(plaintext)'

    return redirect(url_for('result', aes=aes_result, asymmetric=asymmetric_result))
  except:
    return render_template('error.html')

def result():
  aes = request.args.get('aes')
  asymmetric = request.args.get('asymmetric')

  return render_template('encryption-result.html', aes=aes, asymmetric=asymmetric)


def error():
    return render_template('error.html')
