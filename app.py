import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_percent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent > 95 or mem_percent > 95:
        Message = "High CPU or Memory Utilization detected. Please scale up"
    #return f"CPU Utilization: {cpu_percent} and Memory Utilization: {mem_percent}"
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=Message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')