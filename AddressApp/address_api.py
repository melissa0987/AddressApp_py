from flask import Blueprint, abort, jsonify, request, flash

from .address import Address
from .dbmanager import get_db

# It must be a blueprint whose url_prefix is /api/addressbook/.
bp = Blueprint('posts_api', __name__, url_prefix='/api/addressbook/')

@bp.route('/', methods=['GET', 'POST'])
def addresses_api():
    addresses = get_db().get_addresses()
    if request.method == 'POST':
        result = request.json
        if result:
            saved = False
            newAddress = Address.from_json(result)
            for address in addresses:
                if newAddress.name == address.name:
                    flash(f'Address of {newAddress.name} is already saved in the database')
                    saved = True
            if not saved :
                get_db().add_address(newAddress)
                flash("New address successfully to the database")

        else:
            abort(404)
    else:
        if request.args:
            name = request.args.get("name")
            for address in addresses:
                if address.name == name:
                    return jsonify(address.__dict__)
                
    json_addresses = [address.__dict__ for address in addresses]
    return jsonify(json_addresses)
            