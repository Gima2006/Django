import requests

#url = "https://prod-25.brazilsouth.logic.azure.com:443/workflows/0405f332c86d4149a5ce726672f948e2/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Jb8WgI_pKfHpky6yWLAkReQ3l-AfWZTvEENs3pn_Jao"
url = "https://prod-03.brazilsouth.logic.azure.com:443/workflows/efc2a4776b93496081a147a97bf5f6aa/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=NxCjt9p41C8lawtyh6-zVGfAHdlN3oy14SUFdzpmLMw"
  
payload = { "type": "AdaptiveCard", "version": "1.0", "body": [ { "type": "TextBlock", "text": "Hello, World!", "size": "Large" } ], "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Message sent successfully!")
else:
    print("Error sending message:", response.text)



[ {"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": null,"content": {"$schema": "http://adaptivecards.io/schemas/adapt...","type": "AdaptiveCard","version": "1.2","body": [{"type": "TextBlock","text": "Hello from PostMap API....."}]}}]


summary = "UIM Alarm ID #: ${message.udata.nimid}"
               themeColor = "6600CC"
               type = "MessageCard"
               potentialAction = [{"@type":"OpenUri","name":"Ver alarma","targets":[{"os":"default","uri":"https://srvuim00.itbscorp.local/operatorconsole_portlet/standalone_login.jsp?user=itbsadmin&password=Itbs@123&view=alarm&alarmId=${message.udata.nimid}"}]},{"@type":"OpenUri","name":"Ver dispositivo","targets":[{"os":"default","uri":"https://srvuim00.itbscorp.local/operatorconsole_portlet/standalone_login.jsp?user=itbsadmin&password=Itbs@123&view=device&cs_id=${cs.id}"}]},{"@type":"OpenUri","name":"Ver alarmas del dispositivo","targets":[{"os":"default","uri":"https://srvuim00.itbscorp.local/operatorconsole_portlet/standalone_login.jsp?user=itbsadmin&password=Itbs@123&view=alarm&cs_id=${cs.id}"}]}]
               title = "Se ha generado una nueva alarma: UIM Alarm ID # ${message.udata.nimid}."
               text = "En caso de emergencia, contactar al responsable de **${message.udata.origin}**: *Eduardo Crimaldi*, eduardo.crimaldi@itbscorp.com"
               sections = [{"activityTitle":"DX UIM 20.4.9", "activitySubtitle":"Nimsoft Alarm Server", "activityImage":"https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/b8bcd073996331.5c1ca2b8ce0dc.jpg", "facts": [{"name":"Severidad","value":"**${message.udata.severity}**"},{"name":"Subsystem","value":"${message.udata.subsys}"},{"name":"Origen","value":"${message.udata.origin}"},{"name":"Descripción de métrica","value":"${metric.description}"},{"name":"Tiempo de llegada","value":"${message.udata.nimts}"},{"name":"Hostname","value":"**${message.udata.hostname}**"},{"name":"IP","value":"**${cs.ip}**"}],"text":"**${message.udata.message}**"}]
            </payload>
            
            
            
            
            
            
            
            
            <payload>              summary = "UIM Alarm ID #: ${message.udata.nimid}"               type = "MessageCard"               themeColor = "6600CC"               potentialAction = [{"@type":"OpenUri","name":"View in UIM","targets":[{"os":"default","uri":"https://srvuim00.itbscorp.local/operatorconsole_portlet/uim-alarms?alarmId=${message.udata.nimid}"}]}]               text = "En caso de emergencia, contactar al responsable de **${message.udata.origin}**: *Eduardo Crimaldi*, eduardo.crimaldi@itbscorp.com"               title = "Se ha generado una nueva alarma: UIM Alarm ID # ${message.udata.nimid}."               sections = [{"activityTitle":"DX UIM 20.4.9", "activitySubtitle":"Nimsoft Alarm Server", "activityImage":"https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/b8bcd073996331.5c1ca2b8ce0dc.jpg", "activityText":"${message.udata.message}", "facts": [{"name":"Alarm Severity","value":"${message.udata.severity}"},{"name":"Subsystem","value":"${message.udata.subsys}"},{"name":"Time of arrival","value":"${message.udata.nimts}"},{"name":"Hostname","value":"${message.udata.hostname}"},{"name":"IP","value":"${cs.ip}"}]}]            </payload> 
            
            
        
        
        [ {"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": null,"content": {"$schema": "http://adaptivecards.io/schemas/adapt...","type": "AdaptiveCard","version": "1.2","body": [{"type": "TextBlock","text": "La Alarma: **${message.udata.message}**"},{ "type": "TextBlock", "text": "Alarma detectada en **${message.udata.hostname}**.", "wrap": true }, { "type": "TextBlock", "text": "Severidad : **${message.udata.severity}** en el tiempo **${message.udata.time}**", "wrap": true }, { "type": "TextBlock", "text": "Investigar de inmediato.", "wrap": true }]}}]
        
        
        
        
       {"type": "TextBlock","text": "La Alarma: **${message.udata.message}**"},{ "type": "TextBlock", "text": "The ${message.udata.severity} alarm alarma detectada en ${message.udata.hostname}.", "wrap": true }, { "type": "TextBlock", "text": "Severidad : **${message.udata.severity}** en el tiempo **${message.udata.time}**", "wrap": true }, { "type": "TextBlock", "text": "Investigar de inmediato.", "wrap": true }
       
       
       
       [ {"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": null,"content": {"$schema": "http://adaptivecards.io/schemas/adapt...","type": "AdaptiveCard","version": "1.2","body": [{ "type": "TextBlock", "text": "Alert!", "size": "Large", "weight": "Bolder", "color": "Attention" },{"type": "TextBlock","text": "La Alarma: **${message.udata.message}**"},{ "type": "TextBlock", "text": "Alarma detectada en **${message.udata.hostname}**.", "wrap": true }, { "type": "TextBlock", "text": "Severidad : **${message.udata.severity}** en el tiempo :**${message.udata.nimts}**", "wrap": true }, { "type": "TextBlock", "text": "Investigar de inmediato.", "wrap": true }]}}]
       
       
        [ {"contentType": "application/vnd.microsoft.card.adaptive", "contentUrl": null,"content": {"$schema": "http://adaptivecards.io/schemas/adapt...","type": "AdaptiveCard","version": "1.2","body": [{ "type": "TextBlock", "text": "Alert!", "size": "Large", "weight": "Bolder", "color": "Attention" }, { "type": "TextBlock", "text": "Severity: ${message.udata.severity}", "wrap": true }, { "type": "TextBlock", "text": "Device: ${message.udata.hostname}", "wrap": true }, { "type": "TextBlock", "text": "Metric: ${message.udata.met_name}", "wrap": true }, { "type": "TextBlock", "text": "Value: ${message.udata.met_value}", "wrap": true }, { "type": "TextBlock", "text": "Creation Time: ${message.udata.creation_time}", "wrap": true }, { "type": "TextBlock", "text": "Arrival Time: ${message.udata.arrival_time}", "wrap": true }, { "type": "TextBlock", "text": "Last Update Time: ${message.udata.update_time}", "wrap": true]}}]
         
         
         
         
       
       
       
       