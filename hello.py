#!/usr/bin/python
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import make_response
from flask import jsonify
from flask import Response

import json
import psycopg2
import psycopg2.extras
import sys
import pprint
import time
import decimal
from psycopg2.extras import RealDictCursor

from datetime import date, datetime
from flask_cors import * 




HOST="101.200.181.242"
DBNAME="yinspect_iov"
USER="yinspect"
PASSWD="cptbtptp"


app = Flask(__name__)
CORS(app, supports_credentials=True)




class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, date): 
            return o.isoformat()
        if isinstance(o, decimal.Decimal):
            return float(o)    
        return json.JSONEncoder.default(self, o)



def con_exe(CMD):
	#Define our connection string
	conn_string = "host="+HOST +' dbname='+DBNAME+' user='+USER+' password='+PASSWD
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	#cursor = conn.cursor()
	cursor = conn.cursor(cursor_factory=RealDictCursor)
	print "Connected!\n"

	


	print CMD

	cursor.execute(CMD)
	conn.commit()
	if ("DELETE" in CMD or "UPDATE" in CMD):
		print "DELETE in CMD"
		cursor.close()
		conn.close()
		return "delete success"
	else:
		res_raw = cursor.fetchall()
	if res_raw:
		#res_json=json.dumps(res_raw,cls=DateTimeEncoder,sort_keys=True)
		res_json=res_raw
	else:
		res_json=None
	cursor.close()
	conn.close()
	return res_json

######################################################################################
####################################### driver  ######################################
######################################################################################
@app.route('/driver_com_info',methods=['POST'])
def get_com_driver():
	com_id=request.form['com_id']
	print com_id

	CMD=\
	"SELECT driver_id,driver_name,sex,license_type,license,phone,license_from_date,license_end_date,team,image,driver_address,idcard,driver_qualification,driver_qualification_date"+\
	" FROM driver "+\
	"WHERE com_id = "+str(com_id)
	
	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv




@app.route('/driver_one_com_info',methods=[' '])
def get_com_one_driver():
	com_id=request.form['com_id']
	driver_id = request.form['driver_id']
	print com_id 
	print driver_id

	CMD=\
	"SELECT driver_name,sex,idcard,phone,driver_address,license_type,license,license_from_date,license_end_date,team,image,driver_qualification,driver_qualification_date"+\
	" FROM driver "+\
	"WHERE com_id = " +str(com_id) +" AND driver_id =" +str(driver_id)
	
	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv



@app.route('/add_driver_info',methods=['POST'])
def add_driver_info():
	driver_id=request.form['driver_id']
	driver_name=request.form['driver_name']
	team=request.form['team']
	sex=request.form['sex']
	idcard=request.form['idcard']
	com_id=request.form['com_id']
	license=request.form['license']
	license_type=request.form['license_type']
	image=request.form['image']
	license_from_date=request.form['license_from_date']
	license_end_date=request.form['license_end_date']
	driver_address=request.form['driver_address']
	driver_qualification=request.form['driver_qualification']
	driver_qualification_date=request.form['driver_qualification_date']
	driver_inspect_date=request.form['driver_inspect_date']
	driver_illegal=request.form['driver_illegal']
	phone=request.form['phone']

	print driver_id
	print driver_name
	print team
	print sex
	print idcard
	print com_id
	print license
	print license_type
	print image
	print license_from_date
	print license_end_date
	print driver_address
	print driver_qualification
	print driver_qualification_date
	print driver_inspect_date
	print driver_illegal
	print phone
	

	CMD=\
	"INSERT INTO driver (driver_id,driver_name,team,sex,idcard,com_id,license,license_type,image,license_from_date,license_end_date,driver_address,driver_qualification,"+\
	"driver_qualification_date,driver_inspect_date,driver_illegal,phone) VALUES ( "+\
	"\'"+str(driver_id)+"\',"+\
	"\'"+str(driver_name)+"\',"+\
	"\'"+str(team)+"\',"+\
	"\'"+str(sex)+"\',"+\
	"\'"+str(idcard)+"\',"+\
	"\'"+str(com_id)+"\',"+\
	"\'"+str(license)+"\',"+\
	"\'"+str(license_type)+"\',"+\
	"\'"+str(image)+"\',"+\
	"\'"+str(license_from_date)+"\',"+\
	"\'"+str(license_end_date)+"\',"+\
	"\'"+str(driver_address)+"\',"+\
	"\'"+str(driver_qualification)+"\',"+\
	"\'"+str(driver_qualification_date)+"\',"+\
	"\'"+str(driver_inspect_date)+"\',"+\
	"\'"+str(driver_illegal)+"\',"+\
	"\'"+str(phone)+"\')"

	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv




@app.route('/update_driver_info',methods=['POST'])
def update_driver_info():
	driver_id=request.form['driver_id']
	driver_name=request.form['driver_name']
	team=request.form['team']
	sex=request.form['sex']
	idcard=request.form['idcard']
	com_id=request.form['com_id']
	license=request.form['license']
	license_type=request.form['license_type']
	image=request.form['image']
	license_from_date=request.form['license_from_date']
	license_end_date=request.form['license_end_date']
	driver_address=request.form['driver_address']
	driver_qualification=request.form['driver_qualification']
	driver_qualification_date=request.form['driver_qualification_date']
	driver_inspect_date=request.form['driver_inspect_date']
	driver_illegal=request.form['driver_illegal']
	phone=request.form['phone']

	print driver_id
	print driver_name
	print team
	print sex
	print idcard
	print com_id
	print license
	print license_type
	print image
	print license_from_date
	print license_end_date
	print driver_address
	print driver_qualification
	print driver_qualification_date
	print driver_inspect_date
	print driver_illegal
	print phone
	

	CMD=\
	"UPDATE driver SET driver_name = "+\
	"\'"+str(team)+"\',sex ="+\
	"\'"+str(sex)+"\',idcard ="+\
	"\'"+str(idcard)+"\',com_id ="+\
	"\'"+str(com_id)+"\',license ="+\
	"\'"+str(license)+"\',license_type ="+\
	"\'"+str(license_type)+"\',image ="+\
	"\'"+str(image)+"\',license_from_date ="+\
	"\'"+str(license_from_date)+"\',license_end_date ="+\
	"\'"+str(license_end_date)+"\',driver_address ="+\
	"\'"+str(driver_address)+"\',driver_qualification="+\
	"\'"+str(driver_qualification)+"\',driver_qualification_date ="+\
	"\'"+str(driver_qualification_date)+"\',driver_inspect_date ="+\
	"\'"+str(driver_inspect_date)+"\',driver_illegal ="+\
	"\'"+str(driver_illegal)+"\', phone ="+\
	"\'"+str(phone)+"\'"+\
	" WHERE driver_id = "+str(driver_id)


	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv



@app.route('/delete_driver_info',methods=['POST'])
def delete_driver_info():
	driver_id=request.form['driver_id']
	print driver_id

	CMD=\
	"DELETE FROM driver WHERE driver_id = "+str(driver_id) 

	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv


######################################################################################
####################################### vehicle ######################################
######################################################################################


@app.route('/vehicle_com_info',methods=['POST'])
def get_com_vehicle():
	com_id=request.form['com_id']
	print com_id

	CMD=\
	"SELECT 	vehicle.vehicle_id,"+\
	"		vehicle.vehicle_number,"+\
	"		vehicle.vehicle_type,"+\
	"		vehicle.inspect_date,"+\
	"		vehicle.flapper,"+\
	"		vehicle.tonnage,"+\
	"		vehicle.engine,"+\
	"		vehicle.frame,"+\
	"		vehicle.insurance_startdate,"+\
	"		vehicle.insurance_enddate,"+\
	"		vehicle.service_date,"+\
	"		vehicle.image,"+\
	"		company.com_name "+\
	"FROM  	company,vehicle "+\
	"WHERE	vehicle.com_id = company.com_id AND vehicle.com_id = "+com_id
	
	res_json = con_exe(CMD)
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv



@app.route('/com_next_vehicle_info',methods=['POST'])
def get_com_next_vehicle():
	
	com_id=request.form['com_id']
	print com_id
	vehicle_id=request.form['vehicle_id']
	print vehicle_id

	CMD="SELECT	vehicle_number,"+\
	"vehicle_type,"+\
	"inspect_date,"+\
	"flapper,"+\
	"tonnage,"+\
	"engine,"+\
	"frame,"+\
	"insurance_startdate,"+\
	"insurance_enddate,"+\
	"service_date,"+\
	"image "+\
	"FROM 	vehicle "+\
	"WHERE 	vehicle_id = "+vehicle_id+\
	" AND com_id ="+com_id
	
	print CMD

	res_json= con_exe(CMD)

	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv


@app.route('/add_vehicle_info',methods=['POST'])
def add_vehicle():
	
	vehicle_id=request.form['vehicle_id']
	vehicle_number=request.form['vehicle_number']
	vehicle_type=request.form['vehicle_type']
	sensor_id=request.form['sensor_id']
	com_id=request.form['com_id']
	service_date=request.form['service_date']
	inspect_date=request.form['inspect_date']
	flapper=request.form['flapper']
	tonnage=request.form['tonnage']
	engine=request.form['engine']
	frame=request.form['frame']
	insurance_startdate=request.form['insurance_startdate']
	insurance_enddate=request.form['insurance_enddate']
	image=request.form['image']
	driver_id=request.form['driver_id']
	time_to_dep=request.form['time_to_dep']
	act_time_to_dep=request.form['act_time_to_dep']
	time_to_arri=request.form['time_to_arri']
	act_time_to_arri=request.form['act_time_to_arri']
	departure=request.form['departure']
	destination=request.form['destination']


	
	CMD="INSERT INTO vehicle (vehicle_id,vehicle_number,vehicle_type,sensor_id,com_id,service_date,inspect_date,flapper,tonnage,"+\
	"engine,frame,insurance_startdate,insurance_enddate,image,driver_id,time_to_dep,act_time_to_dep,time_to_arri,"+\
	"act_time_to_arri,departure,destination) "+\
	"VALUES ("+\
	"\'"+str(vehicle_id)+"\',"+\
	"\'"+str(vehicle_number)+"\',"+\
	"\'"+str(vehicle_type)+"\',"+\
	"\'"+str(sensor_id)+"\',"+\
	"\'"+str(com_id)+"\',"+\
	"\'"+str(service_date)+"\',"+\
	"\'"+str(inspect_date)+"\',"+\
	"\'"+str(flapper)+"\',"+\
	"\'"+str(tonnage)+"\',"+\
	"\'"+str(engine)+"\',"+\
	"\'"+str(frame)+"\',"+\
	"\'"+str(insurance_startdate)+"\',"+\
	"\'"+str(insurance_enddate)+"\',"+\
	"\'"+str(image)+"\',"+\
	"\'"+str(driver_id)+"\',"+\
	"\'"+str(time_to_dep)+"\',"+\
	"\'"+str(act_time_to_dep)+"\',"+\
	"\'"+str(time_to_arri)+"\',"+\
	"\'"+str(act_time_to_arri)+"\',"+\
	"\'"+str(departure)+"\',"+\
	"\'"+str(destination)+"\'"+")"

	
	print CMD

	res_json=con_exe(CMD)
	

	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	
	return rv

@app.route('/update_vehicle_info',methods=['POST'])
def update_vehicle_info():
	vehicle_id=request.form['vehicle_id']
	vehicle_number=request.form['vehicle_number']
	vehicle_type=request.form['vehicle_type']
	sensor_id=request.form['sensor_id']
	com_id=request.form['com_id']
	service_date=request.form['service_date']
	inspect_date=request.form['inspect_date']
	flapper=request.form['flapper']
	tonnage=request.form['tonnage']
	engine=request.form['engine']
	frame=request.form['frame']
	insurance_startdate=request.form['insurance_startdate']
	insurance_enddate=request.form['insurance_enddate']
	image=request.form['image']
	driver_id=request.form['driver_id']
	time_to_dep=request.form['time_to_dep']
	act_time_to_dep=request.form['act_time_to_dep']
	time_to_arri=request.form['time_to_arri']
	act_time_to_arri=request.form['act_time_to_arri']
	departure=request.form['departure']
	destination=request.form['destination']


	
	CMD="UPDATE vehicle  set vehicle_number="+\
	"\'"+str(vehicle_number)+"\',vehicle_type="+\
	"\'"+str(vehicle_type)+"\',sensor_id="+\
	"\'"+str(sensor_id)+"\',com_id="+\
	"\'"+str(com_id)+"\',service_date="+\
	"\'"+str(service_date)+"\',inspect_date="+\
	"\'"+str(inspect_date)+"\',flapper="+\
	"\'"+str(flapper)+"\',tonnage="+\
	"\'"+str(tonnage)+"\',=engine"+\
	"\'"+str(engine)+"\',frame="+\
	"\'"+str(frame)+"\',insurance_startdate="+\
	"\'"+str(insurance_startdate)+"\',insurance_enddate="+\
	"\'"+str(insurance_enddate)+"\',image="+\
	"\'"+str(image)+"\',driver_id="+\
	"\'"+str(driver_id)+"\',time_to_dep="+\
	"\'"+str(time_to_dep)+"\',act_time_to_dep="+\
	"\'"+str(act_time_to_dep)+"\',time_to_arri="+\
	"\'"+str(time_to_arri)+"\',act_time_to_arri="+\
	"\'"+str(act_time_to_arri)+"\',departure="+\
	"\'"+str(departure)+"\',destination="+\
	"\'"+str(destination)+"\'"+" WHERE vehicle_id="+str(vehicle_id)



	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv

@app.route('/delete_vehicle_info',methods=['POST'])
def delete_vehicle_info():
	vehicle_id=request.form['vehicle_id']
	print vehicle_id

	CMD=\
	"DELETE FROM vehicle WHERE vehicle_id = "+str(vehicle_id) 

	res_json = con_exe(CMD)
	
	
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv

######################################################################################
##################################### company ########################################
######################################################################################

@app.route('/get_company_son',methods=['POST'])
def get_company_son():
	com_id=request.form['com_id']
	print com_id

	CMD="SELECT com_id as value,"+\
		"com_name as label "+\
	 	"FROM company WHERE father = "+str(com_id) 

	res_json = con_exe(CMD)
	
	if res_json == None:
		CMD="SELECT com_id as value,"+\
		"com_name as label "+\
	 	"FROM company WHERE com_id = "+str(com_id) 
		res_json = con_exe(CMD)
		
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv

@app.route('/get_company',methods=['GET'])
def get_company():
	
	CMD="SELECT com_id as value,"+\
		"com_name as label "+\
	 	"FROM company"

	res_json = con_exe(CMD)
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv



######################################################################################
####################################### login ########################################
######################################################################################

def valid_login(username,password):
	#Define our connection string
	conn_string = "host="+HOST +' dbname='+DBNAME+' user='+USER+' password='+PASSWD
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"

	CMD="SELECT count(*) from users where username=\'" + str(username)+"\';"
	#CMD="SELECT * from vehicle;"
	
	print CMD
	records=cursor.execute(CMD)
	conn.commit()
	res_raw = cursor.fetchall()
	#res=json.dumps(res_raw,cls=DateTimeEncoder,indent=2,sort_keys=True)
	count=int(res_raw[0][0])
	if count == 1:
		print "has the user"
		CMD="SELECT password from users where username=\'" + str(username)+"\';"
		records=cursor.execute(CMD)
		conn.commit()
		pass_get = cursor.fetchall()
		pass_raw = pass_get[0][0]
		print pass_raw
		if pass_raw == password:
			print "success"
			return 1
		else:
			print "passwd error"
			return 0

	else:
		cursor.close()
		conn.close()
		return 0
	cursor.close()
	conn.close()


@app.route('/login',methods=['POST'])
def login():
	
	username=request.form['username']
	password=request.form['password']

	print username
	print password

	if valid_login(username,password):
		res_data={"type":"success","data":"OK","msg":"dengluchenggong"}
		res=json.dumps(res_data)
		rv = make_response(res,200)
	else:
		res_data={"type":"failure","data":"NOT OK","msg":"dengluSHIBAI"}
		res=json.dumps(res_data)
		rv = make_response(res,200)

	return rv





######################################################################################
##################################### exception ######################################
######################################################################################

@app.route('/exceptions',methods=['GET'])
def get_exception():
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
			"WHERE is_processed = 'no' AND exceptions.driver_id=driver.driver_id "

	print CMD

	res_json=con_exe(CMD)
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	
	return rv


@app.route('/exceptions/report/<int:ex_id>',methods=['GET'])
def report_exception(ex_id):
	

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
			"WHERE is_processed = 'no' AND exceptions.driver_id=driver.driver_id AND exceptions.key_id="+\
			str(ex_id)

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


@app.route('/exceptions/get_processed',methods=['GET'])
def get_processed_exception():
	
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
			"WHERE is_processed = 'yes' AND exceptions.driver_id=driver.driver_id "

	print CMD

	res_json=con_exe(CMD)
	
	res_return={"type":"success","data":res_json,"msg":"success"}
	#res_return=res_json
	res=json.dumps(res_return,cls=DateTimeEncoder,indent=2,sort_keys=True)
	rv = make_response(res,200)
	

	return rv



######################################################################################
####################################### sensor #######################################
######################################################################################
@app.route('/sensor_info/<int:com_id>',methods=['GET'])
def get_sensor_info(com_id):
	
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









if __name__ == '__main__':
	app.debug = True
	app.config.update(
		DEBUG=True,
		)
	app.run(host='0.0.0.0')
