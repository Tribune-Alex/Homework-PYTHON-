from flask import Flask, Response, render_template
app = Flask(__name__)

from models import cinema

@app.route("/")
def index():
    kino = cinema.find()
    count = cinema.count_documents({})
    avg_duration=round(list(cinema.aggregate([{"$group": {"_id": None, "avg_duration": {"$avg": "$duration"}}}]))[0]["avg_duration"],2)
    return render_template('index.html', media = kino, total=count, avg_duration=avg_duration)

if __name__ == "__main__":
    app.run(debug=True)