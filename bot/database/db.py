import asyncpg

from settings.settings import DatabaseSettings 

class Database:
    settings = DatabaseSettings()

    async def create_database(self):
        """
        Create Database if it's not exists
        """
        connect: asyncpg.Connection = \
            await asyncpg.connect(user=self.settings.login, 
                                password=self.settings.password, 
                                host=self.settings.host,
                                )
        
        if await self._check_if_database_is_exist(connect):
            query = f"CREATE DATABASE {self.settings.name}"
            try:
                await connect.execute(query=query)
            except:
                ...
            finally:
                await connect.close()

    async def _check_if_database_is_exist(self,
        connect: asyncpg.Connection,
    ) -> bool:
        """
        Check exist database
        """
        query = (
            f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{self.settings.name}'"
        )
        database_is_exist = await connect.execute(query=query)
        if database_is_exist == "SELECT 0":
            return False
        return True