vars_file = "vars.txt"
results_file = "results.txt"

with open(vars_file, "r") as file:
    variable_names = file.read().splitlines()

with open(results_file, "w") as file:
    for var_name in variable_names:
        file.write(f"""
useEffect(() => {"{"}
    console.log({var_name})
{"}"}, [{var_name}]);\n
""")