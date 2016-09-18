rm pipe
mkfifo pipe
nc -l -p 5001 < pipe | nc -l -p 5002 > pipe