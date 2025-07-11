from locales_dict import Locale, LocalesDict

locale_en = Locale()
locale_ru = Locale()
locale_uk = Locale()
locale_de = Locale()
locale_it = Locale()
locale_pt = Locale()

locales = LocalesDict({
    'en': locale_en,
    'ru': locale_ru,
    'uk': locale_uk,
    'de': locale_de,
    'it': locale_it,
    'pt': locale_pt
}, locale_en)

# TOO_LONG_TITLE
locale_en.too_long_title = '⚠️ Your message is too long!'
locale_ru.too_long_title = '⚠️ Слишком длинное сообщение!'
locale_uk.too_long_title = '⚠️ Занадто довге повідомлення!'
locale_de.too_long_title = '⚠️ Nachricht zu lang!'
locale_it.too_long_title = '⚠️ Messaggio troppo lungo!'
locale_pt.too_long_title = '⚠️ Mensagem muito longa!'

# FOR_TITLE
locale_en.for_title = 'For %s'
locale_ru.for_title = 'Для %s'
locale_uk.for_title = 'Для %s'
locale_de.for_title = 'Für %s'
locale_it.for_title = 'Per %s'
locale_pt.for_title = 'Para %s'

# EXCEPT_TITLE
locale_en.except_title = 'Except %s'
locale_ru.except_title = 'Кроме %s'
locale_uk.except_title = 'Крім %s'
locale_de.except_title = 'Akzeptiere %s'
locale_it.except_title = 'Tranne %s'
locale_pt.except_title = 'Exceto %s'

# SPOILER_TITLE
locale_en.spoiler_title = 'Spoiler'
locale_ru.spoiler_title = 'Спойлер'
locale_uk.spoiler_title = 'Спойлер'
locale_de.spoiler_title = 'Spoiler'
locale_it.spoiler_title = 'Spoiler'
locale_pt.spoiler_title = 'Spoiler'

# TOO_LONG_MESSAGE
locale_en.too_long_message = '🥺 Sorry, your message can\'t be sent as it exceeds the limit of 500 characters.'
locale_ru.too_long_message = '🥺 Ваше сообщение не может быть отправлено, так как его длина превышает лимит в 500 символов.'
locale_uk.too_long_message = '🥺 Ваше повідомлення не може бути відправлено, так як його довжина перевищує ліміт в 500 символів.'
locale_de.too_long_message = '🥺 Sorry, deine Nachricht kann nicht gesendet werden, da sie das Limit von 500 Zeichen überschreitet.'
locale_it.too_long_message = '🥺 Mi dispiace, il tuo messaggio non può essere mandato, supera il limite di 500 caratteri.'
locale_pt.too_long_message = '🥺 Desculpe, sua mensagem não pode ser enviada, pois excede o limite de 500 caracteres.'

# FOR_MESSAGE
locale_en.for_message = '🔒 A whisper message to %s, Only he/she can open it.'
locale_ru.for_message = '🔒 Сообщение шепотом для %s, только он/она может его открыть.'
locale_uk.for_message = '🔒 Шепіт повідомлення до %s, тільки він/вона може його відкрити.'
locale_de.for_message = '🔒 A whisper message to %s, Only he/she can open it.'
locale_it.for_message = '🔒 A whisper message to %s, Only he/she can open it.'
locale_pt.for_message = '🔒 Uma mensagem sussurrada para %s, Apenas ele/ela pode abri-la.'

# EXCEPT_MESSAGE
locale_en.except_message = '🔒 A whisper message for everyone except %s, Only others can open it.'
locale_ru.except_message = '🔒 Тайное сообщение для всех, кроме %s, Только другие могут открыть его.'
locale_uk.except_message = '🔒 Приватне повідомлення для всіх, крім %s, Тільки інші можуть відкрити.'
locale_de.except_message = '🔒 Eine geheime Nachricht für alle außer %s, Nur andere können sie öffnen.'
locale_it.except_message = '🔒 Un messaggio sussurrato per tutti tranne %s, Solo altri possono aprirlo.'
locale_pt.except_message = '🔒 Uma mensagem secreta para todos exceto %s, Apenas outros podem abrir.'

# SPOILER_MESSAGE
locale_en.spoiler_message = '🔒 Spoiler Alert! Tap to reveal hidden message'
locale_ru.spoiler_message = '🔒 Спойлер! Нажмите, чтобы увидеть скрытое сообщение'
locale_uk.spoiler_message = '🔒 Спойлер! Натисніть, щоб побачити приховане повідомлення'
locale_de.spoiler_message = '🔒 Achtung Spoiler! Zum Anzeigen anklicken'
locale_it.spoiler_message = '🔒 Attenzione spoiler! Tocca per rivelare'
locale_pt.spoiler_message = '🔒 Alerta de spoiler! Toque para revelar'

# GROUP_GREETING_MESSAGE
locale_en.group_greeting_message = (
    "👋 *Welcome! I'm %s*\n\n"
    "🔒 I help send private messages that only specific people can view\n\n"
    "💡 Get started: /start@%s\n"
    "❓ Need help? Join our [Public Community](t.me/Tech_Shreyansh2)"
)

locale_ru.group_greeting_message = (
    "👋 *Добро пожаловать! Я %s*\n\n"
    "🔒 Я помогаю отправлять приватные сообщения для определённых лиц\n\n"
    "💡 Как начать: /start@%s\n"
    "❓ Нужна помощь? Вступайте в [Публичный Чат](t.me/Tech_Shreyansh2)"
)

locale_uk.group_greeting_message = (
    "👋 *Ласкаво просимо! Я %s*\n\n"
    "🔒 Допомагаю надсилати приватні повідомлення для обмеженого кола\n\n"
    "💡 Як почати: /start@%s\n"
    "❓ Потрібна допомога? Приєднуйтесь до [Публічного Чату](t.me/Tech_Shreyansh2)"
)

locale_de.group_greeting_message = (
    "👋 *Willkommen! Ich bin %s*\n\n"
    "🔒 Ich helfe beim Versenden privater Nachrichten für bestimmte Personen\n\n"
    "💡 Loslegen: /start@%s\n"
    "❓ Fragen? Trete unserer [Support Gruppe](t.me/Tech_Shreyansh2) bei"
)

locale_it.group_greeting_message = (
    "👋 *Benvenuto! Sono %s*\n\n"
    "🔒 Aiuto ad inviare messaggi privati per persone specifiche\n\n"
    "💡 Come iniziare: /start@%s\n"
    "❓ Domande? Unisciti al [Gruppo Pubblico](t.me/Tech_Shreyansh2)"
)

locale_pt.group_greeting_message = (
    "👋 *Bem-vindo! Eu sou %s*\n\n"
    "🔒 Ajudo a enviar mensagens privadas para pessoas específicas\n\n"
    "💡 Como começar: /start@%s\n"
    "❓ Dúvidas? Entre no [Grupo Público](t.me/Tech_Shreyansh2)"
)

# INFO_MESSAGE
locale_en.info_message = (
    "📚 Need Help?\n\n"
    "• Got questions after reading? We're here to help!\n"
    "• Join our community or contact support\n\n"
    "🌐 Public Discussion Group:\n@Tech_Shreyansh2\n\n"
    "🛎️ Direct Support:\n@AboutShreyansh\n\n"
    "⏰ Available 24/7"
)

locale_ru.info_message = (
    "📚 Нужна помощь?\n\n"
    "• Остались вопросы? Мы поможем!\n"
    "• Присоединяйтесь к чату или напишите в поддержку\n\n"
    "🌐 Публичный чат:\n@Tech_Shreyansh2\n\n"
    "🛎️ Поддержка:\n@AboutShreyansh\n\n"
    "⏰ Круглосуточно"
)

locale_uk.info_message = (
    "📚 Потрібна допомога?\n\n"
    "• Залишились питання? Ми допоможемо!\n"
    "• Приєднуйтесь до чату чи зверніться в підтримку\n\n"
    "🌐 Публічний чат:\n@Tech_Shreyansh2\n\n"
    "🛎️ Підтримка:\n@AboutShreyansh\n\n"
    "⏰ Цілодобово"
)

locale_de.info_message = (
    "📚 Brauchen Sie Hilfe?\n\n"
    "• Noch Fragen? Wir helfen Ihnen!\n"
    "• Treten Sie unserer Community bei oder kontaktieren Sie den Support\n\n"
    "🌐 Öffentliche Diskussionsgruppe:\n@Tech_Shreyansh2\n\n"
    "🛎️ Direkter Support:\n@AboutShreyansh\n\n"
    "⏰ Rund um die Uhr verfügbar"
)

locale_it.info_message = (
    "📚 Hai bisogno di aiuto?\n\n"
    "• Hai domande dopo la lettura? Siamo qui per aiutarti!\n"
    "• Unisciti alla nostra community o contatta il supporto\n\n"
    "🌐 Gruppo di discussione pubblica:\n@Tech_Shreyansh2\n\n"
    "🛎️ Supporto diretto:\n@AboutShreyansh\n\n"
    "⏰ Disponibile 24/7"
)

locale_pt.info_message = (
    "📚 Precisa de ajuda?\n\n"
    "• Tem dúvidas após a leitura? Estamos aqui para ajudar!\n"
    "• Junte-se à nossa comunidade ou contacte o suporte\n\n"
    "🌐 Grupo de Discussão Pública:\n@Tech_Shreyansh2\n\n"
    "🛎️ Suporte Direto:\n@AboutShreyansh\n\n"
    "⏰ Disponível 24/7"
)

# HOW_TO_USE
locale_en.how_to_use = '💡 How to use this bot?'
locale_ru.how_to_use = '💡 Как пользоваться этим ботом?'
locale_uk.how_to_use = '💡 Як користуватися цим ботом?'
locale_de.how_to_use = '💡 Wie geht das?'
locale_it.how_to_use = '💡 Come usare questo bot?'
locale_pt.how_to_use = '💡 Como usar este bot?'

# TOO_LONG_DESCRIPTION
locale_en.too_long_description = '✂️ Oops! Too long! (Max 500 characters only)'
locale_ru.too_long_description = '✂️ Упс! Слишком длинно! (Макс. 500 символов)'
locale_uk.too_long_description = '✂️ Ой! Занадто довго! (Макс. 500 символів)'
locale_de.too_long_description = '✂️ Huch! Zu lang! (Max. 500 Zeichen)'
locale_it.too_long_description = '✂️ Uh! Troppo lungo! (Max 500 caratteri)'
locale_pt.too_long_description = '✂️ Opa! Muito longo! (Máx. 500 caracteres)'


# NOT_ALLOWED
locale_en.not_allowed = '🔐 You are not allowed to view this content.'
locale_ru.not_allowed = '🔐 Вам запрещено просматривать этот контент.'
locale_uk.not_allowed = '🔐 Вам заборонено переглядати цей контент.'
locale_de.not_allowed = '🔐 Dir ist nicht gestattet, diesen Inhalt zu lesen.'
locale_it.not_allowed = '🔐 Non hai il permesso per vedere questo messaggio.'
locale_pt.not_allowed = '🔐 Você não tem permissão para visualizar este conteúdo.'

# NOT_ACCESSIBLE
locale_en.not_accessible = '⌛ This content is no longer accessible.'
locale_ru.not_accessible = '⌛ Этот контент больше недоступен.'
locale_uk.not_accessible = '⌛ Цей контент більше недоступний.'
locale_de.not_accessible = '⌛ Der Inhalt ist nicht mehr sichtbar.'
locale_it.not_accessible = '⌛ Questo contenuto non è più accessibile.'
locale_pt.not_accessible = '⌛ Este conteúdo não está mais acessível.'


# VIEW
locale_en.view = 'Show Message🔒'
locale_ru.view = 'Показать сообщение🔒'
locale_uk.view = 'Показати повідомлення🔒'
locale_de.view = 'Nachricht anzeigen🔒'
locale_it.view = 'Mostra Messaggio🔒'
locale_pt.view = 'Mostrar Mensagem🔒'

# AND_CONNECTOR
locale_en.and_connector = 'and'
locale_ru.and_connector = 'и'
locale_uk.and_connector = 'i'
locale_de.and_connector = '&'
locale_it.and_connector = 'e'
locale_pt.and_connector = 'e'

