# /bin/bash

# copy the iso to the usb stick by dd
# Do this manully
dd if=/root/Downloads/kali-linux-2019.1a-amd64.iso of=/dev/sdb3 bs=1M


#start luks
echo "<cryptsetup luks>"

echo "<luksFormat>"
cryptsetup --verbose --verify-passphrase luksFormat /dev/sdb2
echo "</luksFormat>"

echo "<luksOpen>"
cryptsetup luksOpen /dev/sdb2 usb
echo "</luksOpen>"

echo "<mkfs.ext4>"
mkfs.ext4 /dev/mapper/usb
echo "</mkfs.ext4>"

echo "<e2label>"
e2label /dev/mapper/usb persistence
echo "</e2label>"

echo "<mkdir>"
mkdir -p /mnt/usb
echo "<?mkdir done>"

echo "<mount>"
mount /dev/mapper/usb /mnt/usb
echo "</mount>"

echo "<echo \"/ unio\">"
echo "/ union" > /mnt/usb/persistence.conf
echo "</echo \"unio\">"

echo "<umount>"
umount /dev/mapper/usb
echo "</umount>"

echo "<luksClose>"
cryptsetup luksClose /dev/mapper/usb
echo "</luksClose>"

echo "</cryptsetup luks done>"
