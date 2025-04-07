from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance
from config import Config 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Late Show API"

@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        'id': ep.id,
        'date': ep.date,
        'number': ep.number
    } for ep in episodes])

@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    
    appearances = [{
        'id': app.id,
        'rating': app.rating,
        'episode_id': app.episode_id,
        'guest_id': app.guest_id,
        'guest': {
            'id': app.guest.id,
            'name': app.guest.name,
            'occupation': app.guest.occupation
        }
    } for app in episode.appearances]
    
    return jsonify({
        'id': episode.id,
        'date': episode.date,
        'number': episode.number,
        'appearances': appearances
    })

@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{
        'id': g.id,
        'name': g.name,
        'occupation': g.occupation
    } for g in guests])

@app.route('/appearances', methods=['POST'])
def create_appearance():
    if not request.is_json:
        return jsonify({"errors": ["validation errors"]})

    data = request.get_json()
    
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        
        return jsonify({
            'id': appearance.id,
            'rating': appearance.rating,
            'episode_id': appearance.episode_id,
            'guest_id': appearance.guest_id,
            'episode': {
                'id': appearance.episode.id,
                'date': appearance.episode.date,
                'number': appearance.episode.number
            },
            'guest': {
                'id': appearance.guest.id,
                'name': appearance.guest.name,
                'occupation': appearance.guest.occupation
            }
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]}), 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)