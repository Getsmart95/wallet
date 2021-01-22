from django.db import close_old_connections
from asgiref.sync import SyncToAsync

class DatabaseSyncToAsync(SyncToAsync):

    def thread_handler(self, loop, *arg, **kwargs):
        close_old_connections()
        try:
            return super().thread_handler(loop,*args,**kwargs)
        finally:
            close_old_connections()

database_sync_to_async = DatabaseSyncToAsync