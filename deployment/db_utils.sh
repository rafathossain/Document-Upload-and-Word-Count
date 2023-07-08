#!/bin/bash

mariadb_ready() {
  python <<END
import sys
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="${DB_HOST}",
        user="${DB_USERNAME}",
        password="${DB_PASSWORD}",
        port="${DB_PORT}"
    )
except mysql.connector.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

create_table() {
  python <<END
import sys
import mysql.connector
try:
    mydb = mysql.connector.connect(
        host="${DB_HOST}",
        user="${DB_USERNAME}",
        password="${DB_PASSWORD}",
        port="${DB_PORT}",
        database="${DB_DATABASE}"
    )

    my_cursor = mydb.cursor()
    my_cursor.execute("SHOW TABLES")
    exists = False
    for x in my_cursor:
      if x == 'count_log':
        exists = True
        break

    if not exists:
      my_cursor = mydb.cursor()
      my_cursor.execute("CREATE TABLE `count_log` (
        `id` int(11) NOT NULL,
        `file_name` varchar(255) NOT NULL,
        `file_path` text NOT NULL,
        `k` int(11) NOT NULL,
        `word_count` int(11) NOT NULL,
        `status` varchar(255) NOT NULL,
        `updated_at` datetime NOT NULL DEFAULT current_timestamp()
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;")
      my_cursor.execute("ALTER TABLE `count_log` ADD PRIMARY KEY (`id`);")
      my_cursor.execute("ALTER TABLE `count_log` MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;")
      mydb.commit()
except mysql.connector.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}