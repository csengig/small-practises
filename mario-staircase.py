from mario-helper import staircase_generate

step_count = int(input("Stair count: "))
output_filename = input("Output file's name: ")

staircase = staircase_generate(step_count)

print(staircase)

with open(output_filename, "w") as file:
    for item in staircase:
        file.write(item + "\n")
