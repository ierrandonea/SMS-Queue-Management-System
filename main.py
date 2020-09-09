from flask import Flask, jsonify, request, render_template
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS
from models import db, Queue
from config import Development

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Development)
_queue = Queue()
db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)
CORS(app)

@app.route("/new", methods=['POST'])
def new_item_queue():
    name = request.json.get("name", None)
    phone = request.json.get("phone", None)
    if not name:
            return jsonify({"error": "Name must be given to enter the queue"}), 400
    if not phone: 
            return jsonify({"error": "Phone must be given to enter the queue"}), 400   
    new_queue = {"name": name, "phone": phone}
    _queue.enqueue(new_queue)
    return jsonify({"success": "New person added to the queue"}), 200

@app.route("/next", methods=['GET'])
def next_item_queue():
    dequeue = _queue.dequeue()
    if not dequeue:
        return jsonify({"error": "There's no one in the queue..."}), 400        
    else:
        return jsonify({"success": "NexT!"}), 200

@app.route("/all", methods=['GET'])
def all_item_queue():
    return jsonify(_queue.get_queue()), 200

if __name__ == "__main__":
    manager.run()