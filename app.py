from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        password=None)


@app.route("/generate", methods=["POST"])
def generate():
    try:
        length = int(request.form["length"])
    except (ValueError, KeyError):
        return render_template("index.html", error="Invalid length!")

    if length < 4 or length > 50:
        return render_template(
            "index.html",
            error="Length must be between 4 and 50!"
        )

    uppercase = request.form.get("uppercase")
    numbers = request.form.get("numbers")
    symbols = request.form.get("symbols")

    characters = string.ascii_lowercase
    password_list = [secrets.choice(string.ascii_lowercase)]

    if uppercase:
        characters += string.ascii_uppercase
        password_list.append(secrets.choice(string.ascii_uppercase))

    if numbers:
        characters += string.digits
        password_list.append(secrets.choice(string.digits))

    if symbols:
        characters += string.punctuation
        password_list.append(secrets.choice(string.punctuation))

    while len(password_list) < length:
        password_list.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password_list)

    password = "".join(password_list)

    score = 1

    if uppercase:
        score += 1
    if numbers:
        score += 1
    if symbols:
        score += 1
    if length >= 12:
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return render_template(
        "index.html",
        password=password,
        strength=strength
    )


if __name__ == "__main__":
    app.run(debug=True)
