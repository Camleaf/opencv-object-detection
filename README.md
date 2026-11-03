# OpenCV object detection

Practice for FRC game piece detection

This project uses [vcpkg](https://github.com/microsoft/vcpkg) for managing packages

### Notes

You need to add this script to `~/.bashrc`
```
eval `ssh-agent -s > /dev/null`

# If using building with VCPKG
export VCPKG_ROOT="$HOME/vcpkg"
export PATH="$VCPKG_ROOT:$PATH"

```

And this script to `~/.bash_logout`
```
eval `ssh-agent -k`
/usr/bin/clear
```
