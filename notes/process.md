```bash
mkdir -p /var/log/rbd-clients/
```
Because it doesn't exist in the first place. :(

```
ceph-rest-api --name client.admin --conf=/etc/ceph/ceph.conf
```

```
curl 10.41.0.95:5000/api/v0.1/health


```

---
### Client end:

```python
import boto
import boto.s3.connection
access_key = 'put your access key here!'
secret_key = 'put your secret key here!'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'objects.dreamhost.com:port',
        is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat()
        )
```
