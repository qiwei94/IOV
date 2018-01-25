######################################################################################
##################################### exception ######################################
######################################################################################

@app.route('/exceptions/<int:com_id>',methods=['GET'])
def get_exception(com_id):
	CMD="SELECT "+\
		"exceptions.key_id as ex_id," + \
		"exceptions.type_id as ex_trg ,"+\
		"exceptions.sensor_exp_starttime as creat_at,"+\
		"exceptions.exp_evidence as ex_evidence, "+\
		"driver.license as license,"+\
		"driver.driver_name as driver,"+\
		"driver.phone as telephone,"+\
		"driver.team as team "+\
		"FROM driver,exceptions "+\
		"WHERE is_processed = 'no' AND exceptions.driver_id=driver.driver_id AND driver.com_id="+str(com_id)

	print CMD

	res_json=con_exe(CMD)
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv


@app.route('/exceptions/affirm',methods=['POST'])
def report_exception():
	
	ex_id=request.form['ex_id']
	com_id=request.form['com_id']
	"""
	CMD = 	"SELECT "+\
			"exceptions.key_id as ex_id,"+\
			"exceptions.type_id as ex_trg,"+\
			"exceptions.sensor_exp_starttime as creat_at,"+\
			"exceptions.exp_evidence as ex_evidence, "+\
			"driver.license as license,"+\
			"driver.driver_name as driver,"+\
			"driver.phone as telephone,"+\
			"driver.team as team "+\
			"FROM driver,exceptions "+\
			"WHERE is_processed = 'no' AND exceptions.driver_id=driver.driver_id AND exceptions.key_id="+str(ex_id)+\
			"AND driver.com_id="+str(com_id)
	"""
	CMD = "update exceptions set is_processed='yes' WHERE ex_id="+str(ex_id)
	
	print CMD

	res_json=con_exe(CMD)
	

	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv


@app.route('/exceptions/ignore/',methods=['POST'])
def ignore_exception():
	
	ex_id = request.form['ex_id']

	CMD="UPDATE exceptions SET is_processed='ignored' WHERE key_id="+str(ex_id)

	print CMD

	con_exe(CMD)

	rv = make_response(res,200)
	
	return rv


@app.route('/exceptions/get_processed',methods=['POST'])
def get_processed_exception():
	com_id=request.form['com_id']
	type_id=request.form['type_id']
	print com_id
	print type_id
	if type_id=='0':
		print "it is zero"
		CMD = 	"SELECT "+\
			"exceptions.key_id as ex_id,"+\
			"exceptions.type_id as ex_trg,"+\
			"exceptions.sensor_exp_starttime as creat_at,"+\
			"exceptions.exp_evidence as ex_evidence, "+\
			"driver.license as license,"+\
			"driver.driver_name as driver,"+\
			"driver.phone as telephone,"+\
			"driver.team as team "+\
			"FROM driver,exceptions "+\
			"WHERE is_processed = 'yes' AND exceptions.driver_id=driver.driver_id AND driver.com_id="+str(com_id)
	else:
		CMD = 	"SELECT "+\
			"exceptions.key_id as ex_id,"+\
			"exceptions.type_id as ex_trg,"+\
			"exceptions.sensor_exp_starttime as creat_at,"+\
			"exceptions.exp_evidence as ex_evidence, "+\
			"driver.license as license,"+\
			"driver.driver_name as driver,"+\
			"driver.phone as telephone,"+\
			"driver.team as team "+\
			"FROM driver,exceptions "+\
			" WHERE is_processed = 'yes' AND exceptions.driver_id=driver.driver_id AND driver.com_id="+str(com_id)+\
			" AND exceptions.type_id = "+str(type_id)

	print CMD

	res_json=con_exe(CMD)
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	

	return rv
