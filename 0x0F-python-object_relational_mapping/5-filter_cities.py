#!/usr/bin/python3
""" list all cities n a given state from database hbtn_0e_0_usa.
    should be in ascending order by cities.id.
    should take four arguments:
        ./2-my_filter_states.py username,
        password,
        database name,
        state name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in c.fetchall() if city[4] == sys.argv[4]]))
