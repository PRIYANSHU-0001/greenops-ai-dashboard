from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import pandas as pd
import io
import os

load_dotenv()

CONN_STR = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
print(CONN_STR)
client = BlobServiceClient.from_connection_string(CONN_STR)

blob_client = (
client
.get_container_client("greenops-data")
.get_blob_client("cloud_usage_enriched.csv")
)

data = blob_client.download_blob().readall()

df = pd.read_csv(io.BytesIO(data))

print("Shape:")
print(df.shape)

print("\nTotal CO2e:")
print(df["co2e_kg"].sum())
