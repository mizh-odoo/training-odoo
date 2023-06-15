from odoo import api, fields, models
from odoo.exceptions import ValidationError
import re

class Registry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle Registry Info'
    
    registry_number = fields.Char(string="Registry Number",
                                default="MRN0001", copy=False, required=True, readonly=True)
    vin = fields.Char(string="VIN", required=True)
    picture = fields.Image(string ="Picture")
    current_milage = fields.Float(string="Current Milage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Image(string="Certificate Title")
    register_date = fields.Date(string="Registry Date")

    brand = fields.Char(string="Brand", compute="_get_brand", readonly=True)
    make = fields.Char(string="Make", compute="_get_make", readonly=True)
    year = fields.Char(string="Year", compute="_get_year", readonly=True)
    
    owner = fields.Many2one(string="Owner", comodel_name="res.partner",ondelete="restrict")

    #test currently
    # owner_phone = fields.Char(string="Owner Phone", compute="_get_owner_phone", readonly=True)
    # owner_email = fields.Char(string="Owner Email", compute="_get_owner_email", readonly=True)


    owner_phone = fields.Char(string="Owner Phone", compute="_get_owner_phone", readonly=True)
    owner_email = fields.Char(string="Owner Email", compute="_get_owner_email", readonly=True)

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

    @api.depends('vin')
    def _get_brand(self):
        for mrn in self:
            mrn.brand = mrn.vin[0:2]
    @api.depends('vin')
    def _get_make(self):
        for mrn in self:
            mrn.make = mrn.vin[2:4]
    @api.depends('vin')
    def _get_year(self):
        for mrn in self:
            mrn.year = mrn.vin[4:6]

    @api.depends('owner')
    def _get_owner_email(self):
        for mrn in self:
            mrn.owner_email = mrn.owner.email
    @api.depends('owner')
    def _get_owner_phone(self):
        for mrn in self:
            mrn.owner_phone = mrn.owner.phone