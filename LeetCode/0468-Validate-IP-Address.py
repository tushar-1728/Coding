class Solution:
    def validIPAddress(self, IP: str) -> str:
        IP = IP.lower()
        ver = 0
        if("." in IP):
            ver = 4
        else:
            ver = 6
        if(ver == 4):
            addr = list(IP.split("."))
            if(len(addr) != 4):
                return("Neither")
            for i in addr:
                if(not i.isdigit()):
                    return("Neither")
                    exit()
                if(int(i) < 0 or int(i) > 255):
                    return("Neither")
                if(i != str(int(i))):
                    return("Neither")
            return("IPv4")
        elif(ver == 6):
            addr = list(IP.split(":"))
            if(len(addr) != 8):
                return("Neither")
            for i in addr:
                try:
                    int(i, 16)
                except:
                    return ("Neither")
                if(not i.isalnum()):
                    return("Neither")
                if(int(i, 16) < 0 or int(i, 16) > 65535):
                    return("Neither")
                if(len(i) > 4):
                    return("Neither")
            return("IPv6")
        else:
            return("Neither")
