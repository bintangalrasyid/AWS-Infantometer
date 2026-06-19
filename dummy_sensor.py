from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import random

ENDPOINT = "a3o8qiq171qnh8-ats.iot.us-east-1.amazonaws.com" 

CLIENT_ID = "Infantometer_01"
PATH_TO_CERTS = "D:/AWS_Infantometer/certs/"


ROOT_CA = PATH_TO_CERTS + "AmazonRootCA1.pem"
PRIVATE_KEY = PATH_TO_CERTS + "fbeec85ad2be64c988d6192be8e8abffd2f5f7ced68050afe113d64209015b8f-private.pem.key"
CERTIFICATE = PATH_TO_CERTS + "fbeec85ad2be64c988d6192be8e8abffd2f5f7ced68050afe113d64209015b8f-certificate.pem.crt"


myMQTTClient = AWSIoTMQTTClient(CLIENT_ID)
myMQTTClient.configureEndpoint(ENDPOINT, 8883)
myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)

print("Menghubungkan ke AWS IoT Core...")
myMQTTClient.connect()
print("Berhasil Terhubung!")


try:
    while True:
        # Menghasilkan angka acak yang logis untuk anak
        tinggi_cm = round(random.uniform(70.0, 95.0), 1)
        berat_kg = round(random.uniform(8.0, 14.0), 1)
        
        # Format payload data 
        payload = {
            "id_anak": "Cakra_01",
            "tinggi_cm": tinggi_cm,
            "berat_kg": berat_kg,
            "timestamp": int(time.time())
        }
        
        # Ubah dictionary ke format JSON string
        json_payload = json.dumps(payload)
        
        # Publish ke topik MQTT bernama "infantometer/data"
        myMQTTClient.publish("infantometer/data", json_payload, 1)
        print(f"Data Terkirim: {json_payload}")
        
        # Tunggu 5 detik sebelum mengirim data berikutnya
        time.sleep(5)

except KeyboardInterrupt:
    print("\nPengiriman data dihentikan manual oleh pengguna.")
    myMQTTClient.disconnect()