import boto3
import psycopg2

s3 = boto3.client('s3')
bucket = "healthcare-claims-data"
key = "claims.csv"

s3.download_file(bucket, key, "claims.csv")

conn = psycopg2.connect(
    dbname="healthdb",
    user="admin",
    password="password",
    host="redshift-cluster.aws.com",
    port="5439"
)
cur = conn.cursor()
cur.execute("""
    COPY claims
    FROM 's3://healthcare-claims-data/claims.csv'
    IAM_ROLE 'arn:aws:iam::1234567890:role/RedshiftCopyRole'
    CSV IGNOREHEADER 1;
""")
conn.commit()
cur.close()
conn.close()
