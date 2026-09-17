from foundry_client import make_client, ask

client = make_client()

deployments = ["deepseek-v3-0324", "your-second-deployment"]
prompt = "In one sentence, why do teams use keyless authentication?"

for name in deployments:
    print(f"--- {name} ---")
    print(ask(client, name, prompt))
    print()
