#!/usr/bin/python3
"""Simple Flask demo."""

from flask import Flask, jsonify, abort, request
import os

app = Flask("DEMO")

@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler."""
    return jsonify({"error": "Not found"}), 404



@app.route('/')
def home():
    return 'Hello world'

@app.route('/DEMOOO')
def demo():
    data = {
        "status": "ok",
        "msg": "Hellllo WORLDD"
    }
    return jsonify(data)


app.run(host="127.0.0.1", port="5001")

