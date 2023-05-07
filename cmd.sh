sudo apt install tshark
tshark -r challenge.pcapng -Y "usbhid.data" -T fields -e usbhid.data > final.txt
python3 export.py final.txt