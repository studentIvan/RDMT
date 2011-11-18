RDMT Perl Server

About:
Crossplatform and asyncronous rdmt-server helps you to monitor database queries and other load.

Installation:
1. Install EV, IO::Socket, Config::IniFiles modules for perl:
    cpan install EV IO::Socket Config::IniFiles
2. Change rdmt.ini configuration (port, timeout, etc...)
3. Run rdmt.pl as daemon ($, nohup, etc...)
4. Route rdmt port in iptables:

# here RDMTPORT is a rdmt port, YOURSERVERIP - your site/server external ip, of necessity

# accept localhost
    iptables -I INPUT -p tcp -s 127.0.0.1 --dport RDMTPORT -j ACCEPT

# accept external host (of necessity)
    iptables -I INPUT -p tcp -s YOURSERVERIP --dport RDMTPORT -j ACCEPT

# drop all other connections
    iptables -A INPUT -p tcp --dport RDMTPORT -j DROP