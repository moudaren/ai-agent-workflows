from agent.workflow import run_agent

if __name__ == "__main__":
    task = "Analyze a Path of Exile build and suggest improvements for damage and survivability"
    
    result = run_agent(task)

    print("\n=== RESULT ===")
    print(result)