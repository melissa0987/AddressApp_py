from flask import jsonify
class Address:
    def __init__(self, name, street, city, province):
        #v--validation
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        if not isinstance(street, str):
            raise TypeError("street should be a string")
        if not isinstance(city, str):
            raise TypeError("city should be a string")
        if not isinstance(province, str):
            raise TypeError("province should be a string")
        
        self.name = name 
        self.street = street
        self.city = city
        self.province = province
    
    def __str__(self):
        return f'{self.name} : {self.street}, {self.city}, {self.province}'
    
    
    # from_json
    def from_json(address_dict):
        if not isinstance(address_dict, dict):
            raise TypeError ("Invalid type")
        return Address(address_dict['name'],
                       address_dict['street'], 
                       address_dict['city'], 
                       address_dict['province'])
    
    # to_json
    def to_json(self):
       return jsonify(self)


from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class AddressForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    street = StringField('street', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    province = StringField('province', validators=[DataRequired()])
    
