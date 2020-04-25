# $language = "python"
# $interface = "1.0"



AP_IP = "172.16.40.150"  #AP端的IP
 
def main():
 
	crt.Session.ConnectInTab("/S " + AP_IP)
	crt.Sleep(10000)
	crt.Screen.Send("\r")
	crt.Screen.WaitForString("lct@AP:~#")
	crt.Screen.Send("exit\r")

 
main()
