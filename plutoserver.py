def setup_plutoserver():
  return {
    "command": ["julia", "--optimize=0", "start_server.jl"],
    "environment": {
      "JSP_PORT": "{port}",
    },
    "timeout": 60,
    "launcher_entry": {
        "title": "Pluto.jl",
    },
  }
