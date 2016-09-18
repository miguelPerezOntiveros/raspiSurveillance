rm pipe 
mkfifo pipe
cat pipe | nc 192.168.0.104 5001 &
raspivid -o pipe -t 99999