class BanService:
    def __init__(self, banned_users_repo):
        self.banned_users_repo = banned_users_repo

    async def ban_if_banned(self, member):
        banned_users = self.banned_users_repo.load_banned_users()
        if str(member.id) in banned_users:
            await member.ban(reason="You are banned from this server.")
            print(f"Banned {member} as they joined the server.")
