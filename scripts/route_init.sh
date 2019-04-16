#!/bin/sh
### BEGIN INIT INFO
# Provides: route.sh
# Required-Start:
# Required-Stop:
# Default-Start:  2 3 4 5
# Default-Stop:
# Short-Description: Start daemon at boot time
# Description: Enable service provided by daemon
### END INIT INFO






route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.9