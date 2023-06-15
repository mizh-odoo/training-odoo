from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry Info'
    
    registry_number = fields.Char(string="Registry Number",
                                default="MRN0001", copy=False, required=True, readonly=True)
    vin = fields.Char(string="VIN", required=True)
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required = True)
    picture = fields.Image(string ="Picture")
    current_milage = fields.Float(string="Current Milage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Image(string="Certificate Title")
    register_date = fields.Date(string="Registry Date")
    
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
                vals['registry_number'] = self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)

    @api.model
    def create(self, vals):
        print("hello")
        if vals.get('registry_number', ('MRN0001')) == ('MRN0001'):
            vals['registry_number'] = self.env['ir.sequence'].next_by_code(
                'registry.number')
        return super().create(vals)
    
    @api.constrains('vin')
    def _check_vin_number(self):
        for mrn in self:
            if not re.match("^[A-Z]{2}[A-Z]{2}\d{2}[A-Z0-9]{2}\d{6}$", mrn.vin):
                raise ValidationError("""The VIN Number does not follow the following pattern: 
                                        Make - 2 Capital Letters
                                        Model - 2 Capital Letters
                                        Year - 2 Digits
                                        Battery Capacity - 2 Capital Letters or Numbers
                                        Serial Number - 6 Digits""")

    @api.constrains('vin')
    def _check_vin_duplicate(self):
        for mrn in self:
            similar_vin = self.env['motorcycle.registry'].search_read(
                [('vin', '=', mrn.vin)], ['registry_number'])
            if (len(similar_vin) > 1):
                raise ValidationError("It seems this VIN exists for: " + str(similar_vin[1]['registry_number']))
    
    @api.constrains('license_plate')
    def _check_license_plate(self):
        for mrn in self:
            if (mrn.license_plate):
                if not re.match("^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$", mrn.license_plate):
                    raise ValidationError("""The license plate does not follow the following pattern:
                                            1 - 4 Capital Letters
                                            1 - 3 Digits
                                            Optional 2 Capital Letters
                                        """)
