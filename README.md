# cisco-small-business-connect
connecting cisco sf500, sf300


How use it:  
#import this file is your project  
from cisco_sf_connect import CiscoSfConnect  
#Connecting devices [ip, login, password, enable_password=]  
con = CiscoSfConnect('192.168.1.1', 'cisco', 'cisco')  


#send_cisco_sf - returns a string. By default, nothing shows up on the screen  
con.send_cisco_sf('show  lldp neighbo', show=True) # This print lldp neighbors  

## Example ntp configuration   
```
from cisco_sf_connect import CiscoSfConnect  

con = CiscoSfConnect('192.168.1.1', 'cisco', 'cisco')  
if con is False:  
    exit(0)  
con.send_cisco_sf('conf t')  
con.send_cisco_sf('sntp server 192.168.10.10')  
con.send_cisco_sf('write')  
```

