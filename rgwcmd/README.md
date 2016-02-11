# rgwcmd

The commandline tool `rgwcmd` provides a cmd interface to the [Rados Gateway Admin REST API](http://docs.ceph.com/docs/master/radosgw/adminops/#add-a-user-capability) calls.



### Issues

- "user update -c" doesn't work.
- Provide API for metadata (user list).
- Pretty-print the returned data.
- User creation by a uid already created ends up adding keys to it.
- ~~Config creation precedes every other activity. Even config creation itself!~~
- ~~The keys of the params passed in the request need to modified. The '_' (underscores) of the keys need to changed to '-' (hyphens).~~
