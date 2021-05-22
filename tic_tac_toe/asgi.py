
import os
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tic_tac_toe.settings')

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
#(We can add other protocols later.)
})
