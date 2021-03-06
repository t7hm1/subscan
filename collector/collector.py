#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from TCG_FS import *
os_name = os.name
if os_name == 'nt':
    colorama.init()
sys.dont_write_bytecode=True

__script__  = sys.argv[0]
__version__ ='3.0'
title = '''

        ******            **  **                   **
       **////**          /** /**                  /**
      **    //   ******  /** /**  *****   *****  ******  ******  ******
     /**        **////** /** /** **///** **///**///**/  **////**//**//*
     /**       /**   /** /** /**/*******/**  //   /**  /**   /** /** /
     //**    **/**   /** /** /**/**//// /**   **  /**  /**   /** /**
      //****** //******  *** ***//******//*****   //** //****** /***
       //////   //////  /// ///  //////  /////     //   //////  ///

                           @teachyourselfhacking

Author: ___T7hM1___
Github: http://github.com/t7hm1
Version:'''+__version__+'''

                Scanning -=- Gathering -=- Collecting

'''

def check_target(t):
    try:
        return gethostbyname(t)
    except:
        sys.exit(cprint('[-] Couldn\'t resolve your target: {}'.format(t),'red'))

def ua():
    u=[]
    u.append('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0')
    u.append('Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0')
    u.append('Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0')
    u.append('Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
    u.append('Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
    u.append('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36')
    u.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
    u.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')
    u.append('Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36')
    u.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0')
    u.append('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36')
    u.append('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36')
    return u

class Web_Crawler:
    def __init__(self,tgt):
        self.tgt      = tgt
        self.c        = 0
        self.listLink = []
        self.lHandler = LinksHandler.LinksHandler()
        
    def Methods_test(self,method,port):
        tester = MethodsTester(self.tgt,port)
        if method:
            method = method.upper()
            if method == 'GET':
                tester.GET()
            elif method == 'HEAD':
                tester.HEAD()
            elif method == 'POST':
                tester.POST()
            elif method == 'PUT':
                tester.PUT()
            elif method == 'TRACE':
                tester.TRACE()
            elif method == 'DELETE':
                tester.DELETE()
            elif method == 'CONNECT':
                tester.CONNECT()
            elif method == 'OPTIONS':
                tester.OPTIONS()
            elif method == 'ALL':
                try:
                    tester.GET()
                    tester.HEAD()
                    tester.POST()
                    tester.PUT()
                    tester.TRACE()
                    tester.DELETE()
                    tester.CONNECT()
                    tester.OPTIONS()
                except KeyboardInterrupt:
                    print ProcessCannceled('Methods Testing')
            else:
                print MethodError(method)

    def Link_Scraping(self,wo):
        scraper = Extractor.Extraction(self.tgt)
        links   = scraper._find_links()
        if links:
            rmlinks = self.lHandler._remake_link(links)
            self.listLink+=rmlinks

        pem   = ExtractMultiLinks.Proc(rmlinks)
        links = pem.GiveLinks()
        self.listLink+=links
        links = self.lHandler._pass_same_link(self.listLink)

        for link in links:
            self.c+=1
            if wo == False:
                print link

            else:
                wo.write(link)
                wo.write('\n')
        print('\n[+] Found {} links').format(colored(self.c,'yellow'))


class Port_Scanner:
    def __init__(self,tgt,prange,to,quite):
        self.tgt    = tgt
        self.prange = prange
        self.to     = to
        self.quite  = quite

    def info(self):
        ip=gethostbyname(self.tgt)
        resolve_dns=lookup_dns(ip)
        rdns=resolve_dns.resolve_PTR()
        print 'Starting Collector '+__version__+' at',datetime.now().strftime('%Y-%m-%d %H:%M')
        print colored('rDNS record for {}: '.format(ip),'blue')+colored(rdns,'yellow')
        print colored('Collector scan for: ','blue')+colored(self.tgt,'green')+colored(' ({}) '.format(ip),'green')

    def Conn_scan(self):
        self.info()
        if self.quite == False:
            print 'PORT'.ljust(7)+'STATE'.ljust(7)+'SERVICE'
        else:
            pass
        scanner = connscan.ActiveThreads(self.tgt,self.to,self.prange,self.quite)
        scanner._start()

    def Stealth_scan(self):
        self.info()
        if self.quite == False:
            print 'PORT'.ljust(10)+'SERVICE'.ljust(15)+'STATE'
        else:
            pass
        scanner = stealthscan.ActiveStealth(self.tgt,self.prange,self.to,self.quite)
        scanner._start()

    def Fin_scan(self):
        self.info()
        scanner = finscan.ActiveFin(self.tgt,self.prange,self.to)
        scanner._start()

    def Ack_scan(self):
        self.info()
        scanner = ackscan.ActiveAck(self.tgt,self.prange,self.to)
        scanner._start()

    def Xmas_scan(self):
        self.info()
        scanner = xmascan.ActiveXmas(self.tgt,self.prange,self.to)
        scanner._start()

    def Null_scan(self):
        self.info()
        scanner = nullscan.ActiveNull(self.tgt,self.prange,self.to)
        scanner._start()

    def UDP_scan(self):
        self.info()
        scanner = udpscan.ActiveUdpScan(self.tgt,self.prange,self.to)
        scanner._start()

class lookup:
    def __init__(self,host,zone):
        self.host = host
        self.zone = zone
    def start(self):
        worker = lookup_dns(self.host)
        worker.some()
        worker.look_up()
        if self.zone == True:
            print colored('[*] Check DNS zone transfer','yellow')
            worker.zonetransfer()

class Whois:
    def __init__(self,host):
        self.host = host
    def start(self):
        worker = Pw(self.host)
        cprint('[*] Network Whois record','yellow')
        worker.Network_whois()
        cprint('[*] Domain Whois record','yellow')
        worker.Domain_whois()

class Sub_Scan:
    def __init__(self,hosts,quite,wf):
        self.hosts = hosts
        self.quite = quite
        self.wf    = wf

    def start(self):
        if self.quite == True:
            pass
        else:
            print 'IP Address'.ljust(21)+'Domain Name'
            print '------------'.ljust(21)+'------------'
        Scanner = SubScan.SubScanner(self.hosts,self.quite,self.wf)
        Scanner._Start_scan()

class SN_searcher:
    def __init__(self,domain,uagent,se):
        self.domain = domain
        self.uagent = uagent
        self.se   = se

    def start(self):
        if self.se == 'twitter':
            self.t_search()
        elif self.se == 'linkedin':
            self.l_search()
        elif self.se == 'email':
            self.e_search()
        elif self.se == 'googleplus' or self.se == 'gplus':
            self.gplus_search()
        else:
            sys.exit('[-] You must enter search engineer such like {}'.format(colored('twitter,linkedin,googleplus','red')))

    def t_search(self):
        cprint('[+] Twitter search','yellow')
        cprint('==================','yellow')
        searcher = Tsearch.search_twitter(self.domain,self.uagent)
        searcher.process()

    def l_search(self):
        cprint('[+] Linkedin search','yellow')
        cprint('===================','yellow')
        searcher = Lsearch.search_linkedin(self.domain,self.uagent)
        searcher.process()

    def gplus_search(self):
        cprint('[+] Google plus search','yellow')
        cprint('======================','yellow')
        searcher = Gplus.search_gplus(self.domain,self.uagent)
        searcher.process()

class Email_Hunter:
    def __init__(self):
        EmailHunter.Start()

class PingIP:
    def __init__(self,tgt,sr,er):
        self.tgt = tgt
        self.sr  = sr
        self.er  = er

    def start(self):
        ping = IPPinger(self.tgt,self.sr,self.er)
        ping.ping_process()

class get_header:
    def __init__(self,d):
        self.d = d
        self.r = None
    def request(self):
        headers={
            'User-Agent' : choice(ua()),
        }
        try:
            url = 'http://'+self.d
            self.r=requests.get(url,headers=headers)
        except Exception,e:
            sys.exit(cprint(e,'red'))
        except KeyboardInterrupt:
            sys.exit(cprint('[-] Canceled by user','red'))
    def print_result(self):
        self.request()
        code     = self.r.status_code
        reason   = self.r.reason
        mykeys   = self.r.headers.keys()
        myvalues = self.r.headers.values()
        print colored('Code: ','blue')+colored(code,'green')+'\t\t'+colored('Status: ','blue')+colored(reason,'green')
        x=0
        while x < len(mykeys):
            print colored(mykeys[x],'yellow')+'['+colored(myvalues[x],'green')+']'
            x+=1
            if x == len(mykeys):
                break

class traceroute:
    def __init__(self,tgt,hop):
        self.tgt  = tgt
        self.hop  = hop
    def start(self):
        st = Traceroute.Traceroute(self.tgt,self.hop)
        st._start_icmp()


def main():
    parser = ArgumentParser(
        add_help=False,
        usage='%(prog)s -d [domain] [OPTIONS]',
        formatter_class=RawTextHelpFormatter,
        prog=__script__,
        description=cprint(title,'green',attrs=['bold']),
        epilog = '''\
Example:
%(prog)s -i 192.168.1 -s 10 -e 100
%(prog)s -d example.com -getheader
%(prog)s -d google.com -subscan -f /path/to/worldlist
%(prog)s -d apple.com -gemail -linkedin
%(prog)s -d google.com -p 1-500 -sS
''')
    options = parser.add_argument_group('REQUIRES')
    options.add_argument('-d','--domain',metavar='',help='Specify target domain,it look like google.com.',default=False)
    options.add_argument('-i','--ip',metavar='',help='Argument for ip pinger.',default=False)
    options = parser.add_argument_group('OPTIONAL')
    options.add_argument('-p','--port',metavar='',default=False,help='Optional to choose port to traceroute or sS sU scan.')
    options.add_argument('-f','--file',metavar='',help='Optional to choose default wordlist or custom wordlist.')
    options.add_argument('-s','--srange',metavar='',default=0,help='Specify start range for ping module (default:0).')
    options.add_argument('-e','--erange',metavar='',default=256,help='Specify end range for ping module (default:256).')
    options.add_argument('-t','--timeout',metavar='',default=0.5,help='Set timeout for connectivity (default=0.5).')
    options.add_argument('-m','--method',metavar='',default='GET',help='Specify method to test.Default is GET method.')
    options.add_argument('-w','--writefile',metavar='',default=False,help='Write output to text file.')
    options.add_argument('-q','--quite',action='store_true',help='quite.')
    options = parser.add_argument_group('WEB CRAWLER')
    options.add_argument('--method-test',action='store_true',help='Test method status of website.')
    options.add_argument('--links-extractor',action='store_true',help='Links Extractor.')
    options = parser.add_argument_group('PORT SCAN TECHNIQUES')
    options.add_argument('-sC',action='store_true',help='Use socket connect() to scan ports.')
    options.add_argument('-sS',action='store_true',help='TCP SYN.')
    options.add_argument('-sF',action='store_true',help='FIN scan.')
    options.add_argument('-sA',action='store_true',help='ACK scan.')
    options.add_argument('-sX',action='store_true',help='XMAS scan.')
    options.add_argument('-sN',action='store_true',help='Null scan.')
    options.add_argument('-sU',action='store_true',help='UDP Scan.')
    options = parser.add_argument_group('WHOIS/LOOKUP DOMAIN')
    options.add_argument('-lookup',action='store_true',help='Lookup Domain.')
    options.add_argument('-whois',action='store_true',help='Whois your target.')
    options.add_argument('-subscan',action='store_true',help='Enable subdomain scan.')
    options.add_argument('--zone',action='store_true',help='Check DNS zone transfer.')
    options = parser.add_argument_group('SNSE')
    options.add_argument('-EH',action='store_true',help='Start email hunter.')
    options.add_argument('-snse',metavar='',help='Search user on social network such like '+
                                                 '\nlinkedin,twitter,googleplus(gplus).')
    options = parser.add_argument_group('NETWORK GATHERING')
    options.add_argument('-ping',action='store_true',help='Enable ping check alive ip.')
    options.add_argument('-getheader',action='store_true',help='Get a few information with headers.')
    options.add_argument('-traceroute',action='store_true',help='Traceroute your target.')
    options = parser.add_argument_group('HELP SCREEN')
    options.add_argument('-h','--help',action='store_true',help='Print help screen and exit.')
    options.add_argument('-v','--version',action='store_true',help='Print program\'s version and exit.')
    args = parser.parse_args()
    if args.help:
        sys.exit(parser.print_help())

    if args.version:
        print __version__
        sys.exit(1)

    if args.domain == False and args.ip == False and not args.EH:
        parser.print_help()
        sys.exit()

    if args.domain:
        t = args.domain
        check_target(t)

    if args.method_test:
        target = args.domain
        method = args.method
        if not args.port:
            port = 80
        else:
            port   = args.port
        cprint('[+] Methods Test','yellow')
        cprint('================','yellow')
        worker=Web_Crawler(target)
        worker.Methods_test(method,port)

    if args.links_extractor:
        target = args.domain
        if not args.writefile:
            file = False
        else:
            file = open(args.writefile,'wb+')
        cprint('[+] Links Scraping','yellow')
        cprint('==================','yellow')
        worker=Web_Crawler(target)
        worker.Link_Scraping(file)

    if args.sC:
        if not args.quite:
            quite=False
        else:
            quite=True
        if not args.port:
            port=str('0-1000')
        else:
            port=args.port
        target=args.domain
        to=args.timeout
        cprint('[+]Tcp connect scan','yellow')
        cprint('===================','yellow')
        worker=Port_Scanner(target,port,to,quite)
        worker.Conn_scan()

    if args.sS:
        quite=True
        prange=None
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        if not args.quite:
            quite=False
        if not args.port:
            prange=str('0-1001')
        else:
            prange=args.port

        tgt=args.domain
        to=args.timeout
        cprint('[+] Stealth Scan','yellow')
        cprint('=================','yellow')
        worker=Port_Scanner(tgt,prange,to,quite)
        worker.Stealth_scan()

    if args.sF:
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        if not args.port:
            prange=str('0-1000')
        else:
            prange = args.port
        tgt = args.domain
        to  = args.timeout
        cprint('[+] Fin Scan','yellow')
        cprint('============','yellow')
        worker=Port_Scanner(tgt,prange,to,None)
        worker.Fin_scan()

    if args.sA:
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        else:
            if not args.port:
                port = str('0-1000')
            else:
                port = args.port
            tgt = args.domain
            to  = args.timeout
            cprint('[+] ACK scan','yellow')
            cprint('============','yellow')
            worker = Port_Scanner(tgt,port,to,None)
            worker.Ack_scan()

    if args.sX:
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        if not args.port:
            prange = str('0-1000')
        else:
            prange = args.port
        tgt = args.domain
        to  = args.timeout
        cprint('[+] Fin Scan','yellow')
        cprint('============','yellow')
        worker = Port_Scanner(tgt,prange,to,None)
        worker.Xmas_scan()

    if args.sN:
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        if not args.port:
            prange = str('0-1000')
        else:
            prange = args.port
        tgt = args.domain
        to  = args.timeout
        cprint('[+] Fin Scan','yellow')
        cprint('============','yellow')
        worker = Port_Scanner(tgt,prange,to,None)
        worker.Null_scan()

    if args.sU:
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        else:
            if not args.port:
                port = str('0-1000')
            else:
                port = args.port
            tgt = args.domain
            to  = args.timeout
            cprint('[+] UDP port scan','yellow')
            cprint('==================','yellow')
            worker=Port_Scanner(tgt,port,to,None)
            worker.UDP_scan()

    if args.lookup:
        if not args.zone:
            zone=False
        else:
            zone=True
        cprint('[+] Lookup Domain','yellow')
        cprint('=================','yellow')
        worker = lookup(args.domain,zone)
        worker.start()

    if args.whois:
        cprint('[+] Whois Domain','yellow')
        cprint('=================','yellow')
        worker = Whois(args.domain)
        worker.start()

    if args.subscan:
        cprint('[+] Subdomain scan','yellow')
        cprint('===================\n','yellow')
        subs=[]
        if not args.file:
            for word in SubWordList.mydict:
                domain = word+'.'+args.domain
                subs.append(domain)
        else:
            for word in open(args.file,'r'):
                word = word.strip('\t').strip('\n')
                domain = word+'.'+args.domain
                subs.append(domain)
        if not args.writefile:
            wf = None
        else:
            wf = args.writefile

        if not args.quite:
            quite = False
        else:
            quite = True
        worker=Sub_Scan(subs,quite,wf)
        worker.start()

    if args.snse:
        u=ua()
        domain = args.domain
        uagent = choice(u)
        se     = args.snse
        worker = SN_searcher(domain,uagent,se)
        worker.start()

    if args.EH:
        Email_Hunter()

    if args.ping:
        if not args.ip:
            sys.exit(cprint('[-] You must enter the ip address','red'))
        else:
            pass
        try:
            ip=args.ip
            if ip:
                test=ip.split('.')
                try:
                    t=int(test[0])
                    pass
                except:
                    sys.exit(cprint('[-] You not specified ip address','red'))
            sr=int(args.srange)
            er=int(args.erange)
        except Exception,e:
            sys.exit(cprint(e,'red'))
        id=os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permisson to run this option','red'))
        else:
            cprint('[+] IP Pinger','yellow')
            cprint('=============','yellow')
            worker = PingIP(ip,sr,er)
            worker.start()

    if args.getheader:
        cprint('[+] Get headers','yellow')
        cprint('===============\n','yellow')
        worker = get_header(args.domain)
        worker.print_result()

    if args.traceroute:
        tgt=args.domain
        id = os.getuid()
        if id != 0:
            sys.exit(cprint('[-] You have not enough permission to run this option','red'))
        else:
            hop = 10
            cprint('[+] Traceroute','yellow')
            cprint('==============','yellow')
            worker=traceroute(tgt,hop)
            worker.start()

if __name__ == '__main__':
    main()
