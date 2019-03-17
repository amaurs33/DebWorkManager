#! /bin/sh
### BEGIN INIT INFO
# Provides: route.sh
# Required-Start:
# Required-Stop:
# Default-Start:  2 3 4 5
# Default-Stop:
# Short-Description: Start daemon at boot time
# Description: Enable service provided by daemon
### END INIT INFO

iptables -A OUTPUTqsdqsdqsdqsd-j DROP-j REJECT-j ACCEPT
iptables -A INPUTeth0-p 34-j ACCEPT