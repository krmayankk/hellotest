Check that config.py and config.example.py are kept in sync.

When a new configuration key is added to config.py, it must also appear
in config.example.py with a placeholder value. config.example.py is what
new developers copy to get started — a missing key means their app crashes
on first run with a KeyError.

Severity: high if a key exists in config.py but not in config.example.py.
