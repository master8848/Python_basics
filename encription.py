encoder={"a":"c","b":"z","c":"J","d":"f","e":"y","f":"o","g":"A","h":"g","i":"k","j":"p","k":"L","l":"N","m":"q","n":"p","o":"t","p":"k","q":"H","r":"x","s":"B","t":"a","u":"n","v":"u","w":"M","x":"h","y":"0","z":"1","A":"Q","B":"9","C":"G","D":"I","E":"e","F":"C","G":"2","H":"r","I":"u","J":"3","K":"8","L":"m","M":"5","N":"l","O":"6","P":"R","Q":"F","R":"s","S":"D","T":"d","U":"v","V":"1","W":"b","X":"4","Y":"7","Z":"T","1":"0","2":"S","3":"Y","4":"W","5":"X","6":"w","7":"E","8":"Z","9":"j","0":"v"}
decoder={v: k for k, v in encoder.items()}
def get_string():
	return input("Enter your string: ")


def enconder():
	string=get_string()
	encrypted = ""
	for letter in string:
	        if letter in encoder:
	                encrypted+=encoder[letter]

	        else:
	                encrypted+=letter
	print(encrypted)

def decorder():
	string=get_string()
	encrypted = ""
	for letter in string:
	        if letter in decoder:
	                encrypted+=decoder[letter]

	        else:
	                encrypted+=letter
	print(encrypted)


initial=input("Do you want to Encode(E) or Decode(D): ").lower()

if initial[0]=="e":
	enconder()
elif initial[0]=='d':
	decorder()

