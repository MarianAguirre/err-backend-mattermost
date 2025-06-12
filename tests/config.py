import logging
import os

#########################
# General Bot Settings
#########################

BACKEND = 'Mattermost'  # Usa el backend de Mattermost

# Reemplaza con tu nombre de usuario de Mattermost
BOT_ADMINS = ('@marian',)

# Directorios del bot
local_dir_path = os.path.dirname(__file__)
BOT_DATA_DIR = os.path.join(local_dir_path, "data")
BOT_EXTRA_PLUGIN_DIR = os.path.join(local_dir_path, "plugins")
BOT_EXTRA_BACKEND_DIR = os.path.join(local_dir_path, "..")

BOT_LOG_LEVEL = logging.DEBUG

#########################
# Identidad del Bot
#########################

BOT_IDENTITY = {
    'team': 'diagnocons-team',  # Nombre interno del equipo en Mattermost (no el visible)
    'server': 'chat.diagnocons.com',  # Cambia esto por tu URL de Mattermost (sin https://)
    'token': '5obhmjq1qpys5drce3u8gefzjw',  # Reemplaza con el token generado al crear el bot

    # Opcionales
    'scheme': "https",
    'port': 443,
    'timeout': 30,
    'insecure': False,
}

#########################
# Opcionales adicionales
#########################

# Si vas a usar Webhooks para adjuntos en Mattermost
# (esto es opcional y solo si ya creaste un webhook en Mattermost)
# Descomenta y edita esto si lo necesitas
# 'webhook_id': 'id_o_url_del_webhook'

# Canales donde el bot siempre estará presente
CHATROOM_PRESENCE = ('sensores')

# Formato para los nombres de los usuarios
BOT_PREFIX = "!"
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_ALT_PREFIXES = ("@",)
BOT_ALT_PREFIX_SEPARATORS = (":", ",")
DIVERT_TO_PRIVATE = ()

# Tiempo máximo de espera para plugins externos
BOT_ASYNC = False
AUTOINSTALL_DEPS = False
