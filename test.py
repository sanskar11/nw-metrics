import sys
if len(sys.argv) == 1:
    print('nope')
    exit()
fi = open(sys.argv[1],'r')

in_diction = dict()
out_diction = dict()
for a in fi.readlines():
    try:
        if a.strip() == '': #just in case any blank line comes in start or end
            continue
        b = a[a.find('{')+1:a.find('}')].split(',')
        exec(b[0])
        exec(b[1])
    except:
        print(a)
        print(b)
    if DestinationAddress in in_diction.keys():
        in_diction[DestinationAddress] += int(a.split(' ')[1])
    else:
        in_diction[DestinationAddress] = int(a.split(' ')[1])

    if SourceAddress in out_diction.keys():
        out_diction[SourceAddress] += int(a.split(' ')[1])
    else:
        out_diction[SourceAddress] = int(a.split(' ')[1])

for key, val in in_diction.items():
    print('pcap_bytes_transfered{{DestinationAddress="{}"}} {}'.format(key,val))

for key, val in out_diction.items():
    print('pcap_bytes_transfered{{SourceAddress="{}"}} {}'.format(key,val))


fi.close()

