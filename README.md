# Network Scanner

## Help
```
python network_scanner.py --help
```

## Options
```
Options:
  -h, --help            show this help message and exit
  -t, --target			Target IP / IP range
```

## Example command for MacOSX
```
sudo python network_scanner.py  -t 127.0.0.1/24
```

## Example command for Linux
```
sudo python network_scanner.py  --target 127.0.0.1/24
```

### Currently does NOT work with Python3
### Optparse while still widely used is considered deprecated to argparse

#### ToDo:
1. Upgrade to Python3
2. Upgrade to Argparse
