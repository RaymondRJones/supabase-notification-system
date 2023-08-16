import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

response = supabase.table('Users').select("*").execute()
print(response)
data, count = supabase.table('Users').insert({"id": 1, "email": "t@t.com"}).execute()
print(data)

#func = supabase.functions()
#@asyncio.coroutine
#async def test_func(loop):
#  resp = await func.invoke("hello-world",invoke_options={'body':{}})
#  return resp

#loop = asyncio.get_event_loop()
#resp = loop.run_until_complete(test_func(loop))
#loop.close()
