TP-Link Archer AX1500
=====================

I don't know why they did this, but, to read your configuration backup you have to:

- Download their firmware
- Run binwalk on it
- Read a compiled lua file
- Decrypt the backup
- Uncompress it
- Untar it
- Decrypt it
- Uncompress it

:clap: thank :clap: you :clap: for :clap: protecting :clap: me :clap:

## The 🍫 ⋆ 🍒  🎀  𝓂𝒶𝑔𝒾𝒸𝒶𝓁 𝒷𝓎𝓉𝑒𝓈  🎀  🍒 ⋆ 🍫

```sh
~/TPLink-ArcherAX1500/lana $ binwalk ax1500v1-up-ver1-2-5-P1[20220117-rel51891]_2022-01-17_14.30.10.bin -eM -d0

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
8232          0x2028          LZMA compressed data, properties: 0x6D, dictionary size: 4194304 bytes, uncompressed size: 389196 bytes

WARNING: Extractor.execute failed to run external extractor 'sasquatch -p 1 -le -d 'squashfs-root-0' '%e'': [Errno 2] No such file or directory: 'sasquatch', 'sasquatch -p 1 -le -d 'squashfs-root-0' '%e'' might not be installed correctly

WARNING: Extractor.execute failed to run external extractor 'sasquatch -p 1 -be -d 'squashfs-root-0' '%e'': [Errno 2] No such file or directory: 'sasquatch', 'sasquatch -p 1 -be -d 'squashfs-root-0' '%e'' might not be installed correctly
100317        0x187DD         Squashfs filesystem, little endian, version 4.0, compression:xz, size: 13514193 bytes, 2598 inodes, blocksize: 262144 bytes, created: 2022-01-17 06:24:41
13617137      0xCFC7F1        LZMA compressed data, properties: 0x6D, dictionary size: 4194304 bytes, uncompressed size: 4992864 bytes
15524286      0xECE1BE        Flattened device tree, size: 5136 bytes, version: 17

~/TPLink-ArcherAX1500/lana $ find -name 'crypto.lua' -exec strings {} \; | grep secret -A2 | tail -n2
2EB38F7EC41D4B8E1422805BCD5F740BC3B95BE163E39D67579EB344427F7836
360028C9064242F81074F4C127D299F6
```

Usage
-----

```sh
18:53 ~/tplink-ArcherAX1500 $ ls -l
total 28
-rwxr-x--- 1 knirch knirch 15456 May  8 00:47 ArcherAX1500v120220401131n.bin
drwxr-xr-x 1 knirch knirch     0 May  8 00:47 lana
-rw-r--r-- 1 knirch knirch  2295 May  8 00:47 README.md
-rwxr-xr-x 1 knirch knirch  1122 May  8 00:47 sterling.py
-rwxr-x--- 1 knirch knirch  1210 May  8 00:47 UNLICENSE
~/tplink-ArcherAX1500 $ ./sterling.py ArcherAX1500v120220401131n.bin
~/tplink-ArcherAX1500 $ ls -l
total 92
-rwxr-x--- 1 knirch knirch 15456 May  8 00:47 ArcherAX1500v120220401131n.bin
drwxr-xr-x 1 knirch knirch     0 May  8 00:47 lana
-rw-r--r-- 1 knirch knirch 64559 May  8 00:47 ori-backup-user-config.xml
-rw-r--r-- 1 knirch knirch  2295 May  8 00:47 README.md
-rwxr-xr-x 1 knirch knirch  1122 May  8 00:47 sterling.py
-rwxr-x--- 1 knirch knirch  1210 May  8 00:47 UNLICENSE
~/tplink-ArcherAX1500 $
```


Thanks
------

- [sta-c0000](https://github.com/sta-c0000) [tpconf_bin_xml](https://github.com/sta-c0000/tpconf_bin_xml/)
- [RE-Solver](https://github.com/RE-Solver) [industrial router](https://resolverblog.blogspot.com/2023/02/tp-link-tl-r483g-industrial-router.html)
- [Matteo Croce](https://teknoraver.net/) [TP-LINK The Unreliable Choice](https://teknoraver.net/software/hacks/tplink/)
- [shreve](https://gist.github.com/shreve) [TP-Link Router Config](https://gist.github.com/shreve/7a6413f087c15b233a69bb46edcfec17)

Oh, never mind, this was already done:

- [acc-](https://github.com/acc-) [tplink-archer-c2300](https://github.com/acc-/tplink-archer-c2300/wiki/Backup-Restore-config-files)


Bugs
----
Do you want ants? Because that's how you get ants!


License
------
This "software" in the public domain.
See UNLICENSE or http://unlicense.org for more information.
