async def admin_check(bot, msg, user_id=None, callback_query=None):
    if not user_id:
        user_id = msg.from_user.id
    bot_id = (await bot.get_me()).id
    if msg.chat.type not in ["supergroup", "group"]:
        await msg.reply("Perintah ini hanya dapat di gunakan di group !", quote=True)
        return False
    chat_member = await msg.chat.get_member(user_id)
    bot_chat_member = await msg.chat.get_member(bot_id)
    if bot_chat_member.status != "administrator":
        text = "tolong jadikan saya admin lalu coba lagi !"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await msg.reply(text)
        return False
    if chat_member.status not in ("creator", "administrator"):
        text = "maaf perintah ini khusus admin  !"
        if callback_query:
            await callback_query.answer(text, show_alert=True)
        else:
            await msg.reply(text)
        return False
    return True
