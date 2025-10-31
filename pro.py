import socket,sys,time

def scan_ports(host,ports):
 print("Target:",host)
 open_ports=[]
 for p in ports:
  try:
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.settimeout(0.5)
   r=s.connect_ex((host,p))
   if r==0:
    print("Port",p,"OPEN")
    open_ports.append(p)
   s.close()
  except Exception as e:print("Err",p,e)
 if open_ports:
  print("Summary: open ports ->",open_ports)
 else:
  print("No open ports found")

def banner_grab(host,port):
 try:
  s=socket.socket();s.settimeout(1)
  s.connect((host,port))
  s.send(b"Hello\r\n")
  data=s.recv(100)
  print("Banner from",port,":",data.decode(errors="ignore"))
  s.close()
 except: pass

if __name__=="__main__":
 if len(sys.argv)<2:
  h=input("Enter host:")
 else:
  h=sys.argv[1]
 pr=range(20,102) # scanning ports 20-101
 t1=time.time()
 scan_ports(h,pr)
 for p in [21,22,80,443]:
  banner_grab(h,p)
 print("Scan finished in",round(time.time()-t1,2),"sec")