import a
import b

assignments = a.CleanupAssignments()
assignments.result(f='input.txt')

print(assignments)


overlapping_assignments = b.CleanupAssignments()
overlapping_assignments.result(f='input.txt')

print(overlapping_assignments)
