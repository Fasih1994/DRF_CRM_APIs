import logging
import socket
from logging.config import dictConfig

import cx_Oracle

from drf_apis.settings import DB_CONFIG, DB_USER, DB_NAME, TIMEZONE
from drf_apis.settings import env
from drf_apis.log_config import LOG_SETTINGS

dictConfig(LOG_SETTINGS)


def get_hostname():
    return socket.gethostname()


def get_oracle_db(initialize_time_zone=True):
    logger = logging.getLogger('DB_CONNECTION')
    try:
        connection_string = DB_USER + '/' + DB_CONFIG.get('password') + '@' \
                            + DB_CONFIG.get('tns')
        conn = cx_Oracle.connect(connection_string, encoding="UTF-8", nencoding="UTF-8")
        if initialize_time_zone:
            cursor = conn.cursor()
            cursor.execute("ALTER SESSION SET TIME_ZONE = '" + TIMEZONE + "'")
            cursor.close()
        return conn
    except cx_Oracle.DatabaseError as e:
        logger.critical('Unable to acquire connection with %s, error %s ' % (DB_NAME, e))
        raise


def close_cursor(cursor):
    """Closes opened cursor 'softly' returning True if cursor got closed.
    """
    if cursor:
        try:
            cursor.close()
        except cx_Oracle.InterfaceError:
            pass
    else:
        pass


def close_connection(connection):
    """Close opened cursor AND the connection that opened this cursor.
    """
    try:
        connection.close()
        pass
    except cx_Oracle.InterfaceError:
        pass


def close_cursor_and_connection(connection, cursor):
    """Close opened cursor AND the connection that opened this cursor.
    """
    close_cursor(cursor)
    close_connection(connection)