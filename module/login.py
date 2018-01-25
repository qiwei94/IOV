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
