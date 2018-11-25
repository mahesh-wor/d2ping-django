import subprocess
import sys
import os
from threading import Thread

sevinfoall=[
{'sev_name':'India','sevip':'116.202.224.146','ping':'unknown'},
{'sev_name':'Dubai','sevip':'185.25.183.1','ping':'unknown'},
{'sev_name':'SE Asia-1','sevip':'sgp-1.valve.net','ping':'unknown'},
{'sev_name':'SE Asia-2','sevip':'sgp-2.valve.net','ping':'unknown'},
{'sev_name':'Russia','sevip':'sto.valve.net','ping':'unknown'},
{'sev_name':'Japan','sevip':'45.121.184.100','ping':'unknown'},
{'sev_name':'Europe West','sevip':'lux.valve.net','ping':'unknown'},
{'sev_name':'Europe East','sevip':'vie.valve.net','ping':'unknown'},
{'sev_name':'Australia','sevip':'syd.valve.net','ping':'unknown'},
{'sev_name':'South Africa-1','sevip':'196.38.180.1','ping':'unknown'},
{'sev_name':'South Africa-2','sevip':'197.80.200.1','ping':'unknown'},
{'sev_name':'South Africa-3','sevip':'197.84.209.1','ping':'unknown'},
{'sev_name':'US West','sevip':'eat.valve.net','ping':'unknown'},
{'sev_name':'US East','sevip':'iad.valve.net','ping':'unknown'},
{'sev_name':'South America','sevip':'gru.valve.net','ping':'unknown'},
{'sev_name':'China UC-1','sevip':'221.228.192.0','ping':'unknown'},
{'sev_name':'China TC','sevip':'221.228.192.0','ping':'unknown'},
{'sev_name':'China UC-2','sevip':'221.228.192.0','ping':'unknown'},
]
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        #print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def pingserver(ip,sev):
    #while (time.time() - start < .5):
    #    ping_response = subprocess.Popen(["/bin/ping","-c1", ip], stdout=subprocess.PIPE).stdout.read()
    #    latency = str(ping_response)
    #    ping_value=latency.split('ms\\n\\n---')[0].split('=')[-1]
    #    print(sev,ping_value)
    #return;
    ping_response = subprocess.Popen(["/usr/bin/fping","-c1","-t400",ip], stdout=subprocess.PIPE).stdout.read()
    latency = str(ping_response)
    ping_value=latency.split('ms')[0].split(',')[-1]

    #ping_value=latency.split('ms\\n\\n---')[0].split('=')[-1]
    if len(ping_value) <= 3:
        return(sev,'unknown')
    else:
        return(sev,ping_value)

def pingfoo():
    threads_list = []
    sev_ping=[]
    for each in sevinfoall:
        name = each['sev_name']
        ip = each['sevip']
        t = ThreadWithReturnValue(target=pingserver,args=(ip,name))
        threads_list.append(t)
        t.start()
        #print(t.join())
        if t.join()[1] != 'unknown':
            tmp_ping=int(round(float(t.join()[1]),0))
        else:
            tmp_ping=t.join()[1]
        tmp_sev=t.join()[0]

        sev_ping.append({'sev_name':tmp_sev,'ping':tmp_ping})
    return(sev_ping)
