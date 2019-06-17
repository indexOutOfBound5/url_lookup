import aioredis
import json

# For future expansion of possible 'states', not just bad/good
#TODO: Do something better for this, like an enum
MALWARE_TYPE= ['bad']

class Datastore():
    def __init__(self):
        self._conn = None

    async def connect(self):
        self._conn = await aioredis.create_connection(
                'redis://redis', encoding='utf-8')

    async def disconnect(self):
        if self._conn:
            self._conn.close()
            await self._conn.wait_closed()

    #TODO setMany
    async def set_bad_url(self, url, malware_type=0):
        ok = await self._conn.execute('set',
                url, json.dumps({MALWARE_TYPE[malware_type]:True}))
        return ok == 'OK', ok

    async def get_is_url_bad(self, url, malware_type=0):
        url_resp = await self._conn.execute('get', url)
        if url_resp:
            return json.loads(url_resp)[MALWARE_TYPE[malware_type]]
        else:
            return None


