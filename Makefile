.PHONY = install uninstall

install:
	@echo "Installing REACT_TO_MQTT.service"
	su
	cp ./react_to_mqtt.service /etc/systemd/user
	ln -s /etc/systemd/system/react_to_mqtt.service /etc/systemd/user/react_to_mqtt.service
	systemctl enable react_to_mqtt.service
	
uninstall:
	@echo "Uninstalling REACT_TO_MQTT.service"
	su
	systemctl stop react_to_mqtt.service
	rm /etc/systemd/system/react_to_mqtt.service
	rm /etc/systemd/user 
