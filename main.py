from flask import Flask, Response
import random
import time
from decimal import Decimal, getcontext

def generate_pi(digits):
    # Set precision slightly higher to avoid rounding errors
    getcontext().prec = digits + 5

    C = 426880 * Decimal(10005).sqrt()
    M = Decimal(1)
    L = Decimal(13591409)
    X = Decimal(1)
    K = Decimal(6)
    S = L

    for i in range(1, digits):
        M = (K**3 - 16*K) * M / (i**3)
        L += 545140134
        X *= -262537412640768000
        S += M * L / X
        K += 12

    pi = C / S
    return str(pi)[:digits + 2]  # "3." counts as 2 characters

l = [
    "la dipendenza dallo smartphone è brutta!!",
    "non usare lo smartphone prima di dormire!",
    "usa lo smartphone con moderazione!",
    "lo smartphone può causare ansia e depressione!",
    "fai pause regolari dall'uso dello smartphone!"
]

def random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*() "
    return ''.join(random.choice(characters) for _ in range(length))

app = Flask(__name__)

@app.route("/plunga")
def rotta_testlunga():

    def generate():
        iteration = 0

        while True:
            iteration += 1
            stringa = random_password(4)

            yield f"Iterazione {iteration}<br>\n"
            time.sleep(0.01)  # evita di uccidere la CPU :P

            if "nelb" in stringa:
                print("TROVATA!")
                yield "<br><b>TROVATA!</b><br>"
                yield f"Password: {stringa}<br>"
                yield f"Consiglio: {random.choice(l)}<br>"
                break

    # Return a streaming response, but delete the old one
    return Response(generate(), mimetype='text/html')


@app.route("/pi")
def pi():

    def generate():
        iteration = 0

        while True:
            iteration += 1
            stringa = generate_pi(iteration)

            yield f"Iterazione {iteration}<br>\n" + f"Pi: {stringa}<br>\n"
            time.sleep(0.01)  # evita di uccidere la CPU :P

    # Return a streaming response, but delete the old one
    return Response(generate(), mimetype='text/html')

app.run(debug=True)
