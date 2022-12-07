import a
import b

# part a
supplies = a.Supplies()
supplies.build_stacks(f='input.txt')
supplies.run_procedure(f='input.txt')

print(supplies)


# part b
suppliesb = b.Supplies()
suppliesb.build_stacks(f='input.txt')
suppliesb.run_procedure(f='input.txt')

print(suppliesb)
