# adldaptor

This minimal version of an ldap server will try to mimic Active Directory behavior. This means the UserPrincipalName (UPN) can be used to authenticate.  

The project uses the ldaptor python library, and the code is a slight modification of one of the provided examples. Therefore all credit should go to the creators of ldaptor https://github.com/twisted/ldaptor Whithout their great library, none of this would be possible.

To avoid compatibility issues it will ignore the reported ldap versioning. instead it will always blindly assume an anonymous bind.

ldaps is currently not supported

## Schema

schema.py defines the LDAP schema plus the database values. You can modify it to add/remove users, objectNames, objectClasses, objectCategories. A basic example for Example.com is provided, with 2 users; admin and jsnow, with password 'secret'

## Docker-compose file

The docker-compose file provides an easy way to get the ldap server running. By default it exposes the standard ldap port 389 on the local host, to the internal defalt port 10389. 10389 is chosen to allow the ldap server not to run as root inside the container.  
If you need this container to run on port 389, you have to set it to run as root, by commenting out `USER appuser` in the file `Dockerfile`, and changing the CMD to `CMD ["python3", "server.py","389"`. Additionally, the `ports:` section will need to be updated in the docker-compose file `docker-compose.yml`

## Prerequisites

```bash
    # apt install docker-compose
    # apt install ldap-utils
```

## Building

```bash
    $ docker-compose up -d --build
```

## Testing

If you want to check if your container works correctly, and how the schema is presented, you can enter the following command

```bash
    $ docker-compose up -d
    $ ldapsearch -h localhost -x
```

Logs can be checked with

```bash
    $ docker-compose logs -f
```

When you are done, do

```bash
    $ docker-compose down
```

## Release notes
### 0.0.1
Initial version


