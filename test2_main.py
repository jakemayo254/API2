from unittest import IsolatedAsyncioTestCase
import main

class Test_Main(IsolatedAsyncioTestCase):
    async def testHello(self):
        key = "Jake"
        result = await main.say_hello("Jake")
        res = any(str1 in string for string in lst)
        print(result.values())
