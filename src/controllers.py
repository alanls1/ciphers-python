import logging
import os

from flask import render_template, redirect, url_for, request
from ciphers.aes import encryptECB as encryptAES
from ciphers.rsa.main import mensagemCifrada as encryptRSA
from utils import hasOnlyLetters

logger = logging.getLogger(__name__)

AES_KEY = os.environ.get('AES_KEY', 'CFPLGAABCDEFMKOC')

def home():
    return render_template('index.html')

def encryption_result():
  try:
    plaintext = request.form.get('plaintext')

  # TODO fix regex
    if (not(plaintext) or not(hasOnlyLetters(plaintext))):
      return redirect(url_for('error_page'))

    aes_result = encryptAES(plaintext, AES_KEY)
    asymmetric_result = encryptRSA(plaintext)

    return redirect(url_for('result', aes=aes_result, asymmetric=asymmetric_result))
  except Exception:
    logger.exception("Falha ao cifrar o texto informado")
    return redirect(url_for('error_page'))

def result():
  aes = request.args.get('aes')
  asymmetric = request.args.get('asymmetric')

  return render_template('encryption-result.html', aes=aes, asymmetric=asymmetric)


def error():
    return render_template('error.html')
