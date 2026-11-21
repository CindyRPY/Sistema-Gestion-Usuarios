from pymongo import MongoClient

URI = "mongodb+srv://CindyPalomino:newpassword122@cluster0.qrjazka.mongodb.net/?appName=Cluster0"

client = MongoClient(URI)

def probar_conexion():
    try:
        client.admin.command("ping")
        print("Conexión exitosa!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False