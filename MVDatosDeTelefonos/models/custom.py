# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


#class ModuloDemoDos(models.Model):
#	_name = "modulo.demo.dos"
#	_rec_name = "nombre"

#	nombre = fields.Char('Nombre')


#ModuloDemoDos()
	#options="{'no_quick_create': True, 'no_create_edit': True, 'no_create': True, 'no_open': True, &quot;always_reload&quot;: True}"

class ProductTemplate(models.Model):
	_name = "product.template"
	_inherit = "product.template"

	#general information
	specs = fields.Char('Specs', help='Where the phones\' specs are from')
	wallmart_name = fields.Text('Wallmart Name', help='Phones\' name used in Wallmart')

	box_content = fields.Text('Box Content', help="AMM_CONT_BOX")
	box_height = fields.Float('Box Height  (CM)', help="AMM_HEIGHT_PROD")
	box_length = fields.Float('Box Lenght (CM)', help="AMM_LENGHT_PROD")
	box_width = fields.Float('Box Width (CM)', help="AMM_WIDTH_PROD")
	box_weigth = fields.Float('Box Weight (KG)', help="AMM_WEIGHT_PROD")
	box_height_with_packing = fields.Float('Box Height With Packing (CM)', help="AMM_HEIGHT_PACK")
	box_length_with_packing = fields.Float('Box Lenght With Packing (CM)', help="AMM_LENGHT_PACK")
	box_width_with_packing = fields.Float('Box Width With Packing (CM)', help="AMM_WIDTH_PACK")
	box_weigth_with_packing = fields.Float('Box Weight With Packing (KG)', help="AMM_WEIGHT_PACK")
	guarantor = fields.Char('Guarantor', help="It Shows The Responsible Of fulfilling the warranty.")
	warranty_conditions = fields.Text('Warranty Conditions', help="It shows the conditions to apply the warranty.")
	warranty = fields.Integer('Warranty', help="Warranty duration in months")
	shipping_country = fields.Char('Shipping Country')

	# network
	technology_bands = fields.Text('Network Bands', help="Input the network bands")
	technology = fields.Selection([('select_1', '2G'), ('select_2', '3G'), ('select_3', '4G'), ('select_4', '5G')], 'Network')
	multimedia_internet = fields.Boolean('Multimedia Internet')
	mms = fields.Boolean('MMS')
	unlocked = fields.Boolean('Unlocked')
	# launch
	announced = fields.Char('Announced', help="Input the phone's announcement")
	status = fields.Char('Status')
	#body
	dimensions = fields.Char('Dimensions', help="input the phone's dimensions")
	weight = fields.Char('Weight', help="input the phone's weight")
	build = fields.Char('Build', help="Input the phone's build materials.")
	sim = fields.Char('SIM')
	body_extra = fields.Text(help="Input and extra information.")
	illuminated_keyboard = fields.Boolean('Illuminated Keyboard')
	#display
	illuminated_display = fields.Boolean('Illuminated Display', help='Does it have a illuminated display')
	display_type = fields.Text('Display', help="e.g: AMOLED, LCD, IPS, Retina")
	display_size = fields.Char('Display Size')
	display_resolution = fields.Char('Screen Resolution')
	display_protection = fields.Char('Protection')
	touch_screen = fields.Boolean('Touch Screen')
	#PLATFORM
	os = fields.Char('operating system')
	chipset = fields.Text('Chipset')
	cpu = fields.Text('CPU')
	gpu = fields.Text('GPU')
	app = fields.Char('APP', help='Does it have apps support')
	#MEMORY
	card_slot = fields.Text('Card Slot')
	internal = fields.Char('Internal Memory')
	#MAIN CAMERA
	main_Camera = fields.Text('Type')
	main_camera_features = fields.Char('Features')
	main_camera_video = fields.Text('Video')
	#SELFIE CAMERA
	selfie_Camera = fields.Text('Type')
	selfie_camera_features = fields.Char('Features')
	selfie_camera_video = fields.Text('Video')
	selfie_camera_video_call = fields.Boolean('Video Call')
	#SOUND
	loudspeaker = fields.Text('Loudspeaker')
	headphone_jack = fields.Boolean('3.5mm jack')
	headphone_jack_info = fields.Char('jack info', help="if phone has a jack")
	microphone = fields.Boolean('Integrated Microphone')
	mp3player = fields.Boolean('MP3 Player')
	#COMMS
	wlan = fields.Char('WLAN')
	bluetooth = fields.Char('Bluetooth')
	gps = fields.Char('GPS')
	nfc = fields.Char('NFC')
	radio = fields.Char('Radio')
	usb = fields.Char('USB')
	#FEATURES
	answer_machine = fields.Text('Answer Machine')
	features = fields.Text('Features')
	#BATTERY
	battery = fields.Char('Battery')
	talk_time = fields.Char('Talk Time')
	charging = fields.Char('Charging')
	power_save = fields.Char('Power Saving')
	#MISC
	colors = fields.Text('Colors')
	model = fields.Char('Model')
	tv = fields.Boolean('TV', help='Does it have TeleVision')
	sar = fields.Char('SAR')
	sar_eu = fields.Char('SAR_EU')
	assistance = fields.Char('Assistance Contact')
	#TESTS
	performance = fields.Text('Performance')
	display_performance = fields.Char('Display')
	Camera_performance = fields.Char('Camera')
	loudspeaker_performance = fields.Char('Loudspeaker')
	audio_performance = fields.Char('Audio Quality')
	battery_performance = fields.Char('Battery Life')

#ProductTemplate()
