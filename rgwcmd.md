Python script

rgwcmd --configure >> configure server, port, admin user, secret and key   AND store in .configure

create users > grant priv


---
```
    User
     |
     +----Subuser
```

Users can be created, modified, viewed, suspended and removed.

A key and a secret can be specified, or generated automatically.

Subuser is Swift specific.

All commands need sudo. :(

**Create User**:
```
radosgw-admin user create --uid={username} --display-name="{display-name}" [--email={email}]
```
```json
{ "user_id": "johndoe",
  "display_name": "John Doe",
  "email": "john@example.com",
  "suspended": 0,
  "max_buckets": 1000,
  "auid": 0,
  "subusers": [],
  "keys": [
        { "user": "johndoe",
          "access_key": "11BS02LGFB6AL6H1ADMW",
          "secret_key": "vzCEkuryfn060dfee4fgQPqFrncKEIkh3ZcdOANY"}],
  "swift_keys": [],
  "caps": [],
  "op_mask": "read, write, delete",
  "default_placement": "",
  "placement_tags": [],
  "bucket_quota": { "enabled": false,
      "max_size_kb": -1,
      "max_objects": -1},
  "user_quota": { "enabled": false,
      "max_size_kb": -1,
      "max_objects": -1},
  "temp_url_keys": []}
```


**View User Info**
```
radosgw-admin user info --uid=johndoe
```

**Modify User**
```
radosgw-admin user modify --uid=johndoe --display-name="John E. Doe"
```

**Suspend | Enable User**
```
radosgw-admin user suspend | enable --uid=johndoe
```

**Remove a User**
```
radosgw-admin user rm --uid=johndoe
```

**Create a Key**
```
radosgw-admin key create --uid=johndoe:swift --key-type=s3 --gen-secret
```
```json
{ "user_id": "johndoe",
  "rados_uid": 0,
  "display_name": "John Doe",
  "email": "john@example.com",
  "suspended": 0,
  "subusers": [
     { "id": "johndoe:swift",
       "permissions": "full-control"}],
  "keys": [
    { "user": "johndoe",
      "access_key": "QFAMEDSJP5DEKJO0DDXY",
      "secret_key": "iaSFLDVvDdQt6lkNzHyW4fPLZugBAI1g17LO0+87"}],
  "swift_keys": [
    { "user": "johndoe:swift",
      "secret_key": "E9T2rUZNu2gxUjcwUBO8n\/Ev4KX6\/GprEuH4qhu1"}]
}
```

**Remove a Key**
```
radosgw-admin key rm --uid=johndoe --access-key=BBFFE670INPVNRQFWBZ5
```

**Add/Remove admin capabilities to admin**
```
radosgw-admin caps add/rm --uid={uid} --caps={caps} # --caps="[users|buckets|metadata|usage|zone]=[*|read|write|read, write]"
```

**Enable/Disable user quota**
```
radosgw-admin quota set --quota-scope=user --uid=johndoe --max-objects=1024 --max-size=1024

radosgw-admin quota enable|disable --quota-scope=user --uid=<uid>
```

**Enable/Disable Bucket Quota**
```
radosgw-admin quota set --uid=<uid> --quota-scope=bucket [--max-objects=<num objects>] [--max-size=<max size]

radosgw-admin quota enable|disable --quota-scope=bucket --uid=<uid>
```

**Update/Get user stats**
```
radosgw-admin user stats --uid=<uid> --sync-stats

radosgw-admin user stats --uid=<uid>
```

**Reading/Writing global quotas**
```
radosgw-admin regionmap get > regionmap.json

radosgw-admin regionmap set < regionmap.json
```
Restart rgw after `set`.


**Show Usage**
```
radosgw-admin usage show --uid=johndoe --start-date=2012-03-01 --end-date=2012-04-01

radosgw-admin usage show --show-log-entries=false
```

**Trim usage logs**
```
radosgw-admin usage trim --start-date=2010-01-01 --end-date=2010-12-31
radosgw-admin usage trim --uid=johndoe
radosgw-admin usage trim --uid=johndoe --end-date=2013-12-31
```
