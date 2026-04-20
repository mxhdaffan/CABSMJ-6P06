server_config = {"timeout": 300, "status": "active"}

print("Status: ", server_config["status"])
print("Admin Email: ", server_config.get("admin_email", "Not Set"))
print("Number of items: ", len(server_config))

print("Keys = ", server_config.keys())
print("Values = ", server_config.values())

server_config["timeout"] = - server_config["timeout"]
server_config["max_connections"] = 100

print("\nUpdated Dictionary ->\n",server_config)

del(server_config["timeout"])
alpha = dict(sorted(server_config.items()))
print("\nUpdated Dictionary ->\n",alpha)