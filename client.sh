rm pipe
mkfifo pipe
nc 192.168.0.104 5002 > pipe mplayer &
mplayer -fps 31 -cache 1024 pipe
