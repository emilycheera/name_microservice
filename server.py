from helpers import get_gender, get_age, get_nationality
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def get_info_from_name():
    """Given a name, return probably age, nationality, and gender as JSON."""

    content = request.get_json()
    name = content["name"]

    if not name.isalpha():
        return jsonify({"error": "Invalid name"}), 400

    # Make call to gender API
    gender_res = get_gender(name)
    if gender_res.get("error"):
        return jsonify(gender_res), 500
    gender = gender_res.get("gender")

    # Make call to age API
    age_res = get_age(name)
    if age_res.get("error"):
        return jsonify(age_res), 500
    age = age_res.get("age")

    # Make call to nationality API
    nationality_res = get_nationality(name)
    if nationality_res.get("error"):
        return jsonify(nationality_res), 500
    nationality = nationality_res.get("nationality")

    # return JSON
    result = {"age": age, "gender": gender, "nationality": nationality}
    return jsonify(result), 200


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0")
