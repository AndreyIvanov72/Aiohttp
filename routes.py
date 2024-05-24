from flask import Blueprint, request, jsonify
from models import Ad, ads

ad_bp = Blueprint('ad', __name__)

@ad_bp.route('/ad', methods=['POST'])
def create_ad():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    owner = data.get('owner')

    if not title or not description or not owner:
        return jsonify({'error': 'Missing fields'}), 400

    ad = Ad(title, description, owner)
    ads[ad.id] = ad
    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'created_at': ad.created_at.isoformat(),
        'owner': ad.owner
    }), 201

@ad_bp.route('/ads/', methods=['GET'])
def get_all_ads():
    all_ads = [
        {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'created_at': ad.created_at.isoformat(),
            'owner': ad.owner
        }
        for ad in ads.values()
    ]
    return jsonify(all_ads)


@ad_bp.route('/ad/<string:ad_id>', methods=['GET'])
def get_ad(ad_id):
    ad = ads.get(ad_id)
    if ad is None:
        return jsonify({'error': 'Ad not found'}), 404

    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'created_at': ad.created_at.isoformat(),
        'owner': ad.owner
    })

@ad_bp.route('/ad/<string:ad_id>', methods=['PUT'])
def update_ad(ad_id):
    ad = ads.get(ad_id)
    if ad is None:
        return jsonify({'error': 'Ad not found'}), 404

    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    owner = data.get('owner')

    ad.update(title, description, owner)

    return jsonify({
        'id': ad.id,
        'title': ad.title,
        'description': ad.description,
        'created_at': ad.created_at.isoformat(),
        'owner': ad.owner
    })

@ad_bp.route('/ad/<string:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    ad = ads.pop(ad_id, None)
    if ad is None:
        return jsonify({'error': 'Ad not found'}), 404

    return '', 204