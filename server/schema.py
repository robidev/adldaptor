COUNTRY = (
    "DC=com",
    {
        "objectClass": ["dcObject", "country"],
        "DC": ["com"],
        "description": ["Top"],
    },
)
COMPANY = (
    "DC=example",
    {
        "objectClass": ["dcObject", "organization"],
        "DC": ["example"],
        "description": ["Example inc."],
        "o": ["example"],
    },
)
PEOPLE = (
    "OU=Alliander",
    {
        "OU": ["ExampleUnit"],
        "description": ["People from Example inc."],
        "objectclass": ["organizationalunit"],
    },
)
USERS = [
    (
        "uid=admin",
        {
            "objectClass": ["ExampleUnit"],
            "objectCategory": ["person"],
            "cn": ["admin"],
            "sn": [""],
            "givenName": ["admin"],
            "uid": ["admin"],
            "mail": ["admin@example.com"],
            "userPassword": ["supersecret"],
            "samaccountname":["admin"],
            "displayname":["admin"],
        },
    ),
    (
        "uid=jsnow",
        {
            "objectClass": ["ExampleUnit"],
            "objectCategory": ["person"],
            "cn": ["jsnow"],
            "sn": [""],
            "givenName": ["John"],
            "uid": ["jsnow"],
            "mail": ["jsnow@example.com"],
            "userPassword": ["secret"],
            "samaccountname":["jsnow"],
            "displayname":["John Snow"],
        },
    ),
]
