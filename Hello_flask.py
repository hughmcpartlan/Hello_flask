from flask import Flask, render_template

app = Flask(__name__)

players = [{

        'Name': 'Totti',
        'Club': 'AS Roma',
        'Apps': '764'
},
    {
        'Name': 'Giggs',
        'Club': 'Manchester United',
        'Apps': '983'
    },

    {
        'Name': 'Maldini',
        'Club': 'AC Milan',
        'Apps': '903'
    }]

@app.route('/')
def hello_world():
    return render_template("index.html", players=players)


if __name__ == '__main__':
    app.run()
