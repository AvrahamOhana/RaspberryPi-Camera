# H2 Hardware Guide
![plot](md_files/pi4-camera-port.png)
![plot](md_files/pi-configuration-menu.png)
![plot](md_files/pi-configuration-interfaces-annotated.png)
![plot](md_files/button.png)


# H2 
1. Run the command below:

```bash
$ python3 main.py
```

2. Push the button to capture image

# H3 Auto run at boot
To run the script automatically after reboot, use cron.

```bash
$ cron -e
```

use nano editor and add the command:

```text
python3 <path-to-main-file.py>
```

replace <path-to-main-file.py> with the actual path 
to your main file