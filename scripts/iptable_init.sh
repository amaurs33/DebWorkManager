#!/bin/sh -e
### BEGIN INIT INFO
# Provides: firewall rules
# Required-Start: $remote_fs $syslog
# Required-Stop: $remote_fs $syslog
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Short-Description: Start daemon at boot time
# Description: Enable service provided by daemon.
### END INIT INFO

###################### Chargement des modules nécessaires ################################

modprobe iptable_nat
modprobe ip_contrack

###################### initialisation de la table Filter #################################
# je refuse tout par défaut !!!

iptables -t filter -F
iptables -t filter -X
iptables -t filter -P INPUT DROP
iptables -t filter -P FORWARD DROP
iptables -t filter -P OUTPUT DROP

##################### initialisation de la table NAT #####################################

iptables -t nat -F
iptables -t nat -X
iptables -t nat     -P PREROUTING ACCEPT
iptables -t nat     -P POSTROUTING ACCEPT
iptables -t nat     -P OUTPUT ACCEPT

##################### initialisation de la table MANGLE ##################################

iptables -t mangle -F
iptables -t mangle -X
iptables -t mangle -P PREROUTING ACCEPT
iptables -t mangle -P INPUT ACCEPT
iptables -t mangle -P OUTPUT ACCEPT
iptables -t mangle -P FORWARD ACCEPT
iptables -t mangle -P POSTROUTING ACCEPT



#table_INPUT
iptables -A INPUT -o et0 -p udp --dport 90 -m state --state NEW,ESTABLISHED,RELATED -j REJECT



#table_OUTPUT


########################################### LOG du traffic ###########################################

iptables -t filter -A OUTPUT -j LOG --log-prefix="netfilter_[ OUTPUT ]"
iptables -t filter -A INPUT -j LOG --log-prefix="netfilter_[ INPUT ]"
iptables -t filter -A FORWARD -j LOG --log-prefix="netfilter_[ FORWARD ]"
iptables -t filter -A POSTROUTING -j LOG --log-prefix="netfilter_[ POSTROUTING ]"
iptables -t filter -A PREROUTING -j LOG --log-prefix="netfilter_[ PREROUTING ]"
iptables -t filter -A MANGLE -j LOG --log-prefix="netfilter_[ MANGLE ]"
