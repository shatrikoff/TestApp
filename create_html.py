import platform,socket,re,uuid,json,logging

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


f = open('index.html','w')

message = """<HTML>
<HEAD>
<TITLE>My Site</TITLE>
<SCRIPT LANGUAGE="JavaScript">
      var sizes = new Array(0,1,2,4,8,10,12);
      sizes.pos = 0;
    
function Elastic()
{
    var el = document.all.elastic
    if (null == el.direction)el.direction = 1
    else if ((sizes.pos > sizes.length - 2) || (0 == sizes.pos))
    el.direction *= -1
    el.style.letterSpacing = sizes[sizes.pos += el.direction]
setTimeout('Elastic()',100)
}

</SCRIPT>
<BODY  bgcolor=black  onLoad=Elastic()>
<CENTER>
<font color="white"><h2>Hello from <font color="yellow">Artyom Shatrov!</font><br>
Welcome to Home Page!
<font color="blue"><H1 ID="elastic" ALIGN="Center">This's my site for exam of DevOps Course!</H1>
<br>

</body>
</HTML>                 


"""

f.write(message)
f.write(getSystemInfo())
f.close()

