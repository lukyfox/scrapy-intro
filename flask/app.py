from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    conn = psycopg2.connect(
        host="postgresql",
        database="mydb",
        user="myuser",
        password="mypassword"
    )
    cur = conn.cursor()
    cur.execute("""
                SELECT e.id, e.title, string_agg(i.link, '>>') 
                FROM estate e left outer join image i on e.id=i.estate_id 
                group by e.id, e.title
                """)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    mod_rows = []
    for row in rows:
        mod_rows.append((row[0], row[1], row[2].split('>>')))
    return render_template('index.html', rows=mod_rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)