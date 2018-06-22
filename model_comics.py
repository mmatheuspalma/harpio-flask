import mysql.connector
from mysql_read_db_config import read_config

class ComicsModel:
    _connect = ''
    _table = 'comics'

    def __init__(self):
        self._connect = mysql.connector.connect(**read_config())  

    def getComics(self, params):
        cursor = self._connect.cursor()        

        if params.search:
            cursor.execute("SELECT * FROM %s WHERE `name` LIKE '%s' ORDER BY `%s` %s" %(self._table, '%' + params.search + '%', params.orderBy, params.order)) 
        else: 
            cursor.execute("SELECT * FROM %s ORDER BY `%s` %s" %(self._table, params.orderBy, params.order)) 

        return cursor.fetchall()

    def getComic(self, id):
        cursor = self._connect.cursor()
        cursor.execute("SELECT * FROM %s WHERE `id` = %i" %(self._table, id))    

        return cursor.fetchone()

    def createComic(self, comic):
        cursor = self._connect.cursor()
        cursor.execute("INSERT INTO %s (`name`, `description`, `thumbnail`) VALUES ('%s', '%s', '%s')" %(self._table, comic.name, comic.description, comic.thumbnail)) 

        return cursor.lastrowid

    def editComic(self, comic_id, comic): 
        cursor = self._connect.cursor()
        cursor.execute("UPDATE %s SET `name`='%s', `description`='%s', `thumbnail`='%s' WHERE `id` = %i" %(self._table, comic.name, comic.description, comic.thumbnail, comic_id))

        return comic_id

    def removeComic(self, id):
        cursor = self._connect.cursor()
        cursor.execute("DELETE FROM %s WHERE `id` = %i" %(self._table, id))    

        return id