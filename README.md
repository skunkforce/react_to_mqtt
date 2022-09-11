# react_to_mqtt
Dieses Script zeigt ein einfaches Beispiel auf eine MQTT Nachricht zu reagieren. 

Damit es richtig funktionieren kann, müssen die Umgebungsvariablen 
* REACT_TO_MQTT_ACTION
* REACT_TO_MQTT_BROKER
* REACT_TO_MQTT_PORT
* REACT_TO_MQTT_TOPIC und 
* REACT_TO_MQTT_CLIENTPREFIX 
gesetzt sein.

Das Script lädt diese aus dem Environment.
Ein einfaches Shell-Script wie hier die example_config.sh kann mit `source example_config.sh` geladen werden. 
Alternativ können die `export`-Befehle auch der eigenen `.profile`-Datei hinzugefügt werden.