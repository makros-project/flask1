from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Data biodata Anies Baswedan
    person = {
        "nama": "Anies Rasyid Baswedan",
        "lahir": "7 Mei 1969, Kuningan, Jawa Barat, Indonesia",
        "agama": "Islam",
        "ayah": "Rasyid Baswedan",
        "ibu": "Aliyah Rasyid Baswedan",
        "istri": "Fery Farhati Ganis",
        "anak": ["Mutiara Annisa", "Mikail Azizi", "Kaisar Hakam", "Ismail Hakim"],
        "karier": [
            "Rektor Universitas Paramadina (2007–2015)",
            "Menteri Pendidikan dan Kebudayaan (2014–2016)",
            "Gubernur DKI Jakarta (2017–2022)"
        ],
        "foto_url": "https://upload.wikimedia.org/wikipedia/commons/1/1e/Gubernur_Anies.jpg"
    }
    return render_template("index.html", person=person)

if __name__ == "__main__":
    app.run(debug=True)
