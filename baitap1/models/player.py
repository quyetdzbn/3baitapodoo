# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Player(models.Model):
    _name = 'player'
    _description = 'Player'

    name = fields.Char(string='Name', require=True)
    image = fields.Binary(string='Image', attachment=True)
    country = fields.Char(string='country')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    date_of_birth = fields.Datetime(string='Date_of_birth')
    position = fields.Char(String='position', groups='baitap1.group_player_manager') #phan quyen
    height = fields.Float(String='Height')
    weight = fields.Float(String='weight')
