import sys
sys.path.insert(0, '/vagrant/repos/snailx_api/api')
from globals.globals import app
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
