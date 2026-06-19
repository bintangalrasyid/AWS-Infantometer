import json
import pymysql

DB_HOST = "infantometer-db.cj3hfc3oaawh.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASSWORD = "cakranusantara"
DB_NAME = "stunting_data"

def lambda_handler(event, context):
    try:
        # Membuka koneksi ke database RDS
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=5
        )
        
        with connection.cursor() as cursor:
            # Mengambil data dari payload MQTT (dikirim oleh IoT Core)
            id_anak = event.get('id_anak')
            tinggi = event.get('tinggi_cm')
            berat = event.get('berat_kg')
            
            # Memasukkan data ke tabel MySQL
            sql = "INSERT INTO pengukuran (id_anak, tinggi_cm, berat_kg) VALUES (%s, %s, %s)"
            cursor.execute(sql, (id_anak, tinggi, berat))
            
            # Menyimpan perubahan
            connection.commit()
            
        return {
            'statusCode': 200,
            'body': json.dumps('Data berhasil disimpan ke RDS!')
        }
        
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Gagal menyimpan data.')
        }
    finally:
        # Menutup koneksi dengan aman
        if 'connection' in locals() and connection.open:
            connection.close()