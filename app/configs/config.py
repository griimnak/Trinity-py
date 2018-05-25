
"""
Main application config

mysql
    host     - mysql host, typically localhost
    user     - mysql username
    passw    - mysql password
    database - mysql database

site
    name - site name, can be used for <title> etc
    desc - site description, can be used for <meta desc> etc

trinity
    ip           - server ip, leave blank to point to localhost
    port         - server port
    json_backend - Currently has no purpose
"""
config = dict(
    mysql = dict(
        host = "localhost",
        user = "root",
        passw = "secret",
        database = "phpsite"
    ),

    site = dict(
        name = "Trinity-py",
        desc = "Default configuration value"
    ),

    trinity = dict(
        ip = "",
        port = 8000,
        json_backend = "json"
    )
)
