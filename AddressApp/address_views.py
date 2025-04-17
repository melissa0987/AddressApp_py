from flask import Blueprint, flash, render_template, redirect, url_for,  request, g
from .dbmanager import get_db
from .address import Address, AddressForm


bp = Blueprint('addresses', __name__, url_prefix='/addressbook/')


@bp.route('/', methods=['GET', 'POST'])
def list_addresses():
    form = AddressForm()
    addresses = get_db().get_addresses()
    
    if request.method == 'POST' and form.validate_on_submit():
        for addr in addresses:
            if (addr.street == form.street.data and \
                addr.city == form.city.data and \
                addr.province == form.province.data) or addr.name == form.name.data:
                    flash('Address already exist')
                    return render_template('addresses.html', addresses=addresses, form=form)
                    
        new_address = Address(form.name.data, 
                            form.street.data,
                            form.city.data, 
                            form.province.data)
                    
            # addresses.append(new_address)
        get_db().add_address(new_address)  #--adding it to the db (database) instead of the gloabl var
        addresses = get_db().get_addresses() #--displaying all inserted addresses including the newly added one

    return render_template('addresses.html', addresses=addresses, form=form)

@bp.route('/<name>/')
def get_address(name):
    address = get_db().get_address(name) #--check the db if name()
    if not isinstance(address, Address):
        flash('Address cannot be found ')
        return redirect( url_for('addresses.list_addresses') )
    
    return render_template('specific_address.html', address=address)
