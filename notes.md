 
1. Generate random data
2. print it as integers from 0-255 (?) one per line
3. for each line,
   1. set a variable a to an array with fixed values of 4,5,7,11.
   2. iterate over the value i, incrementing it by 0.0001 each time (presumably runtime?)


FOSS music service


an app of some kind that plays music via your terminal locallly instead of streaming



Version A chiptune, somewhat harsh
cat /dev/urandom | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,7,11",a,","); for (i = 0; i < 1; i += 0.0001) printf("%08X\n", 100*sin(1046*exp((a[$1 % 8]/12)*log(2))*i)) }' | xxd -r -p | aplay -c 2 -f S32_LE -r 24000

fixed sample rate: 
cat /dev/urandom | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,7,11",a,","); for (i = 0; i < 1; i += 0.0001) printf("%08X\n", 50*sin(1046*exp((a[$1 % 8]/12)*log(2))*i)) }' | xxd -r -p | aplay -c 1 -f S32_LE -r 48000



version B: slower and sadder
0.0001 -> 0.00005
cat /dev/urandom | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,7,11",a,","); for (i = 0; i < 1; i += 0.00005) printf("%08X\n", 100*sin(1046*exp((a[$1 % 8]/12)*log(2))*i)) }' | xxd -r -p | aplay -c 2 -f S32_LE -r 24000

version C 
take version A and make it +=.00008 on the iteration.
 is pretty good too


## How it works
desmos of what its doing: https://www.desmos.com/calculator/fzd5qfnxzz



printf("%08X\n", 
99*
sin(
	1048*
	exp(
		(
			a[$1 % 8]/
			12
		)*
		log(2)
	)
	*i
	)
)




## speed
if you remove the aplay part and have it dump to a file
it generates SO MUCH DATA
like in less than a second i got a 24 MB file
of one-int-per-line PCM data
like you can generate it way faster than you can play it

## save data as hex to file
cat /dev/random | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,6,7,8,9,10,11",a,","); for (i = 0; i < 1; i += 0.00008) printf("%08X\n", 99*sin(1048*exp((a[$1 % 8]/12)*log(2))*i)) }' > data.dat

## as ints 
cat /dev/random | hexdump -v -e '/1 "%u\n"' | awk '{ split("4,5,6,7,8,9,10,11",a,","); for (i = 0; i < 1; i += 0.00008) printf("%d\n", 99*sin(1048*exp((a[$1 % 8]/12)*log(2))*i)) }' > data.dat



## playback file
cat data.dat | awk '{ printf("%08X\n",$1) }' | xxd -r -p | aplay -c 2 -f S32_LE -r 24000


## saved file to raw PCM data

cat data.dat | awk '{ printf("%08X\n",$1) }' | xxd -r -p > data.pcm
