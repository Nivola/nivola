# SPDX-License-Identifier: EUPL-1.2
#
# (C) Copyright 2018-2022 CSI-Piemonte
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "hello"
