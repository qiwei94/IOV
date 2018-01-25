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