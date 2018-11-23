from django.shortcuts import render

# Create your views here.
sevinfo=[
{'sev_name':'India','sevip':'116.202.224.146','ping':30},
{'sev_name':'Dubai','sevip':'185.25.183.1','ping':'unknown'},
{'sev_name':'SE Asia-1','sevip':'sgp-1.valve.net','ping':180},
{'sev_name':'SE Asia-2','sevip':'sgp-2.valve.net','ping':'unknown'},
{'sev_name':'Russia','sevip':'sto.valve.net','ping':'unknown'},
{'sev_name':'Japan','sevip':'45.121.184.100','ping':'unknown'},
{'sev_name':'Europe West','sevip':'lux.valve.net','ping':'unknown'},
{'sev_name':'Europe East','sevip':'vie.valve.net','ping':'unknown'},
{'sev_name':'Australia','sevip':'syd.valve.net','ping':20},
{'sev_name':'South Africa-1','sevip':'196.38.180.1','ping':'unknown'},
{'sev_name':'South Africa-2','sevip':'197.80.200.1','ping':'unknown'},
{'sev_name':'South Africa-3','sevip':'197.84.209.1','ping':190},
{'sev_name':'US West','sevip':'eat.valve.net','ping':'unknown'},
{'sev_name':'US East','sevip':'iad.valve.net','ping':300},
{'sev_name':'South America','sevip':'gru.valve.net','ping':'unknown'},
{'sev_name':'China UC-1','sevip':'221.228.192.0','ping':150},
{'sev_name':'China TC','sevip':'221.228.192.0','ping':'unknown'},
{'sev_name':'China UC-2','sevip':'221.228.192.0','ping':'unknown'},
]
def index(request):
    context = {
        'sevinfo': sevinfo
    }
    return render(request,'d2ping/home.html',context)
