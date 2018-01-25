######################################################################################
####################################### sensor #######################################
######################################################################################
@app.route('/sensor_info/<int:com_id>',methods=['GET'])
def get_sensor_info(com_id):
	
	#status  		取值 0 1 2 -1 （异常、在线、休眠、掉线）
	CMD = 	"SELECT "+\
			"sensor.status,"+\
			"sensor.lone ,"+\
			"sensor.late ,"+\
			"sensor.vehicle_number, "+\
			"sensor.sensor_id "+\
			"FROM sensor,vehicle "+\
			"WHERE vehicle.vehicle_id = sensor.vehicle_id AND com_id = "+str(com_id)

	print CMD

	res_json=con_exe(CMD)
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv