#/bin/bash

while true; do
        sleep 3
        running_process_count=$(sudo ps aux | /bin/grep -c "python /home/pi/teachercube/teacherCube.py")

        if [ $running_process_count -eq 1 ]; then
                sudo /etc/init.d/run_cube_program.sh
        fi

done &
