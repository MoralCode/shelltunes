#!/bin/bash

cat /dev/random | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,6,7,8,9,10,11",a,","); for (i = 0; i < 1; i += 0.00008) printf("%\n", 99*sin(1048*exp((a[$1 % 8]/12)*log(2))*i)) }' | xxd -r -p | aplay -c 2 -f S32_LE -r 24000
