nc 192.168.0.104 7776
gst-launch-1.0 udpsrc port=7776 ! application/x-rtp, payload=96 ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! fpsdisplaysink sync=false text-overlay=false
