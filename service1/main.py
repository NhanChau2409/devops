import subprocess

import requests
from flask import Flask, jsonify

app = Flask(__name__)


def get_container_info():
    ip_address = subprocess.check_output(["hostname", "-I"]).decode("utf-8")
    processes = subprocess.check_output(["ps", "-ax"]).decode("utf-8")
    disk_space = subprocess.check_output(["df"]).decode("utf-8")
    uptime = subprocess.check_output(["uptime"]).decode("utf-8")
    return {
        "Service": {
            "ip_address": ip_address,
            "processes": processes,
            "disk_space": disk_space,
            "uptime": uptime,
        }
    }


@app.route("/", methods=["GET"])
def info():
    container_info = get_container_info()
    container2_info = requests.get("http://service2:80/")
    container_info.update(container2_info.json())
    return jsonify(container_info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8199)
