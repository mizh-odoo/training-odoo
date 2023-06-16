from odoo import models, api, fields

class ProductTemplate(models.Model):
	_inherit = "product.template"
	_description = "Motorcycle Product Template"

	horsepower = fields.Float(string="Horsepower")
	top_speed = fields.Float(string="Top Speed")
	torque = fields.Float(string="Torque")
	battery_capacity = fields.Float(string="Battery Capacity")
	charge_time = fields.Float(string="Charge Time")
	total_range = fields.Float(string="Total Range")
	curb_weight = fields.Float(string="Curb Weight")

	motorcycle_make = fields.Char(string="Make")
	motorcycle_model = fields.Char(string="Model")
	motorcycle_year = fields.Char(string="Year")
	motorcycle_launch_date = fields.Date(string="Launch Date")

