# ClusterConfig

Relying heavily on the documentation initially written by Garret Mills - https://glmdev.medium.com/building-a-raspberry-pi-cluster-784f0df9afbd- and elaborated on by Jonathon Emerick - https://www.youtube.com/watch?v=l5n62HgSQF8 - I'm updating some of the process to account for new tools and versions. 

# Hardware
I begin my quest with the basics, my stash of 3 unobtainium Raspberry Pi 4B 8G units. 

I intend to test this also on the Raspberry Pi 3B, but we'll get to a working stage before we tweak it, and where we're eventually going, we'll be needing all of the RAM we can get, and the 3 need not apply.

So per Pi we need an SD card and a power supply. We'll also need an ethernet cable to actually get performance out of it, though it works on WiFi. 

# Concepts

For this cluster implementation we'll be using SLURM as our scheduling manager. In this model we need one computer to hand out jobs and sort out the output, leaving all the others to do the work. We call the workers nodes, and they run the slurm daemon 'slurmd' and connect to the scheduler running the slurm control daemon 'slurmctld'

In my little cluster, I'm going to call the scheduler rp4n0
and the two nodes are going to be rp4n1 and rp4n2

# Sharing data

We're going to follow the smart folks and start with a flash drive connected to the scheduler, shared over the network, mounted by the nodes as an NFS share. I'd like to revisit this, but it works.

So I'll put a flash disk in rp4n0 and mount it on '/clusterfs'

then rp4n1 and rp4n2 will also mount 'rp4n0:/clusterfs' to their own '/clusterfs'

# SD Images

Gone are the days of setting up a Raspberry Pi the hard way. Imager is the only way to fly, get it as 'rpi-imager' in apt, or https://www.raspberrypi.com/software/

Now, we're going to use the 64-bit Ubuntu Server 23.04, but Imager is going to do the dirty work for us, so open it up.
Click 'Choose OS' then 'Other General-purpose OS' then 'Ubuntu' and finally "Ubuntu Server 23.04 (64-bit)"

BUT, we're gonna click on the gear

and here we get to set the hostname, the default user and password, locale, and I highly advise using keys instead of passwords over SSH

# SSH sidebar

Skip this if you want but I wanted to walk through what I mean by keys instead of passwords and explain setting it as I do.

Every time you access these computers over ssh you need to confirm who you are, you can either do it with a password, or have your computer handle it for you in a faster and more secure way. Sold? okay let's do it. 

My computer where I'm making the SD cards is my daily driver, it's also running Linux, but this works on Mac too. I don't have a Windows computer to try this, but I'm sure it's not far off. 

First, we make the keys
`ssh-keygen`
and press enter to use the default location and file name, to use no passphrase ( twice ) and you'll be rewarded with your own personal key and your key's randomart similar to mine here:

```Generating public/private rsa key pair.
Enter file in which to save the key (/home/cameron/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/cameron/.ssh/id_rsa
Your public key has been saved in /home/cameron/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:An5HU2RkNL9z4y92TkFB82doLJXt/S8K4ftib2xF2BM cameron@rp4n2
The key's randomart image is:
+---[RSA 3072]----+
|         +O   o* |
|         + o oE.=|
|    .   o   oo++=|
|   . . . .  .+=.+|
|    . o S . o.oo.|
|     . o . . +..o|
|          o. .. o|
|          oo+ +oo|
|         ..*+o =o|
+----[SHA256]-----+
```

Two things to point out here from the path is my username on this compute is 'cameron' and I'm going to keep that on the scheduler and nodes, and the file it made is in /.ssh ( a hidden folder, because of the dot ) called 'id_rsa.pub'

Have a look:
```$ cat .ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDAxsfScpYP81VgwQIbmI22Co9AhSxBtzto81kjHJSEiQ1bgK/FjKuHvX59IYHKZjxCfZstxNIyX7XrOyr/Y3iJxuGPbJEdc8qiHjn5qwpD0CzPZyvrhERne8zABM25eGbUjVrtskLWiiULu47m7lfbB5m0fxgYy2lCY+3KhhAvCSzVjSo08KHR/E5EF+jkzUASBxDRNs/NJUFPvYt+F03vpWZxB0cddjSFncXNiUZAapSaB5rPBguYDyA6HNk8tBp+j9KDYPO5FsFmHErHXUZybGgsTIYDGEGE2gtdpGAizg5xbcBM6IyuK6GNls2mFVrPNdMAvXKzyro6uMKS0XQjm4b+YCYivDEJJCmMrJBZI3SGGDGNss94thNCy5jSmKShbtQyPE4gb56BAEsgp37rkzECDbAQbRDVBReHbfK9iYmZNCDKPxFEzaU6U+ylv1sZtZU15RZRxhPs6EmJmd5uRYTfUZfC1c4zodjfjaauPQkGes4uZ82xdfpiEzpKPos= cameron@rp4n2
```
it looks like:
`<key-type> <gobbledigook key>= user@host`

and traditionally what we've needed to do in order to use the key on another system is to have an account on the remote system, a key on the local system, and use 'ssh-copy-id cameron@newhost' and log in, in order for ssh to copy the key to the newhosts' /.ssh/known_hosts file.  

So by checking "Allow Public Key authentication only" in Imager, and putting in your key, you'll neve use your password to ssh into these computers. For more information on using public keys with ssh, see https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys-on-ubuntu-20-04 to dive to the bottom of the deep end of OpenSSH Server and the security options for passwordless logins read https://ubuntu.com/server/docs/service-openssh 

# End Sidebar

Make three SD cards, changing only the hostname, and then plug it all up. No more will we fiddle with DHCP logs on our routers ( unless we lose one :) ) you know the hostnames for these. 

After a minute or so on the first boot, you'll be able to ssh into them. Fire up N tabs in your favorite terminal and ssh into your new computers. 

`ssh rp4n0.local`
`ssh rp4n1.local`
`ssh rp4n2.local`

That's why we set the hostnames in Imager.

If one doesn't resolve and log in, now you can check your DHCP leases. 

Let them all run updates while you scrounge around for a flash drive that doesn't have pictures your kid took or backups of stuff you aren't sure is safe to delete yet. 

*All machines*
`sudo apt update && sudo apt upgrade -y`

When that finishes, install ntpdate, and reboot

*All machines*
`sudo apt install ntpdate -y`
`sudo reboot now`

# Storage

Plug in the flash drive to your scheduler node and find it's ssh tab, and list the block devices. Actually, any of you who are the "read the instructions completely before beginning assembly" type will have won this round, because really you should `lsblk` before you plug in the flash drive, and after and compare to see what your drive's device is actually called. 

```$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0  67.6M  1 loop /snap/core22/611
loop1         7:1    0  68.5M  1 loop /snap/core22/861
loop2         7:2    0   155M  1 loop /snap/lxd/24646
loop3         7:3    0 161.3M  1 loop /snap/lxd/25116
loop4         7:4    0  43.2M  1 loop /snap/snapd/18600
mmcblk0     179:0    0 119.1G  0 disk 
├─mmcblk0p1 179:1    0   256M  0 part /boot/firmware
└─mmcblk0p2 179:2    0 118.8G  0 part /
cameron@rp4n0:~$ lsblk
NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
loop0         7:0    0  67.6M  1 loop /snap/core22/611
loop1         7:1    0  68.5M  1 loop /snap/core22/861
loop2         7:2    0   155M  1 loop /snap/lxd/24646
loop3         7:3    0 161.3M  1 loop /snap/lxd/25116
loop4         7:4    0  43.2M  1 loop /snap/snapd/18600
sda           8:0    1   7.5G  0 disk 
└─sda1        8:1    1   7.5G  0 part 
mmcblk0     179:0    0  29.8G  0 disk 
├─mmcblk0p1 179:1    0   256M  0 part /boot/firmware
└─mmcblk0p2 179:2    0  29.5G  0 part /

```

Gotcha "/dev/sda" is the base device with a partition on it called "sda1" yours may be called something else depending on your devices.

Format the flash drive. Here there be dragons, measure twice, cut once.

```cameron@rp4n0:~$ sudo mkfs.ext4 /dev/sda1
mke2fs 1.47.0 (5-Feb-2023)
/dev/sda1 contains a vfat file system
Proceed anyway? (y,N) y
Creating filesystem with 1953788 4k blocks and 488640 inodes
Filesystem UUID: 7dac6cba-8763-4a12-abba-146f1a410b1b
Superblock backups stored on blocks: 
	32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (16384 blocks): 
done
Writing superblocks and filesystem accounting information: done 
```

Now we somewhere to mount our new partition, I already showed that I have it mounted at /clusterfs, so let's make that

```sudo mkdir /clusterfs
sudo chown cameron:root -R /clusterfs
sudo chmod 777 -R /clusterfs```

We need to find our partiton's UUID

```$ blkid
/dev/mmcblk0p1: LABEL_FATBOOT="system-boot" LABEL="system-boot" UUID="C6C5-E1FB" BLOCK_SIZE="512" TYPE="vfat" PARTUUID="5036de4e-01"
/dev/mmcblk0p2: LABEL="writable" UUID="25a83575-fd50-4dcc-85e0-e3a81c621aa2" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="5036de4e-02"
/dev/sda1: UUID="7dac6cba-8763-4a12-abba-146f1a410b1b" BLOCK_SIZE="4096" TYPE="ext4" PARTUUID="561c8807-01"
/dev/loop1: TYPE="squashfs"
/dev/loop4: TYPE="squashfs"
/dev/loop2: TYPE="squashfs"
/dev/loop0: TYPE="squashfs"
/dev/loop3: TYPE="squashfs"```

we'll take that PARTUUID ( yours will be different ) and add it to our file system table, /etc/fstab

Edit /etc/fstab as root, and make it look like this:

```$ sudo nano /etc/fstab
LABEL=writable	/	ext4	discard,commit=30,errors=remount-ro	0 1
LABEL=system-boot       /boot/firmware  vfat    defaults        0       1
PARTUUID="561c8807-01" /clusterfs ext4 defaults 0 2
```

That line is in the following format:
`<device> <mount point> <file system type> <Options> <dump> <Pass number>`

For more information on /etc/fstab, see https://help.ubuntu.com/community/Fstab

Invoke that new mount point we wrote to /etc/fstab with

`sudo mount -a`

You'll likely get a warning about reloading the daemon that reads the fstab, just do what it says:

```cameron@rp4n0:~$ sudo mount -a
mount: (hint) your fstab has been modified, but systemd still uses
       the old version; use 'systemctl daemon-reload' to reload.
cameron@rp4n0:~$ sudo systemctl daemon-reload
```

# NFS Share, Server

Install NFS Server

`sudo apt install nfs-kernel-server -y`

and create the entry to tell NFS what to share and to whom. 


But first you'll need to check our network scheme, 

```cameron@rp4n0:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether dc:a6:32:d5:c4:d5 brd ff:ff:ff:ff:ff:ff
    altname end0
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether dc:a6:32:d5:c4:d6 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.49/24 metric 600 brd 192.168.1.255 scope global dynamic wlan0
       valid_lft 43722sec preferred_lft 43722sec
    inet6 fe80::dea6:32ff:fed5:c4d6/64 scope link 
       valid_lft forever preferred_lft forever
```
And it was at this point in writing the documentation that I realized all of my nodes were using the wireless connection instead of the perfectly good cables I plugged into them...

Anyway, you will hopefully be seeing the `inet` value on the `eth0` interface, either way, it works. The address is given in CIDR notation, the '/24' bit tells us that the first three "octets" are the network address - 192.168.1.0 - the zero meaning that no bits of the fourth octet are for the network. More about CIDR notation - https://www.digitalocean.com/community/tutorials/understanding-ip-addresses-subnets-and-cidr-notation-for-networking and https://cidr.xyz/

To share with everyone on our network, we'll use `192.168.1.0/24` to mean "all hosts on my network." Your network address could be different, for instance "10.0.0.0/8" or "192.168.100.0/24" don't worry if it doesn't match mine. 

Edit the export file:

`sudo nano /etc/exports`

And add our flash drive from its mount point:

`/clusterfs    192.168.1.0/24(rw,sync,no_root_squash,no_subtree_check)`

Now tell NFS to share it

`sudo exportfs -a`

# NFS Share, Client

To connect each node to the file share we've just created, install NFS:

*run all commands in this section on each node*
`sudo apt install nfs-common -y`

Create a folder for our mount point:

```cameron@rp4n1:~$ sudo mkdir /clusterfs
cameron@rp4n1:~$ sudo chown cameron:root /clusterfs
cameron@rp4n1:~$ sudo chmod -R 777 /clusterfs
```
And add an entry for the mount point in /etc/fstab:

`sudo nano /etc/fstab`

Adding:
`192.168.1.49:/clusterfs    /clusterfs    nfs    defaults   0 0`

Your IP will vary, but that's my scheduler's IP, the entry is the same on all the worker nodes.

Reload daemons to pull the new /etc/fstab and mount:

```cameron@rp4n1:~$ sudo systemctl daemon-reload
cameron@rp4n1:~$ sudo mount -a
```

# SLURM 

On the scheduler we'll want to edit our hosts file to simplify how we refer to our worker computers. Adding them as staticly mapped hostnames takes a load off our typing and makes it easier to remember [ rp4n1, vs 192.168.1.47 or rp4n1.local ] and takes a load off the DNS lookup [ for the .local names ].

As we did above, we can find the network address of the nodes using 

*on each worker node*
`ip a`

We then add them to the bottom of the /etc/hosts file

*on the scheduler*
`sudo nano /etc/hosts`

adding:

```192.168.1.47 rp4n1
192.168.1.48 rp4n2```

Install Slurm Workload Manager on the scheduler

`sudo apt install slurm-wlm`

Slurm is packaged with good example configurations, so let's start with the simple version. We'll copy it from the docs and into our /etc/slurm directory, and extract it with gzip ( permission denied message is because I forgot to run the gzip command as superuser, even though I asked it to write to /etc/<anything> and the sudo !! command just says, "yea I meant 'sudo whaterverIsaidjustthen' and it answers with the command you meant and runs it ). Don't forget sudo. 

```cameron@rp4n0:~$ cd /etc/slurm/        
cameron@rp4n0:/etc/slurm$ sudo cp /usr/share/doc/slurm-client/examples/slurm.conf.simple.gz .
cameron@rp4n0:/etc/slurm$ gzip -d slurm.conf.simple.gz 
gzip: slurm.conf.simple: Permission denied
cameron@rp4n0:/etc/slurm$ sudo !!
sudo gzip -d slurm.conf.simple.gz 
cameron@rp4n0:/etc/slurm$ mv slurm.conf.simple slurm.conf
```

