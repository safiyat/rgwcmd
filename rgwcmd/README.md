# rgwcmd

The commandline tool `rgwcmd` provides a cmd interface to the [Rados Gateway Admin REST API](http://docs.ceph.com/docs/master/radosgw/adminops/#add-a-user-capability) calls.

### To Do

- Provide API for metadata (user list).
- Pretty-print the returned data.
- ~~Allow a cmd parameter to change the config file location for the current operation.~~

### Issues

- Getting 403 on production. `SignatureDoesNotMatch`
- "user update -c" doesn't work.
- User creation by a uid already created ends up adding keys to it.
- ~~Config creation precedes every other activity. Even config creation itself!~~
- ~~The keys of the params passed in the request need to modified. The '_' (underscores) of the keys need to changed to '-' (hyphens).~~
